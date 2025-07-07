import os
from dotenv import load_dotenv

from pymilvus import MilvusClient, DataType, Function, FunctionType


load_dotenv("config/.env")


def create_hybrid_collections():
    client = MilvusClient(
        uri=os.getenv("ZILLIZ_CLUSTER_PUBLIC_ENDPOINT"),
        token=os.getenv("ZILLIZ_CLUSTER_TOKEN"),
    )

    # create schema
    schema = MilvusClient.create_schema(
        enable_dynamic_fields=True, description="Podedex Data"
    )

    # now we can add fields to the schema
    # id field
    schema.add_field(
        field_name="Auto_id",
        datatype=DataType.INT64,
    )
