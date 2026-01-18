def read_config():
    f = open("config.txt")
    data = f.read()
    f.close()
    return data
