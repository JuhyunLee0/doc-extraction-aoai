import os
import json
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
from openai import AzureOpenAI

azure_openai_ep = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_key = os.getenv("AZURE_OPENAI_KEY")
azure_openai_model = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
azure_openai_api_version = "2023-05-15"

client = AzureOpenAI(
    api_key=azure_openai_key,
    api_version=azure_openai_api_version,
    azure_endpoint=azure_openai_ep
)

def get_response_from_aoai(document_content: str):
    """Get a JSON response from the GPT-4o model with schema"""

    system_prompt_file = os.path.join(os.getcwd(), "local", "system_prompt-modified.txt")
    with open(system_prompt_file, "r") as f:
        system_prompt = f.read()

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": document_content}
        ]

        try:
            response = client.chat.completions.create(
                model=azure_openai_model, # The deployment name you chose when you deploy GPT model
                messages=messages,
                response_format={ "type": "json_object" },
            )
            response_message = response.choices[0].message
            return response_message.content
        except Exception as e:
            print(f"Error: {e}")
            return None