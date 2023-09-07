import csv
from sentence_transformers import SentenceTransformer, util
import time
import torch

start1 = time.time()


def data_generator():
    file = open('data.csv', mode='r', newline='\n')
    reader = csv.reader(file, delimiter=',')
    next(reader)

    for contents in reader:
        yield tuple(contents)

    file.close()


def find_similarity(prompt):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings1 = model.encode(prompt, convert_to_tensor=True)

    for data in tuple(data_generator()):
        total_similarity = 0

        embeddings2 = model.encode(data[1], convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(embeddings1, embeddings2)
        total_similarity += similarity

        # If data matches very closely in the first go then return
        if torch.gt(total_similarity, torch.tensor([[0.35]])):
            return data[2]

        # If average similarity ever goes -ve, then break
        if torch.lt(total_similarity, torch.tensor([[0.05]])):
            continue

    return "No Data Matched"


end1 = time.time()

# Time taken for finding similarity
start2 = time.time()
print(find_similarity("Water is important"))
end2 = time.time()

print("To read data", end1 - start1)
print("To run the function", end2 - start2)
