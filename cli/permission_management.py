import typer
from src.app.data_accuracy_testing_module.permission_management_module.\
aggregration_level_validation import service

app = typer.Typer()

@app.command("test-pmt")
def test_permission_management_table():
    typer.echo("Start testing permission_management_table...")
    service.test_permission_management_table()
    typer.echo("Completed testing permission_management_table.")