from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "mariadb+mariadbconnector://root:root@db:3306/oga-gpt"

engine = create_engine(DATABASE_URL, echo=True)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)
