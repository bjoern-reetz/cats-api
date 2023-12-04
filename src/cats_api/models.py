from datetime import date, timedelta
from decimal import Decimal
from uuid import uuid4

from pydantic import BaseModel, Field, computed_field


def get_namespaces_id_factory(namespace: str):
    return lambda: f"id.{namespace}.{uuid4().hex[:9]}"


class Cat(BaseModel):
    id: str = Field(default_factory=get_namespaces_id_factory("cat"))
    born_at: date
    name: str
    race: str

    @computed_field
    @property
    def age(self) -> timedelta:
        return date.today() - self.born_at


class Toy(BaseModel):
    id: str = Field(default_factory=get_namespaces_id_factory("toy"))
    name: str
    price_in_euro: Decimal = Field(decimal_places=2)


class PlayingSession(BaseModel):
    id: str = Field(default_factory=get_namespaces_id_factory("playing-session"))
    duration: timedelta

    cat_id: str
    toy_id: str
