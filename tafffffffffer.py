# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:40:08 2021

@author: bilal
"""
from PIL import Image
from numpy import *
from matplotlib import pyplot
old_error=0
tab=[]
img = Image.open("D:\Disque D\Bilal\Image\IMG_20180827_153322.jpg")
nbr_group=int(input("Input the number of groups  : "))
width, height = img.size
l=[[0 for x in range(100)] for y in range(100)]
print(str(width) + "x" + str(height))
for i in range(100):
  for j in range(100):
       r,v,b=img.getpixel((i,j))
       n=("P",i,j)
       tab.append([r,v,n,b])         
def distance(tab,l):
	val=[[0 for x in range(len(l))] for y in range(len(tab))]
	for i in range(len(tab)):
		for j in range(len(l)):
			val[i][j]=sqrt(((tab[i][0]-l[j][0])*(tab[i][0]-l[j][0])) + ((tab[i][1]-l[j][1])*(tab[i][1]-l[j][1])))
	return val
def appartient(i,l):
	for k in range(len(l)):
		if(i==l[k]):
			return 1
	return 0
l=[[0 for x in range(2)] for y in range(nbr_group)]
l2=[]
i=0

while (i<nbr_group):
	j=random.randint(0,len(tab)-1)
	if(appartient(j,l2)==0):
		l[i][0]=tab[j][0]
		l[i][1]=tab[j][1]
		l2.append(j)
		i=i+1





while(1==1):
	groups=[[-1 for x in range(len(tab)+1)] for y in range(nbr_group)]
	for i in range(nbr_group):
		groups[i][0]=i+1
	a=distance(tab,l)
	print("distances are  :")
	for i in range(len(a)):
		for j in range(len(a[0])):
			print("%-18f" % a[i][j],end='')
		print()
	 
	for i in range(len(a)):
		min=0
		for j in range(1,len(a[0])):
			if(a[i][min]>a[i][j]):
				min=j
		for k in range(len(groups)):
			if(min==k):
				for n in range(len(groups[0])):
					if(groups[k][n]==-1):
						groups[k][n]=i
						break
	print("groups are  : ")
	for i in range(len(groups)):
		print("the component of group {}  are :".format(i+1),end=' ')		
		for j in range(1,len(groups[0])):
			if(groups[i][j]!=-1):
				print("  {}".format(tab[groups[i][j]][2]),end='    ')
		print()    

	for i in range(len(groups)):
		s1=0
		s2=0
		m=0
		for j in range(1,len(groups[0])):
			if(groups[i][j]!=-1):
				s1=s1+tab[groups[i][j]][0]
				s2=s2+tab[groups[i][j]][1]
				m=m+1
		l[i][0]=s1/m
		l[i][1]=s2/m
	for i in range(len(l)):
		print("the center of group {} is :".format(i+1))		
		print("%-18f" % l[i][0],end='')
		print("%-18f" % l[i][1],end='')
		print()
	erreur=0
	for i in range(len(groups)):
		for j in range(1,len(groups[0])):
			if(groups[i][j]!=-1):
				erreur=erreur+sqrt(((tab[groups[i][j]][0]-l[i][0])**2)+((tab[groups[i][j]][1]-l[i][1])**2))
	
	print(" standard error is  :{}".format(erreur))
	if(old_error==erreur):
		break
	old_error=erreur
pyplot.show()  


