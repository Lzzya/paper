# -*- coding: utf-8 -*-
import csv,sys
import pandas as pd
# from sklearn import linear_model

print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
# Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
print sys.getdefaultencoding()
# 1 读取原始数据，并且汇总至一张表rawDataAll
rawDataAll = pd.DataFrame()
for i in range(8,13):
    fileName = 'sale_by_sku\\2016.'+str(i)+'.csv'
    rawData = pd.read_csv(fileName,encoding="GB2312")
    # print "2016年",str(i)+"月数据有",len(rawData),"行"
    rawDataAll = rawDataAll.append(rawData,ignore_index = True)
    # print rawDataAll.head()

for i in range(1,9):
    fileName = 'sale_by_sku\\2017.'+str(i)+'.csv'
    rawData = pd.read_csv(fileName,encoding="GB2312")
    # excel打开csv文件，可以识别编码“GB2312”，但是不能识别“utf-8”,数据库里的字符串编码是utf-8.
    # decode('utf-8')表示把utf-8编码转换为unicode编码；encode('utf-8')表示把unicode编码转换为utf-8编码

    # print "2017年",str(i)+"月数据有",len(rawData),"行"
    rawDataAll = rawDataAll.append(rawData,ignore_index = True)

print rawDataAll.head(),'\n', len(rawDataAll)

# 1.2 取具有相关特征的数据集子集

# subColDataAll = rawDataAll.loc[:,[u"下单日期","sku",u"一级部门名称",u"二级部门名称",u"订单计数",u"销售数量",u"销售额",u"直降优惠"
#                                   u"满减优惠",u"用券优惠金额]]
# print subColDataAll.head()

# 1.3 按日期分组
groupDataAll = rawDataAll.groupby(by=[u"下单日期",u"二级部门名称"]).sum()
groupDataAll_2 = rawDataAll.groupby(by=[u"二级部门名称",u"下单日期"]).sum()

# print groupDataAll.head(),len(groupDataAll),type(groupDataAll)

print "STOP 1"
writer = pd.ExcelWriter('output.xlsx')
groupDataAll.to_excel(writer, "Sheet1")
groupDataAll_2.to_excel(writer, "Sheet2")
writer.save()
print "STOP 2"


print "STOP 3"

