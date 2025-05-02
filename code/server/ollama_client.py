import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"  # Default Ollama API endpoint

def generate_response(prompt, model="deepseek-r1:1.5b"):
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}

    try:
        print(prompt)
        # return "UES"
        response = requests.post(url, json=data, headers=headers)
        print(response.json())  # Prints the response
        
        return response.json()['response']
    except requests.exceptions.RequestException as e:
        print(f"Error calling Ollama API: {e}")
        return None

# import requests

