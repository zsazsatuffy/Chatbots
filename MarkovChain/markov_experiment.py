#!/usr/bin/env python

import markovify

with open("pulpfiction_dialog.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(5):
    print(text_model.make_sentence())
