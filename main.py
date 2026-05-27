import pydantic
from pydantic import BaseModel, field_validator, ValidationError, Field
from datetime import datetime, UTC
from functools import partial
from typing import Literal


class User(BaseModel):
    uid: int
    name: str
    email: str
    bio: str = ""
    isActive: bool = True
    full_name: str | None = None
    verified_at: datetime | None = None


try:
    user = User(uid=12, name="dfhurhf", email="dfyeffy")
except ValidationError as e:
    print(e)


print(user.model_dump_json(indent=2))


class BlogPost(BaseModel):
    title: str
    content: str
    view_count: int = 0
    is_published: bool = False

    tags: list[str] = Field(default_factory=list)

    create_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))

    author_id: str | int

    status: Literal["draft", "published", "archived"] = "draft"
