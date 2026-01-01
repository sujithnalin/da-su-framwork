from src.core.spanner import get_spanner_database

def get_data():
    db = get_spanner_database()

    # Execute SELECT query
    with db.snapshot() as snapshot:
        results = snapshot.execute_sql(
            """
            SELECT *
            FROM Users
            limit 10
            # WHERE IsActive = @is_active
            """,
            # params={"is_active": True},
            # param_types={"is_active": spanner.param_types.BOOL},
        )

        for row in results:
            print(
                row[0],   # UserId
                row[1],   # UserName
                row[2],   # CreatedAt
            )
