# Inheritance (การสืบทอดคุณสมบัติจากคลาสแม่ไปยังคลาสลูก)

# 1. สร้าง Parent Class (คลาสแม่ - Employee)
class Employee:
    # Class Variables (ตัวแปรส่วนกลางของบริษัท)
    __minSalary = 12000
    maxSalary = 50000
    companyName = "บริษัท XYZ จำกัด"
    
    # Constructor สำหรับรับค่าข้อมูลพนักงาน
    def __init__(self, name, salary, department):
        # Instance Variables
        self.__name = name
        self.__salary = salary
        self.__department = department

    # เมธอดสำหรับแสดงข้อมูลพนักงาน
    def _showData(self):
        print("ชื่อพนักงาน = " + self.__name)
        print("เงินเดือน = ", format(self.__salary))
        print("ตำแหน่ง = " + self.__department)


# 2. สร้าง Child Classes (คลาสลูกที่สืบทอดคุณสมบัติมาจาก Employee)

# คลาสลูก Accounting (ฝ่ายบัญชี)
class Accounting(Employee):
    __departmentName = "แผนกบัญชี"  # ตัวแปรเฉพาะของฝ่ายบัญชี
    
    def __init__(self):
        pass  # เว้นว่างไว้ก่อน (สามารถเรียกใช้ constructor ของแม่หรือเขียนเพิ่มภายหลังได้)


# คลาสลูก Programmer (แผนกพัฒนาระบบ)
class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"  # ตัวแปรเฉพาะของโปรแกรมเมอร์
    
    def __init__(self):
        pass


# คลาสลูก Sale (ฝ่ายขายสินค้า)
class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"  # ตัวแปรเฉพาะของฝ่ายขาย
    
    def __init__(self):
        pass


# --- ส่วนของการสร้างวัตถุ (Object) จากคลาสลูกต่างๆ ---

account = Accounting()       # สร้างวัตถุแทนแผนกบัญชี
programmer = Programmer()    # สร้างวัตถุแทนแผนกพัฒนาระบบ
sale = Sale()                # สร้างวัตถุแทนฝ่ายขายสินค้า