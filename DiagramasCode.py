from diagrams import Cluster, Diagram
from diagrams.gcp.analytics import BigQuery, Dataflow
from diagrams.gcp.compute import AppEngine, Functions
from diagrams.gcp.storage import GCS
from diagrams.custom import Custom
from diagrams.onprem.database import Postgresql
from diagrams.gcp.analytics import Dataproc
from diagrams.gcp.analytics import Composer
from diagrams.onprem.analytics import Powerbi

with Diagram("Data Pipeline Example using Diagram as Code", show=False):

    with Cluster("Source of Data"):
        postgresql = Postgresql("Database")
        csv = Custom("CSV Files", "./Images/csv.png")
        json = Custom("Json Files", "./Images/json.png")

    with Cluster("Raw Layer"):
        storage = GCS("storage")

    functions = Functions("Trigger Cloud Functions")

    postgresql >> storage
    csv >> storage
    json >> storage
    storage >> functions

    with Cluster("Composer"):
        airflow = Composer("Airflow")

        with Cluster("Transformation Layer"):
            dataflow = Dataflow("Data Flow")
            dataproc = Dataproc("Dataproc Cluster")

        functions >> dataflow
        functions >> dataproc

        with Cluster("Curated Layer"):
            bigquery = BigQuery("Bigquery")

    dataflow >> bigquery

    with Cluster("Presentation Layer"):
        powerbi = Powerbi("Power BI")

    bigquery >> powerbi
