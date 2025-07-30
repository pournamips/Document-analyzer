# analyzer/utils.py
import requests
import os

def analyze_with_ai(user_text):
    try:
        headers = {
            "Authorization": f"Bearer {os.environ.get('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "system", "content": "You are a legal expert AI. Analyze the legal document text for risky clauses, missing elements, regulatory compliance, and summarize in plain language."},
                {"role": "user", "content": user_text}
            ]
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        data = response.json()

        if 'choices' in data:
            return data['choices'][0]['message']['content']
        else:
            return f"Error: {data.get('error', 'No response from AI')}"
    except Exception as e:
        return f"Exception: {str(e)}"
