firstdictionary={
    'name':'Anna',
    'age':101,
    'birthcountry':'The United States',
    'favlanguage':'Python',
}
print firstdictionary.values()
def maybe(input):
    for values in input:
        print "My name is {name}. I am {age}. I was born in {birthcountry} and my favorite language is {favlanguage}.".format(**firstdictionary)

maybe(firstdictionary)