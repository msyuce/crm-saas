from pydantic import BaseModel

class TenantBase(BaseModel):
    name: str
    language: str | None = None

class TenantCreate(TenantBase):
    pass

class TenantRead(TenantBase):
    id: int

    class Config:
        orm_mode = True

