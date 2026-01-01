import typer
from src.app.data_accuracy_testing_module.spending_module.\
aggregration_level_validation import service

app = typer.Typer()

@app.command("test-spt")
def test_spending_table():  
    typer.echo("Start testing spending_table...")
    service.test_spending_table()
    typer.echo("Completed testing spending_table.")

    
@app.command("test-spc")
def test_spending_cards():
    typer.echo("Start testing spending_cards...")
    service.test_spending_cards()
    typer.echo("Completed testing spending_cards.") 

