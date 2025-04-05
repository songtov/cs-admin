import base64
from typing import Any, Dict, Optional

import httpx
from fastapi import HTTPException

from app.core.config import settings

class AirflowClient:
    def __init__(self):
        self.base_url = settings.AIRFLOW_API_URL.rstrip("/")
        self.auth = base64.b64encode(
            f"{settings.AIRFLOW_USERNAME}:{settings.AIRFLOW_PASSWORD}".encode()
        ).decode()
        self.headers = {
            "Authorization": f"Basic {self.auth}",
            "Content-Type": "application/json",
        }

    async def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}/api/v1/{endpoint}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=self.headers,
                    json=data,
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as e:
                raise HTTPException(
                    status_code=e.response.status_code if hasattr(e, "response") else 500,
                    detail=f"Airflow API error: {str(e)}",
                )

    async def trigger_dag_run(
        self,
        dag_id: str,
        conf: Dict[str, Any],
    ) -> Dict[str, Any]:
        return await self._request(
            method="POST",
            endpoint=f"dags/{dag_id}/dagRuns",
            data={"conf": conf},
        )

    async def get_dag_run(
        self,
        dag_id: str,
        dag_run_id: str,
    ) -> Dict[str, Any]:
        return await self._request(
            method="GET",
            endpoint=f"dags/{dag_id}/dagRuns/{dag_run_id}",
        )
