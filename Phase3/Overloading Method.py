# Overloading และ Inheritance / Method Overriding / __str__
class Employee:
    # Class Variables (ตัวแปรระดับคลาส)
    __minSalary = 12000
    maxSalary = 50000
    companyName = "บริษัท XYZ จำกัด"
    
    def __init__(self, name, salary, department):
        # Instance Variables (แบบ Private)
        self.__name = name
        self.__salary = salary
        self.__department = department
        
    # เมธอดแสดงรายละเอียดข้อมูลพนักงาน
    def _showData(self):
        print("ชื่อพนักงาน = " + self.__name)
        print("เงินเดือน = ", format(self.__salary))
        print("ตำแหน่ง = " + self.__department)

    # เมธอดคำนวณรายได้ต่อปี (รองรับการใส่โบนัสและค่าล่วงเวลา โดยกำหนดค่าเริ่มต้นเป็น 0)
    def _getIncome(self, bonus=0, overtime=0):
        return (self.__salary * 12) + bonus + overtime

    # เมธอดพิเศษ __str__ สำหรับแปลง Object เป็น String เมื่อสั่ง print()
    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {}".format(
            self.__name, self.__department, self.__salary
        ))


# 1. คลาสลูก Accounting (ฝ่ายบัญชี) สืบทอดจาก Employee
class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    
    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.__age = age  # เพิ่ม Attribute เฉพาะของแผนกบัญชี
        
    def _showData(self):
        super()._showData()
        print("อายุ = " + str(self.__age))
        print("##################")
        
    def __str__(self):
        return (super().__str__() + " , อายุ = {} ปี".format(self.__age))


# 2. คลาสลูก Programmer (แผนกพัฒนาระบบ) สืบทอดจาก Employee
class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.__exp = experience  # ประสบการณ์ทำงาน
        self.__skill = skill      # ทักษะความสามารถ
        
    def _showData(self):
        super()._showData()
        print("ประสบการณ์ = " + str(self.__exp))
        print("ทักษะ = " + self.__skill)
        print("##################")
        
    def __str__(self):
        return (super().__str__() + " , ประสบการณ์ = {} ปี , ทักษะ = {}".format(
            self.__exp, self.__skill
        ))


# 3. คลาสลูก Sale (ฝ่ายขายสินค้า) สืบทอดจาก Employee
class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.__area = area  # พื้นที่รับผิดชอบ
        
    def _showData(self):
        super()._showData()
        print("พื้นที่รับผิดชอบ = " + self.__area)
        print("##################")
        
    def __str__(self):
        return (super().__str__() + " , พื้นที่รับผิดชอบ = {}".format(self.__area))


# --- ส่วนของการสร้างวัตถุ (Object) และการทดสอบเรียกใช้งาน ---

# สร้างออบเจกต์ฝ่ายบัญชี และคำนวณรายได้ต่อปี (บวกโบนัส 3,000 บาท)
account = Accounting("ก้อง", 10000, 30)
print("บัญชี รายได้ต่อปี = " + str(account._getIncome(3000)))

# สร้างออบเจกต์โปรแกรมเมอร์ และคำนวณรายได้ต่อปี (บวกโบนัส 10,000 และ OT 500 บาท)
programmer = Programmer("โจโจ้", 40000, 2, "พัฒนาเกม")
print("โปรแกรมเมอร์ รายได้ต่อปี = " + str(programmer._getIncome(10000, 500)))

# สร้างออบเจกต์ฝ่ายขาย และคำนวณรายได้ต่อปี (ใช้ค่าเริ่มต้น โบนัส=0, OT=0)
sale = Sale("นัด", 35000, "เชียงใหม่")
print("ฝ่ายขาย รายได้ต่อปี = " + str(sale._getIncome()))