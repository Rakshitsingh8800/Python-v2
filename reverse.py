class StringReverser:

    def __init__(self, text: str):
        self.text = text

    def reverse_words(self) -> str:

        words = self.text.split()

        reversed_words = words[::-1]

        return " ".join(reversed_words)
    
s = StringReverser("Hello world this is Python")
print(s.reverse_words())