# -*- coding: utf-8 -*-
import xdrlib
import sys
from XLSHelper import *
from XMLHelper import *


def main():
    keyValMapZh = {}
    keyValMapEn = {}
    unTransMap = {}
    languageMap = {}
    for path in ["zh/account/strings.xml", "zh/app/strings.xml", "zh/baseui/strings.xml",
                 "zh/capital/strings.xml", "zh/market/strings.xml", "zh/transaction/strings.xml"]:
        xml = XMLHelper(path)
        mapVal = xml.getKeyValueMap()
        unTransMap = dict.fromkeys([x for x in keyValMapZh if x in mapVal])
        keyValMapZh = dict(keyValMapZh, **mapVal)
    for path in ["en/account/strings.xml", "en/app/strings.xml", "en/baseui/strings.xml",
                 "en/capital/strings.xml", "en/market/strings.xml", "en/transaction/strings.xml"]:
        xml = XMLHelper(path)
        mapVal = xml.getKeyValueMap()
        unTransMap = dict.fromkeys([x for x in keyValMapEn if x in mapVal])
        keyValMapEn = dict(keyValMapEn, **mapVal)

    for key in keyValMapZh.keys():
        languageMap[keyValMapZh.get(key)] = keyValMapEn.get(key)

    XLSHelper("").generate_language_xls(languageMap, unTransMap)

#    for row in tables:
    # print(excel_table_byname())


if __name__ == "__main__":
    main()
