import os 
import sys 
from langchain.document_loaders import TextLoader 
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

import  constants

# os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY

print("hello")

loader = TextLoader('fastapi.txt')

# change to data.txt to add numbers in sequence 
# uncomment this line 
# loader = TextLoader('data.txt')

# loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

query = sys.argv[1]
# print(index.query(query))
# merge llm and customized data 
print(index.query(query, llm=ChatOpenAI()))

# openai api data usage policies  
# starting on march 1, 2023, 
# 1 not use submitted data to train or improve our own models, customer can opt-in to share 
# 2 any data through api will be retain for max 30 days for abuse and monitoring purposes, then deleted 

# azure openai service, advanced language models 
