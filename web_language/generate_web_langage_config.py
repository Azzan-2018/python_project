import sys
import os
from os.path import isfile, isdir, normpath
sys.path.append(os.path.abspath('./android_language'))
import xlSHelper
import re


def appendFileLine(file, line):
    file.write(line)

def main():
   
    jsFileBase = 'D:/python_project/web_词条/'
    keyValMap = {}
    for path in [jsFileBase+"词条集合.xlsx"]:
        keyValMap = dict(
            keyValMap, **(xlSHelper.XLSHelper(path).getKeyValMap()))
    fileArray = []
    for name in ['en-US.json', 'zh-CN.json']:
         file = open(jsFileBase + name, 'w+', encoding='UTF-8')
         appendFileLine(file, '{\n')
         fileArray.append(file)
    for zhWord in keyValMap.keys():
        replaceRe = re.compile(r'\n')
        enWord = replaceRe.sub(' ', keyValMap.get(zhWord))
        zhWord = replaceRe.sub(' ', zhWord)
        replaceRep = re.compile(r'[?!\.\'\," \n]')
        key = '"' + replaceRep.sub('_', enWord).lower() + '"'
        appendFileLine(fileArray[0], key + ':"' + enWord + '",\n')
        appendFileLine(fileArray[1], key + ':"' + zhWord + '",\n')
    for file in fileArray:
        appendFileLine(file, '}\n')
        file.close()

if __name__ == '__main__':
    main()
