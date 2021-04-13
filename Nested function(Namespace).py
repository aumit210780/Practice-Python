def wrapper(string):
    def clean():
        print(string.upper())
    return clean # or print(clean())
wrapper("Programming")()