import typer
from src.app.data_accuracy_testing_module.group_management_module.\
aggregration_level_validation import service

app = typer.Typer()

@app.command("test-gmt")
def test_group_management_table():
    typer.echo("Start testing group_management_table...")
    service.test_group_management_table()
    typer.echo("Completed testing group_management_table.")