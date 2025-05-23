from fastapi import APIRouter
from fastapi.params import Depends
from src.app.infrastructure.config import config
from src.app.domain.schemas import DetailLegoId, DetailName
from src.app.infrastructure.dependencies import SearchServiceDep

router = APIRouter(prefix=config.search_router_config.prefix, tags=config.search_router_config.tags)


@router.get(
    "/get-detail-by-lego-id",
    summary=config.search_router_config.docs[1]["summary"],
    description=config.search_router_config.docs[1]["description"]
)
def get_detail_by_lego_id(service: SearchServiceDep, schema: DetailLegoId = Depends()):
    return service.get_detail_by_lego_id(schema)


@router.get(
    "/get-detail-by-name",
    summary=config.search_router_config.docs[2]["summary"],
    description=config.search_router_config.docs[2]["description"]
)
def get_detail_by_name( service: SearchServiceDep, schema: DetailName = Depends()):
    return service.get_detail_by_name(schema)
