import matplotlib.pyplot as nsk

labels = ['Lain-lain','samsung','Apple','Huawei','Oppo','Vivo']
values = [42,21,14,9,8,7]
colors = ['red','green','pink','blue','yellow','orange']
explode = [0,1,0,0,0,0]

nsk.title('Diagram Pie Market Share Samsung')
nsk.pie(values,labels=labels,colors=colors,explode=explode,shadow=True,autopct='%1.1f%%',startangle=180)
nsk.axis('equal')
nsk.show()
