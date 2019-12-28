'''excel表格追加'''

# from xlutils.copy import copy
# import xlrd
# file=xlrd.open_workbook("a.xls")
# New_file=copy(file)  #不是直接操作我们打开excel文件，而是复制一份操作复制的文件,只有写的操作，没有读功能
# #get_sheet(下标位置），根据下标位置进入标签页
# biao_qian_ye=New_file.get_sheet(0)
# print(biao_qian_ye)
# biao_qian_ye.write(11,11,"内容")
# New_file.save("11.xls")


# a = open(r'E:\tulili\pyxiangmu1\a.txt','w',encoding='utf - 8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         a.write('{} * {} = {}'.format(j,i,j * i))
#     a.write('\n')
# a.close()

# import xlwt
# file = xlwt.Workbook(encoding='utf - 8')
# sheet = file.add_sheet('a')
# a = open(r'E:\tulili\pyxiangmu1\a.txt','r',encoding='utf -8')
# b = a.readlines()
# a.close()
# for i in range(len(b)):
#     sheet.write(i,0,b[i])
# file.save('a.xls')




import xlwt       #创建写的模块
file=xlwt.Workbook(encoding="utf-8")   #创建文件，设置编码方式
sheet=file.add_sheet("a")     #创建标签页,并命名标签页为a
a=open(r"E:\tulili\pyxiangmu1\a.txt","r",encoding="utf-8")  #设置文件的权限
b=a.readlines()  #将a按照列表的形式显示
a.close()
for i in range(5):
    sheet.write(i,0,b[i])
file.save("c.xls")



































