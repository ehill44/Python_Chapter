def cointoss():
    sumh=0
    sumt=0
    for i in range(1,20):
        import random
        coin=random.choice(['heads', 'tails'])
        if coin=='heads':
            sumh+=1
        if coin=='tails':
            sumt+=1
        print "Attempt {}: Throwing a coin...It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(i, coin, sumh, sumt)

cointoss()