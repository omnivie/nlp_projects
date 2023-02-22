import spacy

nlp = spacy.load('en_core_web_md')


word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# It i interesting that monkey and banana is close in similarity to cat and monkey
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# It is another interesting example and surprisingly similarity of man to fish is higher than child to fish
item1 = nlp("man")
item2 = nlp("child")
item3 = nlp("fish")

print(item1.similarity(item2))
print(item3.similarity(item2))
print(item3.similarity(item1))


# As per the task
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Another set of interesting comparisons. Guess what? Cat is more similar to chocolate (0.23) than man to chocolate (0.09)
words = nlp('cat chocolate monkey man banana ')
for word1 in words:
    for word2 in words:
        print(word1.text, word2.text, word1.similarity(word2))


# As per the task
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
            "Hello, there is my car",
            "I\'ve lost my car in my car",
            "I\'d like my boat back",
            "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


