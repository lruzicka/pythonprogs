class Alphabet(object):
    def __init__(self):
        self.alphabet = {}
        for i in range(129):
            self.alphabet[i] = chr(i)
        
    def get_value(self, key):
        value = self.alphabet[key]
        return(value)
        
    def get_key(self, value):
        for i in self.alphabet.items():
            if i[1] == value:
                key = i[0]
        return(key)
    



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


abeceda = Alphabet()
alfa = abeceda.get_value(97)
beta = abeceda.get_key("a")

print(alfa)
print(beta)
