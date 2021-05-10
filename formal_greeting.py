def make_formal_greeting(name, title):
    return("This is %s, the %s " % (name, title))

#mustard = make_formal_greeting('Mustard', 'Colonel')
#print(mustard)

#These two names don't have to be the same as above inside the par.
user_name = input("What is your name? ")
user_title = input("What is you title? ")

print(make_formal_greeting(user_name, user_title))

