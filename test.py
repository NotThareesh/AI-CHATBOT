import csv
from sentence_transformers import SentenceTransformer, util
import time
import torch

start = time.time()

model = SentenceTransformer("all-MiniLM-L6-v2")


def data_generator():
    file = open('data.csv', mode='r', newline='\n')
    reader = csv.reader(file, delimiter=',')
    next(reader)

    for contents in reader:
        yield tuple(contents)

    file.close()


def find_similarity(prompt):
    embeddings1 = model.encode(prompt, convert_to_tensor=True)

    for data in tuple(data_generator()):
        embeddings2 = model.encode(data[1], convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(embeddings1, embeddings2)

        # If average similarity ever goes less than 10%, then break
        if torch.lt(similarity, torch.tensor([[0.01]])):
            continue

        # If data matches very closely in the first go then return
        if torch.gt(similarity, torch.tensor([[0.35]])):
            return data[2]

    return "No Data Matched"


print(find_similarity("Water is important"))
end = time.time()

print("Total time", end - start)
