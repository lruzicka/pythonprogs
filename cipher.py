class Message(object):
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
                 
    def input_clean(self,text):
        self.text = text

    def output_clean(self):
        return(self.text)

    def num_alph(self):
        nalphabet = {}
        d = enumerate(self.alphabet)
        for i in d:
            nalphabet[i[0]] = i[1]
        return(nalphabet)

    def cipher_alphabet(self, key):
        pass


text = Message()
text.input_clean("This is a text.")
print(text.numalph())
print(text.output_clean())
