from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os

load_dotenv()

api_key = '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'


def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(
        model='gpt-4o',
        api_key= api_key
    )

    return openai_model_client