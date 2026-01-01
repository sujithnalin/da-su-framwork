import typer
from src.app.data_accuracy_testing_module.school_overview_module.\
aggregration_level_validation import service

app = typer.Typer()

@app.command("test-soc")
def test_school_overview_cards():
    typer.echo("Start testing school_overview_cards...")
    service.test_school_overview_cards()
    typer.echo("Completed testing school_overview_cards.")

@app.command("test-sot")
def test_school_overview_table():
    typer.echo("Start testing school_overview_table...")
    service.test_school_overview_table()
    typer.echo("Completed testing school_overview_table.")

@app.command("test-soi")
def test_school_overview_info():
    typer.echo("Start testing school_overview_info...")
    service.test_school_overview_info()
    typer.echo("Completed testing school_overview_info.")
