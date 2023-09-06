from sentence_transformers import SentenceTransformer, util
import time
import torch

start1 = time.time()

model = SentenceTransformer("all-MiniLM-L6-v2")

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
        "How would you define the concept of evolution in biology?",
        "What does the theory of evolution seek to explain?",
        "Can you explain the mechanism of natural selection in evolution?",
        "Why is genetic variation important in the process of evolution?",
        "What role do mutations play in the evolutionary process?",
        "How does adaptation relate to the theory of evolution?",
        "What are some key pieces of evidence supporting the theory of evolution?",
        "Who is Charles Darwin, and what is his contribution to our understanding of evolution?",
        "What is speciation, and how does it occur in the context of evolution?",
        "How does evolution contribute to the diversity of life on Earth?",
        "Can you provide examples of evolution occurring in the natural world?",
        "How do fossils provide insights into the history of evolution?",
        "What is convergent evolution, and can you give examples?",
        "How does environmental change influence the process of evolution?",
        "What is the difference between microevolution and macroevolution?",
        "What are some common misconceptions about the theory of evolution?",
        "How does comparative anatomy help us understand evolutionary relationships?",
        "What is the significance of the fossil record in the study of evolution?",
        "How do scientists use molecular biology techniques to investigate evolutionary history?",
        "What are the ethical implications of understanding evolution for human society?"
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

    (
        "What harm can microorganisms cause to human health?",
        "How do microorganisms contribute to the spread of infectious diseases?",
        "What is the impact of bacteria on food spoilage?",
        "Can microorganisms contaminate drinking water sources?",
        "What role do viruses play in causing illnesses?",
        "How can fungi negatively affect crops and agricultural production?",
        "Do microorganisms contribute to environmental pollution?",
        "Are there microorganisms that harm aquatic ecosystems?",
        "What are the consequences of microbial biofouling in industries?",
        "How do pathogens develop antibiotic resistance?",
        "What is the role of microorganisms in dental decay?",
        "Can microorganisms lead to the deterioration of historic artifacts?",
        "How do microorganisms contribute to foul odors in waste management?",
        "What negative effects can microbes have on the quality of indoor air?",
        "Are there microorganisms that damage building materials and infrastructure?",
        "What is the connection between microorganisms and respiratory infections?",
        "Do microorganisms play a role in allergic reactions and asthma?",
        "How can microbial contamination impact pharmaceutical and medical devices?",
        "What is the role of microorganisms in soil degradation?",
        "Can microorganisms harm wildlife and ecosystems?"
    )
)

prompt = "Meaning of life?"

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

            # print(sentence[2:15], total_similarity/count)

            if count >= 10 and torch.gt(total_similarity/count, torch.tensor([[0.40]])):
                break

            if torch.gt(total_similarity/count, torch.tensor([[0.50]])):
                return "Data Matched"

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
