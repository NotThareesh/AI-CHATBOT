import csv
from sentence_transformers import SentenceTransformer, util
import time
import torch

start1 = time.time()

model = SentenceTransformer("all-MiniLM-L6-v2")

file = open('data.csv', mode='r', newline='\n')
reader = csv.reader(file, delimiter=',')
next(reader)

prompt = "Harms of microorganisms"

embeddings1 = model.encode(prompt, convert_to_tensor=True)


def data_generator():
    for contents in reader:
        yield tuple(contents)


def find_similarity():
    for data in tuple(data_generator()):
        count = 0
        total_similarity = 0

        content = data[1].split('\t')

        for sentence in content:
            count += 1
            embeddings2 = model.encode(sentence, convert_to_tensor=True)
            similarity = util.pytorch_cos_sim(embeddings1, embeddings2)
            total_similarity += similarity

            if count >= 10 and torch.gt(total_similarity/count, torch.tensor([[0.40]])):
                break

            if torch.gt(total_similarity/count, torch.tensor([[0.50]])):
                return ("Data Matched", data[2])

            if torch.lt(total_similarity/count, torch.tensor([[0.0]])):
                break

    return "No Data Matched"


end1 = time.time()

# Time for running function
start2 = time.time()
print(find_similarity())
end2 = time.time()

print("To read data", end1 - start1)
print("To run the function", end2 - start2)
