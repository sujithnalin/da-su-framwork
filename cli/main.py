import typer
from cli import application_overview, compliance, group_management, license_management,\
permission_management, school_overview, spending, usage, filters

app = typer.Typer(help="Management commands")

app.add_typer(application_overview.app, name="application-overview")
app.add_typer(compliance.app, name="compliance")
app.add_typer(group_management.app, name="group-management")
app.add_typer(license_management.app, name="license-management")
app.add_typer(permission_management.app, name="permission-management")
app.add_typer(school_overview.app, name="school-overview")
app.add_typer(spending.app, name="spending")
app.add_typer(usage.app, name="usage")
app.add_typer(filters.app, name="filters")

if __name__ == "__main__":
    app()
