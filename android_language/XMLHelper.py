import xdrlib
import sys
from xml.etree.ElementTree import ElementTree, Element
import os.path
import shutil


class XMLHelper:

    _usableMap = {}
    _unTranslateMap = {}

    def __init__(self, inXmlPath):
        self._inXmlPath = inXmlPath
        self._usableMap = {}
        self._unTranslateMap = {}

    def read_xml(self):
        '''读取并解析xml文件
       in_path: xml路径
       return: ElementTree'''
        tree = ElementTree()
        tree.parse(self._inXmlPath)
        return tree

    def write_xml(self, tree, out_path):
        '''将xml文件写出
        tree: xml树
         out_path: 写出路径'''
        tree.write(out_path, encoding="utf-8", xml_declaration=True)

    # def if_match(node, kv_map):
    #         '''判断某个节点是否包含所有传入参数属性
    #         node: 节点
    #         kv_map: 属性及属性值组成的map'''
    #         for key in kv_map:
    #             if node.get(key) != kv_map.get(key):
    #                 return False
    #         return True

# ---------------search -----

    def find_nodes(self, tree, path):
        '''查找某个路径匹配的所有节点
        tree: xml树
        path: 节点路径'''
        return tree.findall(path)

    def get_node_by_keyvalue(self, nodelist):
        '''根据属性及属性值定位符合的节点，返回节点
        nodelist: 节点列表'''
        result_nodes = []
        for node in nodelist:
            result_nodes.append(node)
        return result_nodes

    # ---------------change -----

    def change_node_properties(self, nodelist, kv_map, is_delete=False):
        '''修改/增加 /删除 节点的属性及属性值
        nodelist: 节点列表
        kv_map:属性及属性值map'''
        for node in nodelist:
            key = node.text
            text = kv_map.get(key)
            # print ("node ----")
            # print(node)
            # print ("key ----")
            # print(key)
            # print ("val ----")
            # print(kv_map.get(key))
            if text:
                text.replace("'", "\'")
                self._usableMap[key] = text
                node.text = text
            else:
                self._unTranslateMap[node.text] = ""
            # for key in kv_map:
            #     if is_delete:
            #         if key in node.attrib:
            #             del node.attrib[key]
            #     else:
            #         self._usableMap[key] = kv_map.get(key)
            #         node.set(key, kv_map.get(key))

    def change_node_text(self, nodelist, text, is_add=False, is_delete=False):
        '''改变/增加/删除一个节点的文本
        nodelist:节点列表
        text : 更新后的文本'''
        for node in nodelist:
            if is_add:
                node.text += text
            elif is_delete:
                node.text = ""
            else:
                node.text = text

    def create_node(self, tag, property_map, content):
        '''新造一个节点
        tag:节点标签
        property_map:属性及属性值map
        content: 节点闭合标签里的文本内容
        return 新节点'''
        element = Element(tag, property_map)
        element.text = content
        return element

    def add_child_node(self, nodelist, element):
        '''给一个节点添加子节点
        nodelist: 节点列表
        element: 子节点'''
        for node in nodelist:
            node.append(element)

    def del_node_by_tagkeyvalue(self, nodelist, tag, kv_map):
        '''同过属性及属性值定位一个节点，并删除之
        nodelist: 父节点列表
        tag:子节点标签
        kv_map: 属性及属性值列表'''
        for parent_node in nodelist:
            children = parent_node.getchildren()
            for child in children:
                if child.tag == tag:
                    parent_node.remove(child)

    def getUsableKeyValMap(self):
        return self._usableMap

    def getUnTranslateKeyValMap(self):
        return self._unTranslateMap

    def getFileName(self):
        return os.path.basename(self._inXmlPath).split(".")[0]

    def getPathName(self):
        path = ""
        if self._inXmlPath.find("zh", 0) > -1 :
            path = self._inXmlPath.replace("zh", "en")
        else:
            path = "dest/" + self._inXmlPath
        dirPath = os.path.dirname(path)
        if os.path.isdir(dirPath):
            shutil.rmtree(dirPath)  # 递归删除文件夹
        os.makedirs(os.path.dirname(path))
        return path
    
    def getKeyValueMap(self):
        nodeList = self.find_nodes(self.read_xml(), "string")
        mapVal = {}
        for node in nodeList:
            mapVal[node.get("name")] = node.text
        return mapVal

    def translate(self, keyVal):
        tree = self.read_xml()
        # print("tree ----")
        # print(tree)

        nodeList = self.find_nodes(tree, "string")
        # print("nodeList ----")
        # print(nodeList)

        # print("keyVal ----")
        # print(keyVal)

        self.change_node_properties(nodeList, keyVal)

        self.write_xml(tree, self.getPathName())


# def main():
#     XMLHelper("in.xml").translate({})


# if __name__ == "__main__":
#     main()
