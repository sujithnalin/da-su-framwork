import typer
from src.app.data_accuracy_testing_module.application_overview_module.\
aggregration_level_validation import service

app = typer.Typer()

@app.command("test-aoc")
def test_application_overview_cards():
    typer.echo("Start testing application_overview_cards...")
    service.test_application_overview_cards()
    typer.echo("Completed testing application_overview_cards.")

@app.command("test-aoubst")
def test_application_overview_ubs_table():
    typer.echo("Start testing application_overview_ubs_table...")
    service.test_application_overview_ubs_table()
    typer.echo("Completed testing application_overview_ubs_table.")

@app.command("test-aoluc")
def test_application_overview_lu_charts():
    typer.echo("Start testing application_overview_lu_charts...")
    service.test_application_overview_lu_charts()
    typer.echo("Completed testing application_overview_lu_charts.")

@app.command("test-aoaduc")
def test_application_overview_adu_charts():
    typer.echo("Start testing application_overview_adu_charts...")
    service.test_application_overview_adu_charts()
    typer.echo("Completed testing application_overview_adu_charts.")

@app.command("test-aoi")
def test_application_overview_info():
    typer.echo("Start testing application_overview_info...")
    service.test_application_overview_info()
    typer.echo("Completed testing application_overview_info.")