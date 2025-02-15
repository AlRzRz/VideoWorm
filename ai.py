from openai import OpenAI
from dotenv import load_dotenv
import os
import prompts


def analyzer(transcript: str) -> str:
  
  load_dotenv()
  secretKey = os.getenv('SECRETKEY')
  client = OpenAI(api_key=secretKey)

  completion = client.chat.completions.create(
    model='gpt-4o',
    messages=[
      {'role': 'developer', 'content': prompts.systemPrompt},
      {'role': 'user', 'content': prompts.userPrompt(transcript=transcript)}
    ]
  )

  # print(completion.choices[0].message.content)

  return completion.choices[0].message.content


# Test:
# analyzer(prompts.placeholderText)
  