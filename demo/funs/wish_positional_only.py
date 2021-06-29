# Positional only arguments
def wish(name, message, /):
    print(message, name)


wish('Scott', 'Hello')                      # Positional
wish("Steve", "Hi")
# wish(message="Good Morning", name="Tom")    # Keyword
