import typer
from src.app.data_accuracy_testing_module.compliance_module.\
aggregration_level_validation import service

app = typer.Typer()

@app.command("test-cc")
def test_compliance_cards():
    typer.echo("Start testing compliance_cards...")
    service.test_compliance_cards()
    typer.echo("Completed testing compliance_cards.")

@app.command("test-ct")
def test_compliance_table():
    typer.echo("Start testing compliance_table...")
    service.test_compliance_table()
    typer.echo("Completed testing compliance_table.")