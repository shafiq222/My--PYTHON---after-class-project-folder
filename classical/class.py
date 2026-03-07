class StringReverse:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()      
        reversed_words = words[::-1]   
        return " ".join(reversed_words)  


sentence = "Hello world from Python"
obj = StringReverse(sentence)

print(obj.reverse_words())