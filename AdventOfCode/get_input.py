import requests
import browser_cookie3
import os

def get_data(year, day):

    if not os.path.isfile("input.txt"):
        cookie = browser_cookie3.firefox()

        req = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies = cookie).text

        with open("input.txt", 'w') as f:
            f.write(req)

        return req.strip()

    else:

        with open("input.txt", 'r') as f:

            return f.read().strip()
    

def split_on_lines(string, to_type = "str"):

    out = string.split("\n")
    if to_type == "int":
        out = [int(num) for num in out]
    elif to_type == "float":
        out = [float(num) for num in out]

    return out

if __name__ == "__main__":
    
    print(split_on_lines(get_data(2021, 1), to_type = "int"))
