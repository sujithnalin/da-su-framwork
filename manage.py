import typer
from scripts.migrate import run_spanner, run_bigquery
from src.app.data_completeness_testing_module import service
from src.app.data_accuracy_testing_module.application_overview_module.\
aggregration_level_validation import service as apservice

app = typer.Typer()
    

if __name__ == "__main__":
    app()
