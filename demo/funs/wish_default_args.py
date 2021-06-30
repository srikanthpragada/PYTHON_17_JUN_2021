def wish(name="Guest", message="Hello"):
    print(message, name)


wish('Scott')  # Positional
wish("Steve", "Hi")
wish(message="Good Morning", name="Tom")  # Keyword
wish()
wish(message="Hi")
