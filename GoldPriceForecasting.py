import numpy as np

x=[]
y=[]
j=1

file=open("GPrice.txt")

for i in file:
    i=i.split(" ")
    x.append(j)
    j+=1
    y.append(float(i[2]))

sumx=np.sum(x)
sumy=np.sum(y)
sumx2=0
sumy2=0
sumxy=0

for i in range(len(x)):
    sumx2+=x[i]*x[i]
    sumy2+=y[i]*y[i]
    sumxy+=x[i]*y[i]
    
div=(len(x)*sumx2)-(sumx*sumx)
b0=((sumy*sumx2)-(sumxy*sumx))/div
b1=((sumxy*len(x))-(sumy*sumx))/div

tt=[]
st=[]

for i in range(len(x)):
    temp=(b1*i)+b0
    tt.append(temp)

for i in range(len(x)):
    temp=y[i]/tt[i]
    st.append(temp)

mon=0
tues=0
wed=0
thurs=0
fri=0
sat=0
sun=0

for i in range(len(x)):
    if x[i]%7==1:
        sun+=st[i]
    elif x[i]%7==2:
        mon+=st[i]
    elif x[i]%7==3:
        tues+=st[i]
    elif x[i]%7==4:
        wed+=st[i]
    elif x[i]%7==5:
        thurs+=st[i]
    elif x[i]%7==6:
        fri+=st[i]
    elif x[i]%7==0:
        sat+=st[i]

sun=sun/7
mon=mon/7
tues=tues/7
wed=wed/7
thurs=thurs/7
fri=fri/7
sat=sat/7

nor=mon+tues+wed+thurs+fri+sat+sun

mon=(mon/nor)*7
tues=(tues/nor)*7
wed=(wed/nor)*7
thurs=(thurs/nor)*7
fri=(fri/nor)*7
sat=(sat/nor)*7
sun=(sun/nor)*7

print('\n----------FORECASTS------------')
print('\n3-Feb-2019 : ',((b1*71)+b0)*sun)
print('\n4-Feb-2019 : ',((b1*72)+b0)*mon)
print('\n5-Feb-2019 : ',((b1*73)+b0)*tues)
print('\n6-Feb-2019 : ',((b1*74)+b0)*wed)
print('\n7-Feb-2019 : ',((b1*75)+b0)*thurs)
print('\n8-Feb-2019 : ',((b1*76)+b0)*fri)
print('\n9-Feb-2019 : ',((b1*77)+b0)*sat)
