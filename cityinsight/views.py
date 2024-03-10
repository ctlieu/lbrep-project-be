from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from langchain.sql_database import SQLDatabase
from langchain.agents import create_sql_agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Create a SQLDatabase instance
db=SQLDatabase.from_uri('postgresql+psycopg2://postgres:sw1tchb0x@localhost/calgary_db')

# create llm
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key, temperature =0)

# Create a SQLDatabaseChain instance
db_chain= create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)


class AskView(View):
    def get(self, request, *args, **kwargs):
        query= request.GET.get('question', None)
        if not query:
            return JsonResponse({"error": "Please provide a question."}, status=400)

        answer = db_chain(query)
        return JsonResponse({'answer':answer})


    def post(self, request, *args, **kwargs):
        query = request.POST.get('question')
        answer = db_chain(query)
        return JsonResponse(answer)



