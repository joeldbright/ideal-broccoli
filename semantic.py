
# Start

import spacy

nlp = spacy.load('en_core_web_md') # using en_core_web_sm adds a lot of warning messages about word vectors

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("")
print(word1.similarity(word2)) # cat and monkey are the most similar most likely because they are both animals
print(word3.similarity(word2)) # banana and monkey are quite similar probably to do with that monkeys famously eat bananas
print(word3.similarity(word1)) # banana and cat have the least similarity as they dont share anything in common really
print("")

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print("")

sentence_to_compare = "Why is my cat on the car"

sentences = [
    "Where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"
]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
print("")

# Stop
