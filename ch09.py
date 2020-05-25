class Car:
    def __init__(self):
        self.color = 0xFF0000
        self.wheel_size = 16
        self.displacement = 200
    def forward(self):
        pass
    def backward(self):
        pass
    def turn_left(self):
        pass
    def turn_right(self):
        pass

class InstanceVar:
    def __init__(self):
        self.text_list=[]
        
    def add(self,text):
        self.text_list.append(text)
    
    def print_list(self):
        print(self.text_list)

class ContactInfo:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def print_info(self):
        print(self.name)
        print(self.email)

class InstanceCounter:
    count = 0
    def __init__(self):
        InstanceCounter.count += 1

if __name__ == '__main__':
    my_car = Car()

    print("0x{:2X}".format(my_car.color))
    print(my_car.wheel_size)
    print(my_car.displacement)

    my_car.forward()
    my_car.bacward()

    a = InstanceVar
    a.add('a')
    a.print_list()

    dahyun = ContactInfo('우다현','wdh112139@ajou.ac.kr')
    dahyun.print_info()

