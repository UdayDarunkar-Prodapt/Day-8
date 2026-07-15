

class TextUtilities:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        words = self.text.split()
        return len(words)

    def unique_words(self):
        words = self.text.split()
        unique_words_set = set(word.lower() for word in words)
        return list(unique_words_set)

    def reverse_string(self):
        return self.text[::-1]
