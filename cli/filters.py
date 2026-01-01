import typer
from src.app.data_accuracy_testing_module.filters_module.\
aggregration_level_validation import service

app = typer.Typer()

@app.command("test-suc-filters")
def test_suc_filters():
    typer.echo("Start testing suc filters...")
    service.test_suc_filters()
    typer.echo("Completed testing suc filters.")


@app.command("test-aof-filters")
def test_application_overview_filters():
    typer.echo("Start testing application overview filters...")
    service.test_application_overview_filters()
    typer.echo("Completed testing application overview filters.")

@app.command("test-sof-filters")
def test_school_overview_filters():
    typer.echo("Start testing school overview filters...")
    service.test_school_overview_filters()
    typer.echo("Completed testing school overview filters.")


@app.command("test-lmf-filters")
def test_license_management_filters():
    typer.echo("Start testing license management filters...")
    service.test_license_management_filters()
    typer.echo("Completed testing license management filters.")

@app.command("test-pmf-filters")
def test_permission_management_filters():
    typer.echo("Start testing permission management filters...")
    service.test_permission_management_filters()
    typer.echo("Completed testing permission management filters.")