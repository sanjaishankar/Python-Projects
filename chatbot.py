import nltk
from nltk.stem.lancaster import LancasterStemmer
stemer = LancasterStemmer()

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import numpy
import tflearn
import json
import random
import pickle


with open("socrce.json") as file:
    data = json.load(file)
try:
    with open('data.pickle',"rb") as f:
        words,labels,training,output = pickle.load(f)
except:    
    labels = []
    docs_x = []
    docs_y = []
    words = []

    for intents in data['intents']:
        for pattern in intents['patterns']:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intents['tag'])
        if intents not in labels:
            labels.append(intents["tag"])
            
    words = [stemer.stem(w.lower()) for w in words if w != '?']
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []


    out_emtpy = [0 for _ in range(len(labels))]

    for x,doc in enumerate(docs_x):
        bag = []
        current = [stemer.stem(w) for w in doc]

        for w in words:
            if  w in current:
                bag.append(1)
            else:
                bag.append(0)
        out_row = out_emtpy[:]
        out_row[labels.index(docs_y[x])]

        training.append(bag)
        output.append(out_row)

    with open('data.pickle',"wb") as f:
        pickle.dump((words,labels,training,output), f)

training = numpy.array(training)
output = numpy.array(output)


net = tflearn.input_data(shape=[None,len(training[0])])
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,len(output[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load()
    print('its working')
except:
    print("its not")
    model.fit(training, output, n_epoch = 1000, batch_size=8,show_metric=True)
    model.save('bot_model')

def bag_of_words(s,words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemer.stem(word.lower()) for word in s_words]

    for given in s_words:
        for i, word in enumerate(words):
            if given == word:
                bag[i]=1
    return numpy.array(bag)

def chat():
    print("your now inside the chatbot , to stop type quit")
    while(True):
        inp = input("you :")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp,words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        
        for rs in data['intents']:
            if tag == rs['tag']:
                responses = rs['responses']
        print(random.choice(responses))
chat()