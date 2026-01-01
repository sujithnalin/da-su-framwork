from google.cloud import spanner
from src.core.config import settings

_spanner_client = None
_database = None

def get_spanner_database():
    global _spanner_client, _database

    if not _database:
        _spanner_client = spanner.Client(
            project=settings.GCP_PROJECT_ID
        )
        instance = _spanner_client.instance(
            settings.SPANNER_INSTANCE_ID
        )
        _database = instance.database(
            settings.SPANNER_DATABASE_ID
        )

    return _database
