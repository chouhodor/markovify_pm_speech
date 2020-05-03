import os
import sys
import markovify

with open(os.path.join(sys.path[0], "corpus.txt"), "r", encoding='utf8') as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)


print(text_model.make_short_sentence(280))



"""
Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())
"""
"""
# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(280))
"""


