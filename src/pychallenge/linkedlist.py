def run():
    import urllib.request
    import urllib.parse
    import re

    p = re.compile("the\ next\ nothing\ is\ (\d*)")

    data = {}
    next_value = "12345"
    for i in range(400):
        print(i)
        data["nothing"] = next_value
        url_values = urllib.parse.urlencode(data)

        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
        full_url = url + "?" + url_values
        response = urllib.request.urlopen(full_url).read().decode("utf-8")
        print(response)
        if "Divide by two and keep going" in response:
            print("Didviding by 2")
            next_value = "%i" % (int(next_value) / 2)
        else:
            next_value = p.search(response).groups()[0]
        print("asking with ", next_value)


if __name__ == "__main__":
    run()
