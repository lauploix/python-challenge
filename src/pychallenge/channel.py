# http://www.pythonchallenge.com/pc/def/channel.html

from zipfile import ZipFile
from os.path import join, split


def run():
    file_name = join(split(__file__)[0], "channel.zip")

    with ZipFile(file_name, "r") as zip:
        # printing all the contents of the zip file
        zip.printdir()


if __name__ == "__main__":
    run()
