import json
import mimetypes
import os
import re
import webbrowser
from argparse import ArgumentParser
import pyperclip
import requests


class Screeny:
    def __init__(self, config,):
        if os.path.isfile(config):
            configHandle = open(config, "r")
            self.config = json.load(configHandle)
            configHandle.close()
        else:
            raise FileNotFoundError(config)

    def uploadString(self, string):
        files = {self.config["FileFormName"]: string}
        r = requests.post(self.config["RequestURL"], files=files, data=self.config["Arguments"])
        return r.text

    def uploadFile(self, file):
        if os.path.isfile(file):
            handle = open(file, 'rb')
            string = handle.read()
            handle.close()
            return self.uploadString((file, string, mimetypes.guess_type(file)[0]))
        else:
            raise FileNotFoundError(file)

    def handleRegex(self, data):
        if len(self.config["RegexList"]) == 0:
            return data
        regexList = []
        for pattern in self.config["RegexList"]:
            regexList.append(re.search(pattern, data).group())

        url = self.config["URL"]
        for index, group in enumerate(regexList):
            url = url.replace("${0}$".format(index + 1), group)

        return url
if __name__ == '__main__':
    argparse = ArgumentParser()
    argparse.add_argument("file")
    argparse.add_argument("--config")
    argparse.add_argument("-clipboard", action="store_true")
    argparse.add_argument("-browser", action="store_true")

    args = argparse.parse_args()

    if not args.config:
        args.config = "{0}/.screeny.json".format(os.path.expanduser("~"))
        if not os.path.isfile(args.config):
            print("Insert default ShareX config in ~/.screeny.json")

    screeny = Screeny(args.config)
    returnedData = screeny.uploadFile(args.file)
    url = screeny.handleRegex(returnedData)
    print(url)
    if args.clipboard:
        pyperclip.copy(url)
    if args.browser:
        webbrowser.open(url)

