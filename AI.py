import os
import os.path
import sys 
from langchain_openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,StorageContext,load_index_from_storage
import logging

# llm = OpenAI() not using OPENAI

text = sys.argv[1]

Persist_Dir = "./storage"

if not os.path.exists(Persist_Dir):

    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)

    index.storage_context.persist(persist_dir=Persist_Dir)
else:

    storage_context = StorageContext.from_defaults(persist_dir=Persist_Dir)
    index = load_index_from_storage(storage_context)





query_engine = index.as_query_engine()

response = query_engine.query(text)


index.storage_context.persist()

# response = llm.invoke(text) Not Using OPENAI

print(response)
