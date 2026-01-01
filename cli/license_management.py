import typer
from src.app.data_accuracy_testing_module.license_management_module.\
aggregration_level_validation import service

app = typer.Typer()

@app.command("test-lmt")
def test_license_management_table():
    typer.echo("Start testing license_management_table...")
    service.test_license_management_table()
    typer.echo("Completed testing license_management_table.")