import sys
from os.path import normpath

import searchFileHelper
from more_itertools.more import difference

import glob




def main():
    basePath = 'D:/project/Code/web/Davao_web/app/public/file/locales/'
    zhFile = basePath+'zh-CN.json'
    enFile = basePath + 'en-US.json'
    zhMap = searchFileHelper.SearchFileHelper(zhFile).searchLanguageWordMap()
    enMap = searchFileHelper.SearchFileHelper(enFile).searchLanguageWordMap()

    jsFileBase = 'D:/project/Code/web/Davao_web/app/'
    languageKeys = set()
    for filePath in glob.glob(jsFileBase + '/*.jsx'):
        languageKeys = languageKeys.union(searchFileHelper.SearchFileHelper(
             filePath).searchKeyAndValByTemplate())

    unTranslateEnMap = dict.fromkeys([x for x in zhMap if x not in enMap])
    unTranslateZhMap = dict.fromkeys([x for x in enMap if x not in zhMap])

    unTranslateKeys = languageKeys.difference(set(zhMap.keys()).intersection(set(enMap.keys())))
    print(' ==== ' + "unTranslateEnMap" + '=====')
    print(unTranslateEnMap)
    print(' ==== ' + "unTranslateZhMap" + '=====')
    print(unTranslateZhMap)
    print(' ==== ' + "unTranslateKeys" + '=====')
    print(unTranslateKeys)

if __name__ == '__main__':
    main()
