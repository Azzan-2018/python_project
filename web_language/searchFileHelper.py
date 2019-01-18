import fileinput
import sys
import re

class SearchFileHelper:

    def __init__(self, xlsPath):
        self._xlsPath = xlsPath
        try:
           self.__file = open(xlsPath, 'r', encoding='UTF-8')
        except :
           print('error')

    def searchLanguageWordMap(self):
        keyValMap = {}
        for line in self.__file:
            temp = self.searchKeyAndValFromLine(line.strip().replace('\"', ''))
            if len(temp) > 1:
                keyValMap[temp[0]] = temp[1].strip().replace(',', '')
        return keyValMap

    def searchKeyAndValFromLine(self, line):
        if (line and line.find(r':') > -1):
            return re.split(r':', line)
        else: return []
    
    def searchKeyAndValByTemplate(self):
        match = re.compile(r'(?<=intl\.get)(\([\'\"][\w\s\.]*[\'\"]\))')
        replaceRep = re.compile(r'[()"\']')
        keySet = set()
        for line in self.__file:
            for key in match.findall(line):
                keySet.add(replaceRep.sub('', key))
        return keySet

        


            
        




