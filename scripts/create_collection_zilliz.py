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
        enable_dynamic_field=True, description="Pokedex Data"
    )

    # now we can add fields to the schema
    # id field
    schema.add_field(
        field_name="Auto_id",
        datatype=DataType.INT64,
        description="Primary Key",
        is_primary=True,
        auto_id=True,
    )

    # vector for embedding search -> this will be produced by a embedding model: i'm gonna store this as well
    schema.add_field(
        field_name="vector",
        datatype=DataType.FLOAT_VECTOR,
        dim=768,  # output dimension of the embeddings generation model, in this case it would be google's embedding model -> gemini-embedding-001
    )

    # meta-data search
    schema.add_field(field_name="metadata", datatype=DataType.JSON)

    # text search
    schema.add_field(
        field_name="text",
        datatype=DataType.VARCHAR,
        max_length=1000,
        enable_analyzer=True,
    )

    # for saprse vectors
    schema.add_field(field_name="sparse", datatype=DataType.SPARSE_FLOAT_VECTOR)

    # function to generate sparse vector from text -> it's using bm25 algorithm: Best Matching 25
    bm25_func = Function(
        name="text_bm25_emb",
        input_field_names=["text"],
        output_field_names=["sparse"],
        function_type=FunctionType.BM25,
    )
    schema.add_function(bm25_func)

    # prepare index parameters
    index_params = client.prepare_index_params()

    # add vector index
    index_params.add_index(
        field_name="vector", metric_type="COSINE", index_type="AUTOINDEX"
    )

    # add sparse index
    index_params.add_index(
        field_name="sparse", metric_type="BM25", index_type="AUTOINDEX"
    )

    # create collection
    client.create_collection(
        collection_name="pokedex", schema=schema, index_params=index_params
    )
    
# call the func to create the collection in zilliz
create_hybrid_collections()
