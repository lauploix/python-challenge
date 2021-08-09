# http://www.pythonchallenge.com/pc/def/peak.html
URL = "http://www.pythonchallenge.com/pc/def/banner.p"
from pprint import pprint


def run():
    import pickle
    import urllib.request

    response = urllib.request.urlopen(URL).read()
    o = pickle.loads(response)

    res = ""

    for line in o:
        for tup in line:
            ch = tup[0]
            occ = tup[1]
            res = res + ch * occ
        res = res + "\n"

    print(res)


if __name__ == "__main__":
    run()
