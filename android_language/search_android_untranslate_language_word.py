# -*- coding: utf-8 -*-
import sys
import xdrlib
from xlSHelper import XLSHelper
from xmLHelper import XMLHelper

def main():
    keyValMapZh = {}
    keyValMapEn = {}
    unTransMap = {}
    languageMap = {}
    basePath = 'D:/project/Code/ztjk/'
    moduleArray = ['baseui', 'app','account','capital','market','transaction']
    middenPath = '/src/main/res/values'
    for path in moduleArray:
        absolutePath = basePath+path+middenPath+'-zh/strings.xml'
        xml = XMLHelper(absolutePath)
        mapVal = xml.getKeyValueMap()
        unTransMap = dict.fromkeys([x for x in keyValMapZh if x in mapVal])
        print(' ==== ' + absolutePath + '=====')
        print(unTransMap)
        keyValMapZh = dict(keyValMapZh, **mapVal)
    for path in moduleArray:
        absolutePath = basePath+path+middenPath+'/strings.xml'
        xml = XMLHelper(absolutePath)
        mapVal = xml.getKeyValueMap()
        unTransMap = dict.fromkeys([x for x in keyValMapEn if x in mapVal])
        keyValMapEn = dict(keyValMapEn, **mapVal)

    for key in keyValMapZh.keys():
        languageMap[keyValMapZh.get(key)] = keyValMapEn.get(key)

    XLSHelper('').generate_language_xls(languageMap, unTransMap)

#    for row in tables:
    # print(excel_table_byname())


if __name__ == '__main__':
    main()
