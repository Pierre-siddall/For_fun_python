import requests

def get_date():
    pass
def _read_key():
    with open("Key.rtf", "r") as f:
        api_key = f.readlines()
    return api_key[-1][0:-1]



if __name__ == "__main__":
    key = _read_key()
    print(key)
