import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from pprint import pprint

_ = load_dotenv(find_dotenv())

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model=model, messages=messages, temperature=temperature
    )

    # pprint(response, width=2)
    return response.choices[0].message.content


def get_completion_from_messages(messages, model="gpt-3.6-turbo", temperature=0):
    response = client.chat.completions.create(
        model=model, messages=messages, temperature=temperature
    )
    return response.choices[0].message.content


prompt = "What is the capital of New York?"
get_completion(prompt)


# messages = [{"role": "user", "content": "What is the capital of New York?"}]
# try:
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo", messages=messages, temperature=0
#     )

#     print(response.choices[0].message.content)
# except Exception as e:
#     print(e)
