from sentence_transformers import SentenceTransformer, util
import time
import torch

start1 = time.time()

model = SentenceTransformer("bert-base-uncased")

list1 = (
    (
        'What is DNA?',
        'What is the genetic material of most living organisms?',
        'What is the molecular basis of heredity?',
        'What is the fundamental molecule that stores genetic information?',
        'What is the primary carrier of genetic instructions in cells?',
        'What is the code that governs the characteristics of an organism?',
        'What is the biological molecule that resembles a twisted ladder?',
        'What is the chemical compound responsible for inheritance?',
        'What is the molecule that contains the instructions for life?',
        'What is the molecule that passes traits from parents to offspring?',
        'What is the long, thread-like molecule found in cell nuclei?',
        'What is the molecule that carries the genetic code?',
        'What is the basis for the diversity of life on Earth?',
        'What is the molecule that determines our unique traits?',
        'What is the informational molecule of life?',
        'What is the molecule that enables species to evolve?',
        'What is the core molecule of genetics?'
    ),

    (
        'What is the environment and why is it important?',
        'How does human activity impact the environment?',
        'What are greenhouse gases, and how do they contribute to climate change?',
        'What is the greenhouse effect, and why is it a concern?',
        'What are some of the major consequences of global warming?',
        'How does deforestation affect the environment?',
        'What is biodiversity, and why is it essential for the environment?',
        'How do pollution and contaminants harm ecosystems and human health?',
        'What is the role of renewable energy sources in protecting the environment?',
        'What are the challenges and benefits of transitioning to a sustainable, green economy?',
        'How do ocean acidification and plastic pollution affect marine environments?',
        'What are the primary causes and consequences of air pollution?',
        'What are the key principles of sustainable agriculture, and why are they important?',
        'How does overfishing impact aquatic ecosystems and global food security?',
        'What are the effects of habitat destruction on wildlife populations?',
        'What is the concept of the circular economy, and how does it promote sustainability?',
        'How can individuals reduce their carbon footprint and contribute to a healthier environment?',
        'What are the implications of water scarcity and contamination for communities and ecosystems?',
        'How does climate change disproportionately affect vulnerable populations?',
        'What international agreements and initiatives are aimed at addressing environmental issues on a global scale?'
    ),

    (
        'What is a skeleton?',
        'What is the main purpose of a skeleton?'
        'Is a skeleton found only in humans?'
        'How does a skeleton help support the body?'
        'What are the parts of a skeleton called?'
        'Are bones a part of the skeleton?'
        'Can you name some animals with skeletons?'
        'What does a skeleton do for animals?'
        'How does a skeleton protect vital organs?'
        'What does a skeleton feel like when you touch it?'
        'How do skeletons help animals move?'
        'Can you see a skeleton in your body?'
        'What is the difference between an exoskeleton and an endoskeleton?'
        'Why do some animals, like insects, have exoskeletons?'
        'What happens if a bone in your skeleton breaks?'
        'How many bones are there in a human skeleton?'
        'Do all animals have the same number of bones in their skeletons?'
        'Are teeth considered part of the skeleton?'
        'What materials are skeletons made of?'
        'Can you name some functions of the human skeleton?'
    ),
)


prompt = ""

embeddings1 = model.encode(prompt, convert_to_tensor=True)

def find_similarity():
    for questions in list1:
        count = 0
        total_similarity = 0

        for sentence in questions: 
            count += 1
            embeddings2 = model.encode(sentence, convert_to_tensor=True)
            similarity = util.pytorch_cos_sim(embeddings1, embeddings2)
            total_similarity += similarity

            print(sentence[2:15], total_similarity/count)

            if count >= 10 and torch.gt(total_similarity/count, torch.tensor([[0.40]])):
                break

            if torch.gt(total_similarity/count, torch.tensor([[0.50]])):
                return "Data Matched"
            
            if torch.lt(total_similarity/count, torch.tensor([[0.0]])):
                break
        
        print('='*50)
            
    return "No Data Matched"

end1 = time.time()

# Time for running function
start2 = time.time()
print(find_similarity())
end2 = time.time()

print("To read data", end1 - start1)
print("To run the function", end2 - start2)
