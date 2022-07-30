"""
You are given a class called Sentence , which takes a string such as 'hello world'. 
You need to provide an interface such that the indexer returns a flyweight 
that can be used to capitalize a particular word in the sentence.

Typical use would be something like:

sentence = Sentence('hello world')
sentence[1].capitalize = True
print(sentence)  # writes "hello WORLD"
"""

from unittest import TestCase


class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split()
        self._capitalized = {}
        super().__init__()

    def __getitem__(self, index):
        if index not in self._capitalized:
            self._capitalized[index] = self.CapitalizedFormat()

        return self._capitalized[index]

    class CapitalizedFormat:
        def __init__(self, capitalize=False) -> None:
            self.capitalize = capitalize

    def __len__(self):
        return len(self.words)

    def __str__(self) -> str:
        new_cap = self.CapitalizedFormat()
        result = []
        for i in range(len(self.words)):
            cap_format = self._capitalized.get(i, new_cap)
            w = self.words[i]
            result.append(w.upper() if cap_format.capitalize else w)

        return " ".join(result)


class Evaluate(TestCase):
    def test_exercise(self):
        s = Sentence('alpha beta gamma')
        s[1].capitalize = True
        self.assertEqual(str(s), 'alpha BETA gamma')


sentence = Sentence('alfa beta gamma')
sentence[1].capitalize = True
sentence[2].capitalize = False
print (0, sentence[0].capitalize)
print (1, sentence[1].capitalize)
print(str(sentence))
