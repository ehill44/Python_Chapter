name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane","Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins","llamas"]


def combininglists(list1,list2):
    newdict={}
    if len(list1)>=len(list2):
        newdict=zip(list1,list2)
        print newdict
    if len(list2)>len(list1):
        newdict=zip(list2,list1)
        print newdict

combininglists(name,favorite_animal)
