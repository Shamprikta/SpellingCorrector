import nltk
anspath='ans.txt'
resultpath='result.txt'

# Evaluate the result
def eval():
    ansfile=open(anspath,'r')
    resultfile=open(resultpath,'r')
    count=0
    nb_line=0
    for r, a in zip(resultfile,ansfile):
        ansline=a.split('\t')[1]
        ansset=set(nltk.word_tokenize(ansline))
        resultline=r.split('\t')[1]
        resultset=set(nltk.word_tokenize(resultline))
        if ansset==resultset:
            count+=1
        nb_line+=1
    print("Accuracy is : %.2f%%" % (count*1.00/nb_line))

