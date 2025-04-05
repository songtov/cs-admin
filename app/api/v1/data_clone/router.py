from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.data_clone.schemas import (
    DataCloneRequest,
    DataCloneResponse,
    DataCloneStatus,
)
from app.services.airflow.client import AirflowClient
from app.services.airflow.service import DataCloneService

router = APIRouter(
    prefix="/data-clone",
    tags=["data-clone"],
    responses={404: {"description": "Not found"}},
)

def get_data_clone_service() -> DataCloneService:
    client = AirflowClient()
    return DataCloneService(client)

@router.post("/trigger", response_model=DataCloneResponse)
async def trigger_data_clone(
    request: DataCloneRequest,
    service: DataCloneService = Depends(get_data_clone_service),
) -> DataCloneResponse:
    response = await service.trigger_data_clone(
        source=request.source,
        target=request.target,
        options=request.options.dict() if request.options else None,
    )
    return DataCloneResponse(
        run_id=response["dag_run_id"],
        status=DataCloneStatus(response["state"]),
        conf=response["conf"],
        start_date=response.get("start_date"),
    )

@router.get("/status/{run_id}", response_model=DataCloneResponse)
async def get_data_clone_status(
    run_id: str,
    service: DataCloneService = Depends(get_data_clone_service),
) -> DataCloneResponse:
    response = await service.get_data_clone_status(run_id)
    return DataCloneResponse(
        run_id=response["dag_run_id"],
        status=DataCloneStatus(response["state"]),
        conf=response["conf"],
        start_date=response.get("start_date"),
        end_date=response.get("end_date"),
    )
