val=x:
if isinstance (val, int):
    if val>=100:
        print "That's a big number!"
    else:
        print "That's a small number"


if isinstance (val, str):
    if len(str)>=50:
        print "Long Sentence"
    else: 
        print "Short Sentence"


if isinstance(val, list):
    if len(list)>=10:
        print "Big List"
    else:
        print "Short List"