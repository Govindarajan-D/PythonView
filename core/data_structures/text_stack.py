class TextStack:
    def __init__(self):
        self.texts = []

    def add_step(self, new_code):
        self.texts.append(new_code)

    def remove_step(self):
        self.texts.pop()

    def append(self, append_text):
        self.add_step(append_text)

    def __add__(self, new_code):
        self.add_step(new_code)

    def __str__(self):
        return self.texts.__str__()

    def __len__(self):
        return self.texts.len
