def run_def():
    from os.path import join, split
    import re

    filename = join(split(__file__)[0], "def.html")

    with open(filename) as f:
        content = f.read().replace("\n", "")

    p = re.compile("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]")
    # p.match(content)
    print("".join(p.findall(content)))


if __name__ == "__main__":
    run_def()
