from google.cloud import bigquery

def get_bigquery_client() -> bigquery.Client:
    return bigquery.Client()