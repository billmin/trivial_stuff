import xml.etree.ElementTree as ET
import os
import sys
''' 
XML文件读取 
<?xml version="1.0" encoding="utf-8"?>
<catalog>
    <maxid>4</maxid>
    <login username="pytest" passwd='123456'>dasdas
        <caption>Python</caption>
        <item id="4">
            <caption>测试</caption>
        </item>
    </login>
    <item id="2">
        <caption>Zope</caption>
    </item>
</catalog>
'''

#遍历xml文件
def traverseXml(element):
    #print (len(element))
    if len(element)>0:
        for child in element:
            print (child.tag, "----", child.attrib)
            traverseXml(child)
    #else:
        #print (element.tag, "----", element.attrib)
        

if __name__ == "__main__":
    xmlFilePath = os.path.abspath("integration-google_product_search_stocks-pl_PL.xml")
    print(xmlFilePath)
    try:
        tree = ET.parse(xmlFilePath)
        print ("tree type:", type(tree))
    
        # 获得根节点
        root = tree.getroot()
    except Exception as e:  #捕获除与程序退出sys.exit()相关之外的所有异常
        print ("parse test.xml fail!")
        sys.exit()
    print ("root type:", type(root))    
    print (root.tag, "----", root.attrib)
    
    #遍历root的下一层
    for child in root:
        print ("遍历root的下一层", child.tag, "----", child.attrib)

    #使用下标访问
    print (root[0].text)
    print (root[1][1][0].text)

    print (20 * "*")
    #遍历xml文件
    traverseXml(root)
    print (20 * "*")
