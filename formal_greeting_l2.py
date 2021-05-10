def make_formal_greeting(name, title):
    return("This is %s, the %s " % (name, title))

# These two names don't have to be the same as above inside the par.
def ask_for_user_info():
    user_name = input("What is your name? ")
    user_title = input("What is you title? ")
    return [user_name, user_title]

def ask_for_user_info():
    user_name = input("What is your name? ")
    user_title = input("What is you title? ")
    return {
        "name": user_name,
        "title": user_title
    }
#print(ask_for_user_info())
    user_info = ask_for_user_info()
    greeting = make_formal_greeting(user_info[name], user_title[title])
    print(greeting)
