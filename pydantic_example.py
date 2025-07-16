from pydantic import BaseModel, Field

class Address(BaseModel):
    zip: str
    city: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias='isActive')


user = User(id=1,
            name="Alice",
            email="alice@example.com",
            is_active=0,
            address=Address(city="Paris", zip="90215"))

print(user.model_dump())
print(user.model_dump_json())