import os
import requests


def get_llm_response(message: str) -> str:
    headers = {
        'Authorization': f'Bearer {os.getenv("OPENAI_TOKEN")}',
        'Content-Type': 'application/json',
    }

    payload = {
        'model': 'gpt-4o-mini',
        "messages": [
            {
                "role": "user",
                "content": message,
            }
        ],
        "temperature": 0.7,
        "store": True,
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)

    if response.status_code == 200:
        choices = response.json().get("choices", [])
        if choices:
            return choices[0]["message"]["content"]
        else:
            raise Exception("No choices found in OpenAI response.")
    else:
        raise Exception(response.text)
