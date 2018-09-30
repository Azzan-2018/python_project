# -*- coding: utf-8 -*-
import xdrlib
import sys
from XLSHelper import *
from XMLHelper import *


def main():
    keyValMap = {}
    # for path in ["file.xls","file2.xls"]:  TEST
    # for path in ["各场景提示内容.xlsx", "英文版效果图文字内容.xlsx", "页面跳转及相关提示语内容.xlsx", "词条补充1.xls","自翻译词条.xlsx"]:
    for path in ["词条集合.xlsx"]:
        keyValMap = dict(keyValMap, **(XLSHelper(path).getKeyValMap()))
        # tempMap = XLSHelper(path).getKeyValMap()
        # for key in tempMap.keys():
        #     text = tempMap.get(key)
        #     if text:
        #         keyValMap[key] = text

    print(keyValMap)
    noUseMap = keyValMap
    unTranslateMap = {}
    # for path in ["in.xml","in2.xml"]:  TEST
    for path in ["zh/account/strings.xml", "zh/app/strings.xml", "zh/baseui/strings.xml",
                 "zh/capital/strings.xml", "zh/market/strings.xml", "zh/transaction/strings.xml"]:
        xml = XMLHelper(path)
        xml.translate(keyValMap)
        noUseMap = dict.fromkeys(
            [x for x in noUseMap if x not in xml.getUsableKeyValMap()])
        unTranslateMap = dict(unTranslateMap, **xml.getUnTranslateKeyValMap())
    keys = noUseMap.keys()
    for key in keys:
        noUseMap[key] = keyValMap.get(key)
    print("nouseMap ---")
    print(noUseMap)
    print("unTranslateMap ---")
    print(unTranslateMap)
    XLSHelper("").write_xls(noUseMap, unTranslateMap)

#    for row in tables:
    # print(excel_table_byname())


if __name__ == "__main__":
    main()
