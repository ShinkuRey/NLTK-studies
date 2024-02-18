import nltk 
nltk.download('punkt')
import string


from nltk.tokenize import sent_tokenize, word_tokenize


def read_file(filename, param,  measure=None, param2=None):
    with open (filename, "r", encoding = "utf-8") as file:
        text = file.read()        
        if param == "word":
            res = word_tokenize(text)
        elif param == "sent":
            res = sent_tokenize(text)
        elif param == "raw":
            res = text
        else:
            res = text


        punct_remove = str.maketrans('', '', string.punctuation)
        res = [w.translate(punct_remove) for w in res]
        res = [w.lower() for w in res]
    
        if measure is not None:
            if measure == "length":
                return len(res)
            
            elif measure == "unique":
                return len(set(res))
            
            
            elif param2 is not None and measure == "compare":
                if param2 == "word":
                    res2 = word_tokenize(text)

                elif param2 == "sent":
                    res2 = sent_tokenize(text)

                else:
                    raise ValueError("Неверный параметр 3")
                res2 = [w.translate(punct_remove) for w in res2]
                res2 = [w.lower() for w in res2]

                return round(len(res) / len(res2), 2)

            else: 
                raise ValueError("Неверный параметр 4")


        return res
        

res = read_file("file.txt", "raw",  "compare", "word")



print (res)
