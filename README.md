# start vertual envirounment
    source venv/bin/activate

# start uvicorn server
    uvicorn src.app.main:app --reload

# install dependancies
    pip install -r requirements.txt

# List all available commands
    python -m cli.main --help

# Set EV 
    export GCP_PROJECT_ID="supersecretpassword" SPANNER_INSTANCE_ID="supersecretpassword" SPANNER_DATABASE_ID="supersecretpassword"


