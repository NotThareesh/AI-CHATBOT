import csv
import torch
from sentence_transformers import SentenceTransformer, util
import openai
from .models import *
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"


def chatGPT(query: str):
    openai.api_key = "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"

    prompt = f"Search the web for information about '{query}' and provide a concise answer and address the user as a human would and remove any greetings at the beginning in a maximum of 80-100 words :\n"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200
        )

    except Exception:
        return "Some Error Occured"

    return response.choices[0].text.strip()


# def getData(request):
#     data = []
#     content = PromptData.objects.filter(username=request.user.id)

#     for item in content:
#         data.append(item)
#         print(item)

#     return data

# Custom Model


model = SentenceTransformer("all-MiniLM-L6-v2")


def data_generator():
    file = open('data.csv', mode='r', newline='\n')
    reader = csv.reader(file, delimiter=',')
    next(reader)

    for contents in reader:
        yield tuple(contents)

    file.close()


def find_similarity(prompt: str):
    all_matches = []
    embeddings1 = model.encode(prompt, convert_to_tensor=True)

    for data in tuple(data_generator()):
        embeddings2 = model.encode(data[1], convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(embeddings1, embeddings2)

        # If average similarity ever goes less than 10%, then break
        if torch.lt(similarity, torch.tensor([[0.01]])):
            continue

        # If data matches very closely in the first go then return
        if torch.gt(similarity, torch.tensor([[0.35]])):
            all_matches.append([similarity, data[2]])

    if len(all_matches) > 1:
        final = [torch.tensor([[0.0]]), '']

        for item in all_matches:
            if torch.gt(item[0], final[0]):
                final = [item[0], item[1]]

        return [final]

    return all_matches
