from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.tenant import Tenant
from app.schemas.tenant import TenantCreate

async def get_all_tenants(db: AsyncSession):
    result = await db.execute(select(Tenant))
    return result.scalars().all()

async def create_tenant(db: AsyncSession, tenant: TenantCreate):
    db_tenant = Tenant(**tenant.dict())
    db.add(db_tenant)
    await db.commit()
    await db.refresh(db_tenant)
    return db_tenant
