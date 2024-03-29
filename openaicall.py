import os
from openai import OpenAI

### Setting the environment
client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )

### Function definition
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content


### TEsting the OpenAI Calling 

prompt = input("Enter your prompt here: ")

texto = get_completion(prompt)
print(texto)