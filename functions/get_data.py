import os
import json
import Levenshtein
from services.AzureOpenAI import get_response_from_aoai
from services.AzureAIDocIntel import get_response_from_docintel

def get_data(target_file_path):

    # getting conten from doc intel
    docintel_resp = get_response_from_docintel(target_file_path)
    content = docintel_resp["content"]
    aoai_resp = get_response_from_aoai(content)

    if aoai_resp is None:
        print("Unable to get response from OpenAI")
        return None

    aoai_resp_json = json.loads(aoai_resp)
    print(aoai_resp_json)
    return aoai_resp_json

def get_test_data(file_path):
    """
    This function is responsible for getting the test data as a json
    """
    return {}