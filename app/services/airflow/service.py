from typing import Dict, Optional

from app.core.config import settings
from app.services.airflow.client import AirflowClient

class DataCloneService:
    def __init__(self, client: AirflowClient):
        self.client = client
        self.dag_id = settings.DATA_CLONE_DAG_ID

    async def trigger_data_clone(
        self,
        source: str,
        target: str,
        options: Optional[Dict] = None,
    ) -> Dict:
        conf = {
            "source": source,
            "target": target,
            "options": options or {},
        }
        return await self.client.trigger_dag_run(
            dag_id=self.dag_id,
            conf=conf,
        )

    async def get_data_clone_status(
        self,
        run_id: str,
    ) -> Dict:
        return await self.client.get_dag_run(
            dag_id=self.dag_id,
            dag_run_id=run_id,
        )
