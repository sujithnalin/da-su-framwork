from .dbs.spanner import spanner as spanner_db
from .dbs.bq import bq as bq_db

# def test_null_values():
#     print("Testing for null from the DB...") 
#     spanner_db.get_data()
#     print("Test completed.")

# def test_bq_values():
#     print("Testing for null from the DB...") 
#     bq_db.get_data()
#     print("Test completed.")

def test_suc_filters()  :
    """"Test Spending, Usage & Compliance (SUC) filters from the DB"""
    print("Testing for SUC filter from the DB...") 
    # TODO: spanner_db.get_data()
    print("Test completed.")

def test_application_overview_filters()  :
    """"Test Application Overview filters from the DB"""
    print("Testing for Application Overview filter from the DB...")
    # TODO: implement the logic to test application overview filters
    print("Test completed.")    

def test_school_overview_filters()  :
    """"Test School Overview filters from the DB"""
    print("Testing for School Overview filter from the DB...")
    # TODO: implement the logic to test school overview filters
    print("Test completed.")


def test_license_management_filters()  :
    """"Test License Management filters from the DB"""
    print("Testing for License Management filter from the DB...")
    # TODO: implement the logic to test license management filters
    print("Test completed.")

def test_permission_management_filters()  :
    """"Test Permission Management filters from the DB"""
    print("Testing for Permission Management filter from the DB...")
    # TODO: implement the logic to test permission management filters
    print("Test completed.")

    


