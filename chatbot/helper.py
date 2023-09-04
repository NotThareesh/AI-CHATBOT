import openai
# from gpt4all import GPT4All
# from pathlib import Path
# import gpt4all.gpt4all
# from transformers import AutoModelForCausalLM
# from transformers import AutoTokenizer, pipeline

# def newFunc():
#   model = AutoModelForCausalLM.from_pretrained("nomic-ai/gpt4all-falcon", trust_remote_code=True)

#   tokenizer = AutoTokenizer.from_pretrained('nomic-ai/gpt4all-falcon', use_fast=False)
#   model.to("cuda:0")

#   prompt = "Describe a painting of a falcon in a very detailed way." # Change this to your prompt
#   prompt_template = f"### Instruction: {prompt}\n### Response:"

#   tokens = tokenizer(prompt_template, return_tensors="pt").input_ids.to("cuda:0")
#   output = model.generate(input_ids=tokens, max_new_tokens=256, do_sample=True, temperature=0.8)
#   print(tokenizer.decode(output[0]))

def cleanLocalGPT(data: str):
    clean_text = data.rfind('.', 1)[0] + '.'

    return clean_text


def chatGPT(query: str):
  openai.api_key = "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"

  prompt = f"Search the web for information about '{query}' and provide a concise answer and address the user as a human would and remove any greetings at the beginning in a maximum of 120-150 words :\n"
  
  try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )

  except Exception as e:
     print(e)
     return "Some Error Occured"

  return response.choices[0].text.strip()
