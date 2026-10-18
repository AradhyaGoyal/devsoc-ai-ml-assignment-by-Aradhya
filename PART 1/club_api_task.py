import requests
import json

def read_prompt_file(file_name):
    with open(file_name, 'r') as file:
        my_text = file.read()
        return my_text

def call_gemini_api(prompt_text):

    #removed the api key since its not safe to make it public you can input it below
    api_key = "api_key_put_here_please"
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"
    
    api_data = {
        "contents": [{
            "parts": [{"text": prompt_text}]
        }]
    }
    
    api_headers = {"Content-Type": "application/json"}


    response = requests.post(api_url, headers=api_headers, json=api_data)

    return response.json()

def save_to_json(ai_data, output_file_name):
    with open(output_file_name, 'w') as json_file:
        json.dump(ai_data, json_file, indent=4)

input_file = "text.txt"
output_file = "ai_answers.json"

print("1. Getting text from file...")
user_prompt = read_prompt_file(input_file)

print("2. Sending to AI ...")
result_data = call_gemini_api(user_prompt)

print("3. Saving to JSON file...")
save_to_json(result_data, output_file)

print(f"All done! Check your folder for {output_file}")