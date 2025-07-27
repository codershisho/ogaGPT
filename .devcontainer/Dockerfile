# ベースイメージを指定
FROM python:3.12

# Node.js, pnpm のインストール
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g pnpm

# 作業ディレクトリを作成
WORKDIR /workspace

# 必要なパッケージをインストール
COPY ./backend/pyproject.toml /workspace/backend/
RUN cd /workspace/backend/ && pip install --no-cache-dir .

# COPY ./frontend/package.json ./frontend/pnpm-lock.yaml /workspace/frontend/
# RUN cd /workspace/frontend && pnpm install

# アプリケーションのソースコードをコピー
# COPY ./backend .

# アプリケーションを起動
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]