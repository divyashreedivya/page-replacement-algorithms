from django.shortcuts import render
from django.views import View
from .forms import InputForm

#function for transpose
def transpose(l1, num):
    for i in l1:
        while(len(i) < num):
            i.append("-")      



    l2 = list(zip(*l1))
    return l2

#fifo algorithm
def fifo(sequence,frameAmt):
    fifofinalList=[]
    fifoallList = []
    sequenceList = sequence
    frames = []
    hit = 0 #stores number of hits
    miss = 0 #stores number of misses
    replaceIndex = 0
    temp = []
    #fifo algorithm
    for s in sequenceList:     
        if s in frames:
            hit += 1
            if 'red' in temp[replaceIndex - 1]: #removing old "red" value
                temp[replaceIndex - 1] = temp[replaceIndex - 1][3:]

        else:
            miss += 1
            if len(frames) == frameAmt:
                frames[replaceIndex] = s
                
            else:
                frames.append(s)
            temp = frames[:] #copying the list by value
            temp[replaceIndex] = 'red'+temp[replaceIndex] #adding "red" to the new value that is replaced
            
            replaceIndex = (replaceIndex + 1) % frameAmt
            
        
        fifoallList.append(temp[:])
    # print('------------')
    # print(fifoallList)
    fifofinalList = transpose(fifoallList, frameAmt) #transpose 

    ratio = 100.0*hit/(len(sequenceList))
    
    fifoctx = {'finalList':fifofinalList,'miss':miss,'hit':hit,'ratio':ratio} #fifo object
    # print(fifoctx)
    return fifoctx

#lru alogorithm


def lru(sequence, frameAmt):
    lrufinalList[]
    sequenceList = sequence
    frames = []
    lruallList = []
    hit = 0
    miss = 0
    temp = []

    #lru algorithm
    for s in sequenceList:
        if s not in frames:
            miss += 1
            if len(frames) == frameAmt:
                frames.remove(frames[0])
                frames.append(s)
                temp = frames[:]
                temp[-1] = 'red'+temp[-1]
            else:
                frames.append(s)
                temp = frames[:]
                temp[-1] = 'red'+temp[-1]
        else:
            hit += 1
            frames.remove(s)
            frames.append(s)
            temp = frames[:]

        lruallList.append(temp)
    lrufinalList = transpose(lruallList, frameAmt)#transpose
    
    lruratio = 100.0*hit/(len(sequenceList))
    lructx = {'finalList': lrufinalList, 'miss': miss,'hit': hit, 'ratio': ratio}  # fifo object
    pass

#opt algorithm
def opt(sequence,frameAmt):
    pass

#index view
def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        
        sequenceString = form.cleaned_data["seq"]
        frameAmtString = form.cleaned_data["frames"]
    return render(request, "algorithms/index.html",
    {
        "form": InputForm()
    })

#result view
def result(request):
    if(request.method=='POST'):
        sequenceString = request.POST["seq"]
        frameAmtString = request.POST["fsize"]

        sequenceList = sequenceString.split()
        frameAmount = int(frameAmtString)
        fifoctx = fifo(sequenceList, frameAmount)

        return render(request,"algorithms/result.html",{
            'form':InputForm(), #form
            'sequence':sequenceString.split(), #input sequence 
            'frameAmount':frameAmount,  #frame size
            'length':len(sequenceString.split()), #number of references
            'fifo':fifoctx #fifo
        })
