from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel, text


class TManualBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=255, index=True)
    content: str = Field(max_length=10000)
    url: str = Field(max_length=255, index=True)
    created_at: datetime | None = Field(default=None, sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")})
    updated_at: datetime | None = Field(
        default=None,
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP"), "onupdate": text("CURRENT_TIMESTAMP")},
    )
    deleted_at: datetime | None = Field(default=None)


class TManual(TManualBase, table=True):
    __tablename__ = "t_manuals"  # type: ignore
    __table_args__ = {"comment": "手順書の情報を格納するテーブル"}

    # リレーション定義
    queries: list["TManualQuery"] = Relationship(back_populates="manual")


class TManualQueryBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    manual_id: int = Field(foreign_key="t_manuals.id")
    query: str = Field(max_length=255, index=True)
    created_at: datetime | None = Field(default=None, sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")})
    updated_at: datetime | None = Field(
        default=None,
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP"), "onupdate": text("CURRENT_TIMESTAMP")},
    )
    deleted_at: datetime | None = Field(default=None)


class TManualQuery(TManualQueryBase, table=True):
    __tablename__ = "t_manual_queries"  # type: ignore
    __table_args__ = {"comment": "手順書のクエリ情報を格納するテーブル"}

    # リレーション定義
    manual: TManual = Relationship(back_populates="queries")
