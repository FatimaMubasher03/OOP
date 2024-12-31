from datetime import datetime

x = datetime.now()
print(x)
y = datetime(2020, 5, 17)
print(y)
z = x.strftime("%d-%b-%Y")
print(z)
print("====================================")
# # https://www.w3schools.com/python/python_datetime.asp

class Address:
    def __init__(self,houseno,street,area,city):
        self.houseno=houseno
        self.street=street
        self.area=area
        self.city=city

    def __str__(self):
        astr='('
        astr+=str(self.houseno)
        astr+=','
        astr+=str(self.street)
        astr+=','
        astr+=str(self.area)
        astr+=','
        astr+=str(self.city)
        astr+=')'
        return astr
    
    def get_houseno(self):
        return self.houseno
    
    def set_houseno(self,hn):
        self.houseno =hn

    def get_street(self):
        return self.street
    
    def set_street(self,s):
        self.street =s

    def get_area(self):
        return self.area
    
    def set_area(self,a):
        self.area =a

    def get_city(self):
        return self.city
    
    def set_city(self,c):
        self.city =c







class BillItem:
    def __init__(self, particular, rate, quantity):
        self.particular = particular
        self.rate = rate
        self.quantity = quantity

    def __str__(self):
        bstr='('
        bstr+=str(self.particular)
        bstr+=','
        bstr+=str(self.rate)
        bstr+=','
        bstr+=str(self.quantity)
        bstr+=')'
        return bstr
    
    def get_particular(self):
        return self.particular
    
    def set_particular(self,p):
        self.particular =p

    def get_rate(self):
        return self.rate
    
    def set_rate(self,r):
        self.rate =r

    def get_quantity(self):
        return self.quantity
    
    def set_quantity(self,q):
        self.quantity =q
    





class Bill:
    def __init__(self, billno, billdate, name, address, items):
        self.billno = billno
        self.billdate = billdate
        self.name = name
        self.address = address
        self.items = items


    def get_billno(self):
        return self.billno
    
    def set_billno(self,bn):
        self.billno =bn

    def get_billdate(self):
        return self.billdate
    
    def set_billdate(self,bd):
        self.billdate =bd

    def get_name(self):
        return self.name
    
    def set_name(self,n):
        self.name =n

    def get_address(self):
        return self.address
    
    def set_address(self,ad):
        self.address =ad


    def __str__(self):
        total = 0
        rstr = ''
        rstr = 'MOBILO' +'\n'
        rstr += 'Mobile City' +'\n'
        rstr += 'Deals in all kinds of Mobile sets and Accsessories' + '\n'
        rstr += 'Cell No: 0321-0000000' + '\n'
        rstr += 'CASHMENO' + '\n' 
        rstr += 'No:' + str(self.billno) + '\n'
        rstr += 'Date:' + self.billdate.strftime("%d-%b-%Y") + '\n'
        rstr += 'Costumer Name:' + str(self.name) + '\n'
        rstr += 'Coustumer Address:' + str(self.address) +'\n'
        rstr += 'QTY\t\tParticulars\t\tRate\t\tAmount\n'

        for item in self.items:
            total += item.quantity * item.rate
            rstr += f'{item.particular.ljust(25)}{str(item.rate).ljust(10)}{str(item.quantity).ljust(8)}{str(item.quantity * item.rate).ljust(9)}\n'


        rstr +=  '_______________________\t____\t\t___\t\t_______\n'
        rstr += f'Total\t\t\t\t\t\t\t{total}\n'
        rstr += 'Signature:______________________\n'
        rstr += 'Address: Basement # 2, Allahwala Plaza, Markaz K9, Islamabad'
        return rstr
    
    
def main():
    totalbill= Bill(12345, datetime.now(), 'Fatima', Address(212, 2, 'Johar Town', 'Lahore'),[BillItem ('Redmi Phone' ,35000, 1), BillItem ('Headphone', 12000, 1)])
    print(totalbill)
    
if __name__ == '__main__':
    main()
