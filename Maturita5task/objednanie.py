food=open('Maturita5task/objednane_jedla.txt','r',encoding='utf-8')
dic={}
counter=0
temp=''
for i in food:
    orders=i.split(' ')
    orders=orders[1].strip('\n')
    counter+=1
    dic[orders]=dic.get(orders,0)+1
print('Total number of orders: '+str(counter))

for orders in dic:
    print('Code: '+orders, 'Number of orders: '+str(dic[orders]))
    if dic[orders]<20:
        temp=temp+orders+', '
temp=temp[:-2:]

if temp!='':
    print('Dishes: '+temp, 'have been order by less than 20 people')
else:
    print('All dishes have been ordered')