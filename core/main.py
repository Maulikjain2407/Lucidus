from data.data_loader import file_loader

from configs.configs import stopwords as STOPWORDS

from core.preprocessing import data_preprocesser,stopword_remover

def main():
    data=file_loader()
    tokens=data_preprocesser(data)
    filtered=stopword_remover(tokens,STOPWORDS)
    print(filtered)

if __name__=="__main__":
    main()