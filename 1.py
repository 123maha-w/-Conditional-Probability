def a_and_b(a,b):

    if a == 1:
        prob_student = 0.3
        if b == 1:
            prob_dining = 0.75
        else :
            prob_dining = 0.25
        print("probibility of a given b :",prob_dining)

        if a == 2:
            prob_student = 0.7
            if b == 1:
                prob_dining = 0.75
            else :
                prob_dining = 0.4
            print("probibility of a given b :",prob_dining)

    prob_a_and_b =  prob_student*prob_dining
    return round(prob_a_and_b,3)

print("check the probibility of any event occring. first enter your choices.")

print("is the student a freshmen ? \n 1. yes \n 2. no")
a = int(input("enter your choice (1/2):"))

print("is the student eating in the dining hall ? \n 1. yes \n 2. no")
b = int(input("enter your choice (1/2):"))

print("here is the probibility of both events occuring : ",a_and_b(a,b))