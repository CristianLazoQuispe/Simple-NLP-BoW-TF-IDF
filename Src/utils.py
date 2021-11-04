import os
import numpy as np

def load_text(filelocation):
    with open(filelocation, 'r') as f:
        data = f.readlines()
    f.close()
    return data

def clean_dataset(data):
    simbols = ['.', ',', '"']
    stopwords = ['ab','ac','ad','adhic','aliqui','aliquis','an','ante','apud','at','atque','aut','autem','cum','cur','de','deinde','dum','ego','enim','ergo','es','est','et','etiam','etsi','ex','fio','haud','hic','iam','idem','igitur','ille','in','infra','inter','interim','ipse','is','ita','magis','modo','mox','nam','ne','nec','necque','neque','nisi','non','nos','o','ob','per','possum','post','pro','quae','quam','quare','qui','quia','quicumque','quidem','quilibet']

    new_data = []
    for text in data:
        new_text = text.lower()
        
        for simbol in simbols:
            new_text = new_text.replace(simbol,'')
        for stopword in stopwords:
            new_text = new_text.replace(stopword,'')
        
        new_text = new_text.strip()

        new_text = ' '.join(new_text.split()) # remove multiple spaces

        new_data.append(new_text)
    return new_data


def get_vocabulary(data):
    vocabulary = {}
    for text in data:
        words = text.split(' ')
        for word in words:
            vocabulary[word]= 0
    print('number of words: ',len(vocabulary))

    return vocabulary