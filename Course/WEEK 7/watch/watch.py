import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    i = re.search(r"(\"(http|https)://(?:www\.)?youtube\.com/embed/[a-zA-z0-9]+\")", s)
    if i:
        i = i.group(1).replace('"', "").replace("/embed", "").replace("youtube", "youtu.be")
        if "www." in i:
            i = i.replace("www.", "")
        if ".com" in i:
            i = i.replace(".com", "")
        if "http:" in i:
            i = i.replace("http", "https")
        return i
    else:
        return None


if __name__ == "__main__":
    main()
