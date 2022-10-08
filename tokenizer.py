import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords as sw
from nltk.tokenize import sent_tokenize as st
from nltk.tokenize import word_tokenize as wt

import Training as t
import analyzer as an


def divsText(data):
    # This function takes as input a dictionary of divs and produces a sequence of word
    divs = an.GetDivs(data)
    output = ""
    for i in divs.values():
        output = output + i.text
    return output


def HeadingsText(data):
    # This function takes as input a dictionary of headingss and produces a sequence of word
    headings = an.GetHeadings(data)
    output = ""
    for i in headings.values():
        output = output + i.text
    return output


def ParagraphsText(data):
    # This function takes as input a dictionary of paragraphs and produces a sequence of word
    paragraphs = an.GetParagraphs(data)
    output = ""
    for i in paragraphs.values():
        output = output + i.text
    return output


def AltText(data):
    # This function takes as input a dictionary of image alts and produces a sequence of word
    alt = an.GetImagesAlt(data)
    output = ""
    for i in alt.values():
        output = output + "," + str(i)
    return output


def CompleteText(data):
    # this function combine the divs,headings,paragraphs,and alt and produces a sequence of word
    text = divsText(data) + HeadingsText(data) + ParagraphsText(data) + AltText(data)
    return text


def Sentence(data):
    # this function take complete sequence of words and produce a list of  sentences
    text = CompleteText(data)
    sentences = st(text)
    return sentences


def words(data):
    # this function take complete sequence of words and produce a list of words
    text = CompleteText(data)
    words = wt(text)
    return words


def wordswithfrequencies(data):
    # this function take words of list and produce the frequency of all words
    text = words(data)
    wordswithfrequencies = nltk.FreqDist(text)
    keyvaluepairs = wordswithfrequencies.items()
    return keyvaluepairs


def Gplot(data):
    # this function take words and their frequencies and produce the  plot of  a graph(curve)
    word = words(data)
    text = nltk.FreqDist(word)
    # print(text.values())
    # print(text.keys())
    n = len(text)
    pllt = text.plot(n, cumulative=False)
    return pllt


def plot(data):
    # this function take figure(graph) and save graph in internal storage
    fig = plt.figure()
    Gplot(data)
    plt.show()
    fig.savefig("static/images/Frequencygraph.png")
    return fig


def stopwords(data):
    # this function produce all stopwords of english words
    stops = sw.words('english')
    return stops


def Removestopword(data):
    # this function remove all stopwords of given data(or input)
    text = CompleteText(data)
    stops = sw.words('english')
    tokens = wt(text)
    for token in tokens:
        if token in stops:
            tokens.remove(token)
    return token


def frerstopword(data):
    # this fuction produce the frequencies of words(after removal of stop words)
    text = Removestopword(data)
    wf = nltk.FreqDist(text)
    kvp = wf.items()
    return kvp


def Rplot(data):
    # this fuction plot the graph between frequencies and the words(after removal of stop words)
    words = Removestopword(data)
    text = nltk.FreqDist(words)
    # print(text.values())
    # print(text.keys())
    print(text)
    n = len(text)
    pltt = text.plot(n, cumulative=False)
    return pltt


def RSWplot(data):
    # this function take figure(graph) from Rplot and save graph in internal storage
    fig = plt.figure()
    Rplot(data)
    plt.show()
    fig.savefig("static/images/RSWplot.png")
    return fig


def getset(data):
    # this function covert the words(after removal of stop words) into set of given data(or input).
    words = Removestopword(data)
    text = nltk.FreqDist(words)
    n = text.keys()
    s1 = set()
    for x in n:
        s1.add(x)
    return s1


def trainingset():
    # this fuction produce the training set
    m = t.training()
    return m
    x = trainingset()
    print(x)


def intersectionset(data):
    # this fuction produce the intersection of  training set and getset
    s1 = trainingset()
    s2 = getset(data)
    m = s1.intersection(s2)
    return m


def dict1(data):
    # this fuction  convert word list  into a dictionary
    word = words(data)
    text = nltk.FreqDist(word)
    return text


def freinterset(data):
    # this function produce frequency of intersection of sets(trainingset and getset)
    # d=dict1(data)
    # print(d)
    # print(d.items())
    l = list(intersectionset(data))
    text = dict1(data)
    # print(l)
    l2 = []
    l3 = []
    for word in l:
        l2.append(word)
        l3.append(text[word])
        # print(x,y)
    # print(l2)
    # print(l3)
    # print ("Words : " + str(l2))
    # print ("frequencies" + str(l3))
    res = {l2[i]: l3[i] for i in range(len(l2))}
    # print ("Combine both in dictionary : " +  str(res))
    return res


def interplot(data):
    # this fuction produce graph between frequency and words of intersection of two sets
    words = freinterset(data)
    text = nltk.FreqDist(words)
    # print(text.values())
    # print(text.key.s())
    n = len(text)
    pltt = text.plot(n, cumulative=False)
    return pltt


def interfreGraph(data):
    # this function take figure(graph) from interplot and save graph in internal storage
    fig = plt.figure()
    interplot(data)
    plt.show()
    fig.savefig("static/images/intersetplot.png")
    return fig


def getFullData(data, trainingset):
    ##intersectionset list and corresponding frequensies list
    mainset = getset(data)
    # trainingset=getset(trainingsetdata)
    m = mainset.intersection(trainingset)
    l = list(m)
    text = dict1(data)
    words = []
    frequencies = []
    for word in l:
        words.append(word)
        frequencies.append(text[word])
    return words, frequencies


def getFullplot(data, trainingset):
    lst = getFullData(data, trainingset)
    w = lst[0]
    f = lst[1]
    # print(w)
    res = {w[i]: f[i] for i in range(len(w))}
    text = nltk.FreqDist(res)
    n = len(text)
    pltt = text.plot(n, cumulative=False)
    return pltt


def getsaveFullplot(data, trainingset):
    # this function take figure(graph) from interplot and save graph in internal storage
    newfig = plt.figure()
    getFullplot(data, trainingset)
    plt.show()
    newfig.savefig("static/images/training2plot.png")
    return newfig
