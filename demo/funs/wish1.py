
def wish(hour):
    if hour < 12:
        print("Good Morning!")
    elif hour < 17:
        print("Good Afternoon!")
    else:
        print("Good Evening!")

    
wish(18)   # call to function
# wish()