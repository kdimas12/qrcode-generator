import pyqrcode
import datetime


def convertCode(what):
    item = pyqrcode.create(what)
    return item


def menuShow(item):
    stuf = convertCode(item)
    print("1. Export to PNG\n2. Show on terminal")
    choose = int(input("> "))
    if choose == 1:
        return stuf.png(f"qr-{datetime.datetime.today()}.png", scale=5, quiet_zone=1)
    if choose == 2:
        print(stuf.terminal(quiet_zone=1))


def main():
    inputSome = input("Enter something to convert to qr\n> ")
    menuShow(inputSome)


main()
