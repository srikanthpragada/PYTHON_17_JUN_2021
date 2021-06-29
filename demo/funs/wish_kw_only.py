# Keyword-only arguments
def wish(*, message, name):
    print(message, name)


# wish('Scott', 'Hello')  # Positional
wish(message="Good Morning", name="Tom")  # Keyword
