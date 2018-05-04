def grade():
    for x in range(1,11):
        import random
        grades=random.random()*60+51
        if grades>=90:
            print "Score;", grades, "Your Grade is A"
        if grades>=80 and grades<90:
            print "Score;", grades, "Your Grade is  B"
        if grades>=70 and grades<80:
            print "Score;", grades, "Your Grade is  C"
        if grades>=60 and grades<70:
            print "Score;", grades, "Your Grade is  D"

grade()
