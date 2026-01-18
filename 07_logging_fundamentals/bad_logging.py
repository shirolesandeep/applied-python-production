def load_config(path):
    print("Loading config")
    if not path:
        print("Invalid path")
        return None
    print("Config loaded")
    return {"env": "dev"}
