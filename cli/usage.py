import typer
from src.app.data_accuracy_testing_module.usage_module.\
aggregration_level_validation import service

app = typer.Typer()

@app.command("test-uc")
def test_usage_cards():
    typer.echo("Start testing usage_cards...")
    service.test_usage_cards()
    typer.echo("Completed testing usage_cards.")

@app.command("test-uc")
def test_usage_cards():
    typer.echo("Start testing usage_cards...")
    service.test_usage_cards()
    typer.echo("Completed testing usage_cards.")

