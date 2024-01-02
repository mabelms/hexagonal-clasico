from fastapi import APIRouter
from entrypoints.sale import router as asd
router = APIRouter(prefix='/v1')
router.include_router(asd)
