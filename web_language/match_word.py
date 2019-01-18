import sys
import os
from os.path import isfile, isdir, normpath
sys.path.append(os.path.abspath('./android_language'))
import xlSHelper
from more_itertools.more import difference
import searchFileHelper
import glob


def searchFiles(dirPath, files):
    if os.path.isfile(dirPath):
        if dirPath.endswith('.jsx'):
             files.add(dirPath)
    else:
         for name in os.listdir(dirPath):
            searchFiles(os.path.join(dirPath, name), files)
  

def main():
    basePath = 'D:/project/Code/web/Davao_web/app/public/file/locales/'
    zhFile = basePath+'zh-CN.json'
    enFile = basePath + 'en-US.json'
    zhMap = searchFileHelper.SearchFileHelper(zhFile).searchLanguageWordMap()
    enMap = searchFileHelper.SearchFileHelper(enFile).searchLanguageWordMap()

    jsFileBase = 'D:/project/Code/web/Davao_web/app/component'
    # jsFileBase = 'D:/python_project/web_词条/'
    languageKeys = set()
    files = set()
    searchFiles(jsFileBase, files)
    for filePath in files:
        languageKeys = languageKeys.union(searchFileHelper.SearchFileHelper(
             filePath).searchKeyAndValByTemplate())

    unTranslateEnMap = dict.fromkeys([x for x in zhMap if x not in enMap])
    unTranslateZhMap = dict.fromkeys([x for x in enMap if x not in zhMap])

    unTranslateKeys = languageKeys.difference(set(zhMap.keys()).intersection(set(enMap.keys())))
    xlSHelper.XLSHelper(
        'D:/python_project/web_词条/web词条统计.xls').generate_web_static_language_xls(unTranslateEnMap, unTranslateZhMap, dict.fromkeys(unTranslateKeys))

    print(' ==== ' + "unTranslateEnMap" + '=====')
    print(unTranslateEnMap)
    print(' ==== ' + "unTranslateZhMap" + '=====')
    print(unTranslateZhMap)
    print(' ==== ' + "unTranslateKeys" + '=====')
    print(unTranslateKeys)

if __name__ == '__main__':
    main()
