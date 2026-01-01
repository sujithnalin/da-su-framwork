from .dbs.spanner import spanner as spanner_db
from .dbs.bq import bq as bq_db

def test_null_values():
    print("Testing for null from the DB...") 
    spanner_db.get_data()
    print("Test completed.")

def test_bq_values():
    print("Testing for null from the DB...") 
    bq_db.get_data()
    print("Test completed.")

