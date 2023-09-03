import openai

def chatAPI(query):
  openai.api_key = "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"

  prompt = f"Search the web for information about '{query}' and provide a concise answer and address the user  as a human would :\n"
  
  try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

  except Exception as e:
     print(e)
     return "Some Error Occured"

  return response.choices[0].text.strip()