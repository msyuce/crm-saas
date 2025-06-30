from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.tenant import TenantCreate, TenantRead
from app.models.tenant import Tenant
from app.db.database import database
from sqlalchemy import select

router = APIRouter()

@router.post("/", response_model=TenantRead, status_code=status.HTTP_201_CREATED)
async def create_tenant(tenant: TenantCreate):
    query = Tenant.__table__.insert().values(name=tenant.name, language=tenant.language)
    tenant_id = await database.execute(query)
    return {**tenant.dict(), "id": tenant_id}

@router.get("/", response_model=List[TenantRead])
async def read_tenants():
    query = select(Tenant)
    results = await database.fetch_all(query)
    return results

