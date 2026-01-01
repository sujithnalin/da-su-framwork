# Create a vertual env
    python3.11 -m venv venv

# start vertual envirounment
    source venv/bin/activate

# install dependancies
    pip install -r requirements.txt

# start uvicorn server
    uvicorn src.app.main:app --reload

# List all available commands
    python -m cli.main --help

# Set EVN variables
    export GCP_PROJECT_ID="supersecretpassword" SPANNER_INSTANCE_ID="supersecretpassword" SPANNER_DATABASE_ID="supersecretpassword"

# docker build
    docker build --no-cache -t da-su-framwork:latest .

# docker run 
    docker run -p 8080:8080 da-su-framwork:latest

# Open a shell inside the container 
    docker exec -it <container_id> /bin/bash



