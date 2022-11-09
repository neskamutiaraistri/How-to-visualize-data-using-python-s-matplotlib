import matplotlib.pyplot as nsk

nsk.axis([0,5,0,20]) #batas sumbu x dan sumbu y
nsk.plot([1,2,3,4],[1,4,9,16],'ro-') #nilai data yang di plot
nsk.text(1.1,12,'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
nsk.title('Plot Data Persamaan Kuadrat',fontsize=20,fontname='Times New Roman')
nsk.xlabel('x',fontsize=16,fontname='Times New Roman',color='blue')
nsk.ylabel('y',fontsize=16,fontname='Times New Roman',color='blue')
nsk.grid(True)
nsk.legend(['First series'])
nsk.savefig('grafik.png')
nsk.show()
