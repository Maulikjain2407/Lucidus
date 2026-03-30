import re

def data_preprocesser(data):
    s=data.lower()
    clean_text=re.sub(r"[^\w\s]","",s)# here the [] are the charater set in which re will subsitute with "",^ tells NOT so that it only selects the punctuations
    #\w tells it to look only for letters and numbers and \s only tells for whitespaces, this basically says remove evrything that is NOT letter,number,whitespace
    clean_text=" ".join(clean_text.split())
    tokens=clean_text.split()

    return tokens

def stopword_remover(tokens,stopwords):
    filtered_tokens=[]
    for word in tokens:
        if word not in stopwords:
            filtered_tokens.append(word)
    return filtered_tokens
