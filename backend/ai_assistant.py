# 1. install ollama https://ollama.com 
# 2. setup ollama, run ollama serve in terminal
# 3.check if the port is available to avoid errors
# 4. make http://localhost:11434/ sure says "ollama is running"

import sys
from langchain_ollama import ChatOllama
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# get user question passed from Node.js
user_question = sys.argv[1]

model = ChatOllama(model="llama3.2", base_url="http://localhost:11434/")

# needs prompt engineering (excessively)
system_message = SystemMessagePromptTemplate.from_template(
    "You are a helpful AI Assistant. You are in expert in PC components and PC building."
)

prompt = HumanMessagePromptTemplate.from_template(user_question)

# create chat history (for now it's just the system message & the user's input)
# will set it up in mongoDB later
chat_history = [system_message, prompt]

chat_template = ChatPromptTemplate.from_messages(chat_history)

chain = chat_template | model | StrOutputParser()

# llama response
response = chain.invoke({})

print(response)
