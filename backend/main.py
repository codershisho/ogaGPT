from typing import Annotated

import numpy as np
from fastapi import Depends, FastAPI
from janome.tokenizer import Tokenizer
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sqlmodel import Session, select

from db import get_session
from models.schema import TManual

app = FastAPI()

model = SentenceTransformer("sonoisa/sentence-bert-base-ja-mean-tokens")
tokenizer = Tokenizer()


def preprocess(text: str) -> str:
    tokens = tokenizer.tokenize(text)
    return " ".join([t.surface for t in tokens])


def load_manuals(session: Session) -> tuple[list[TManual], list[list[float]]]:
    statement = select(TManual).where(TManual.deleted_at.is_(None))  # type: ignore
    manuals = list(session.exec(statement).all())
    texts = [
        preprocess(
            manual.title + " " + manual.content + " " + " ".join(query.query for query in manual.queries),
        )
        for manual in manuals
    ]
    vectors = model.encode(texts).tolist()
    return manuals, vectors


class Message(BaseModel):
    text: str


@app.post("/chat")
def chat(
    message: Message,
    session: Annotated[Session, Depends(get_session)],
) -> dict:
    user_input = preprocess(message.text)
    query_vec = model.encode([user_input])

    # 手順書をDBから読み込み、ベクトルを作成
    manuals, manual_vectors = load_manuals(session)

    if not manuals:
        return {"reply": "手順書データが見つかりません。", "manuals": []}

    scores = cosine_similarity(query_vec, np.array(manual_vectors))[0]

    top_n = 3
    top_indices = np.argsort(scores)[::-1][:top_n]

    # スコアが一定以上の手順書のみを対象とする（例: 0.7）
    top_manuals = [
        {
            "title": manuals[i].title,
            "url": manuals[i].url,
            "score": float(scores[i]),
        }
        for i in top_indices
        if scores[i] >= 0.5
    ]

    if not top_manuals:
        return {
            "reply": "申し訳ありません、該当する手順書が見つかりませんでした。",
            "manuals": [],
        }

    return {
        "reply": "こちらの手順書が参考になるかもしれません：",
        "manuals": [{"title": manual["title"], "url": manual["url"]} for manual in top_manuals],
    }
