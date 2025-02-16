name=input('enter name-------')
mobile=int(input('mobile number_______'))
mail=input("e mail adress-----")
t=input("state and city------")
import csv

#menu driven programme
print('1.selling cars','2.colour of car','3.display the cars','4.payment')
choice=int(input('enter your choice (1-3)'))
if choice== 1:
with open("kcar.csv","w") as fl:
w=csv.writer(fl)
w.writerow(['car','price','milage','engine','seatings','bootspace','fuel','yrs'])
c=input("car name....")
price=int(input("price...."))
milage=int(input("milage....."))
engine=int(input("engine...."))
seatings= int(input("seats....."))
bootspace=int(input("bootspace....."))
fuel=input("fuel type....")
yrs=int(input("years...."))
rec=[car,price,milage,engine,seatings,bootspace,fuel,yrs]
w.writerow(rec)
print("car is sucessfully enlisted for selling")

if choice==2:
f1=open('customization.csv','w+')

print('_________________customization of car_____________________')
cChecker=False
while cChecker == False:
num=int(input("option 1.for exterior and 2.for interior"))
if num == 1:
entry = input('Please enter the exterior colour (press help to view list of acceptable colours): ')
elif num == 2:
entry = input('Please enter the interior colour (press help to view list of acceptable colours): ')
if entry.lower() == 'help':
record=(entry)
print('\nList of acceptable colours: ')
for row in entry:
print(row)
cChecker = True

if choice==3:
with open('kompalcar.csv', 'r') as csvFile:
readCSV = csv.reader(csvFile)
for rec in readCSV:
print(rec)
print('--------------------------\n')

if choice ==4:
num = 0
while True:
try:

DIN = int(input('Please enter the Dealer Inventory Number of the vehicle you would like to
purchase: '))
except ValueError:
print('Error!'); continue
if DIN<1000 or DIN>9999:
print('Error!'); continue
else:
break
with open('kompalcar.csv', 'r') as File:
read = csv.reader(File)
for row in read:
num+=1
if str(DIN) == row['inventory']:
print('\nVehicle: ', row['CAR'], row['NAME'] + ' Price:', row[' PRICE'])
while True:
try:
credit = int(input('Please enter your four digit credit card number: '))
except ValueError:
print('Error!')
continue
if credit<1000 or credit>9999:
print('Error!')
continue
else:
break
print('Congratulations! Enjoy your new vehicle!')
