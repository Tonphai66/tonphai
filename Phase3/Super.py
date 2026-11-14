# Super (การใช้งานฟังก์ชัน super() เพื่อเรียกใช้งาน Constructor ของคลาสแม่)
class Employee:
    # Class Variables (ตัวแปรส่วนกลางของบริษัท)
    __minSalary = 12000
    maxSalary = 50000
    companyName = "บริษัท XYZ จำกัด"
    
    # Constructor ของคลาสแม่ สำหรับรับค่าข้อมูลพนักงาน 3 ตัว
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


# 1. คลาสลูก Accounting (ฝ่ายบัญชี) สืบทอดจาก Employee
class Accounting(Employee):
    __departmentName = "แผนกบัญชี"  # ชื่อแผนกเฉพาะของฝ่ายบัญชี
    
    def __init__(self, name, salary):
        # ใช้ super() เรียก __init__ ของคลาสแม่ Employee 
        # เพื่อส่งชื่อ, เงินเดือน และดึงชื่อแผนก (__departmentName) ไปกำหนดค่าให้คลาสแม่
        super().__init__(name, salary, self.__departmentName)


# 2. คลาสลูก Programmer (แผนกพัฒนาระบบ) สืบทอดจาก Employee
class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)


# 3. คลาสลูก Sale (ฝ่ายขายสินค้า) สืบทอดจาก Employee
class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)


# --- ส่วนของการสร้างวัตถุ (Object) จากคลาสลูกต่างๆ ---
# สังเกตว่าตอนสร้าง Object เราส่งแค่ชื่อกับเงินเดือนเข้าไป เพราะแผนกถูกจัดการอัตโนมัติผ่าน super() แล้ว
account = Accounting("ก้อง", 12000)
programmer = Programmer("โจโจ้", 40000)
sale = Sale("นัด", 35000)