# import xdrlib
# import sys
import xlrd
from xlwt import *


class XLSHelper:

    def __init__(self, xlsPath):
        self._xlsPath = xlsPath

    def open_excel(self, file='file.xls'):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception:
            print("error")
    # 根据索引获取Excel表格中的数据   参数:file：Excel文件路径
    # colnameindex：表头列名所在行的所以  ，by_index：表的索引

    def excel_table_byindex(self, colnameindex=0, by_index=0):
        data = self.open_excel(self._xlsPath)
        table = data.sheets()[by_index]
        nrows = table.nrows  # 行数
        ncols = table.ncols  # 列数
        colnames = table.row_values(colnameindex)  # 某一行数据
        keyValMap = {}
        for rownum in range(0, nrows):
            row = table.row_values(rownum)
            if row:
                keyValMap[row[2]] = row[3]
        return keyValMap


    def write_map(self, table, keyValMap):
        keys = keyValMap.keys()
        position = 0
        for key in keys:
            position = position+1
            table.write(position, 0, key)
            table.write(position, 1, keyValMap.get(key))

    def write_xls(self,noUsekeyValMap,unTanslateMap):
        file = Workbook(encoding = 'utf-8')
        #指定file以utf-8的格式打开
        self.write_map(file.add_sheet("没有翻译"), unTanslateMap)
        self.write_map(file.add_sheet('没用翻译'), noUsekeyValMap)
        file.save("词条.xls")

    def generate_language_xls(self,languageMap,unTanslateMap):
            file = Workbook(encoding = 'utf-8')
        #指定file以utf-8的格式打开
        self.write_map(file.add_sheet("未重叠翻译"), languageMap)
        self.write_map(file.add_sheet('重复翻译'), unTanslateMap)
        file.save("词条重复扫描.xls")

    def getKeyValMap(self):
        return self.excel_table_byindex()


def main():
    keyValMap = XLSHelper("file.xls").getKeyValMap()
    print(keyValMap)


if __name__ == "__main__":
    main()
