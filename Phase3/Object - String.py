class Employee:
    # Class Variables (ตัวแปรส่วนกลางของคลาส)
    __minSalary = 12000
    maxSalary = 50000
    companyName = "บริษัท XYZ จำกัด"
    
    # Constructor สำหรับรับค่าข้อมูลพนักงานพื้นฐาน
    def __init__(self, name, salary, department):
        # Instance Variables (แบบ Private และ Protected)
        self.__name = name              # ชื่อพนักงาน (Private)
        self.__salary = salary          # เงินเดือน (Private)
        self._department = department   # แผนก/ตำแหน่ง (Protected)

    # เมธอดสำหรับแสดงรายละเอียดข้อมูลพนักงาน
    def _showData(self):
        print("ชื่อพนักงาน = " + self.__name)
        print("เงินเดือน = ", format(self.__salary))
        print("ตำแหน่ง = " + self._department)

    # เมธอดคำนวณรายได้ต่อปี (เงินเดือน x 12 เดือน)
    def _getIncome(self):
        return self.__salary * 12

    # เมธอดพิเศษ __str__ สำหรับแปลง Object ให้กลายเป็น String เมื่อถูกเรียกผ่าน print()
    def __str__(self):
        return ("ขื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {}".format(
            self.__name, self._department, self.__salary
        ))

# 1. คลาส Accounting (ฝ่ายบัญชี)
class Accounting(Employee):
    __departmentName = "แผนกบัญชี"  # ชื่อแผนกเฉพาะของฝ่ายบัญชี
    
    def __init__(self, name, salary):
        # ใช้ super() เรียกใช้ __init__ ของคลาสแม่ พร้อมส่งชื่อ เงินเดือน และชื่อแผนกขึ้นไปกำหนดค่า
        super().__init__(name, salary, self.__departmentName)
        

# 2. คลาส Programmer (แผนกพัฒนาระบบ)
class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"  # ชื่อแผนกเฉพาะของโปรแกรมเมอร์
    
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        

# 3. คลาส Sale (ฝ่ายขายสินค้า)
class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"  # ชื่อแผนกเฉพาะของฝ่ายขาย
    
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)

# สร้างออบเจกต์พนักงานฝ่ายบัญชี และสั่งพิมพ์ข้อมูลผ่านเมธอด __str__
account = Accounting("ก้อง", 10000)
print(account.__str__())  # ผลลัพธ์: ขื่อพนักงาน = ก้อง , แผนก = แผนกบัญชี , เงินเดือน = 10000

# สร้างออบเจกต์พนักงานโปรแกรมเมอร์
programmer = Programmer("โจโจ้", 40000)
print(programmer.__str__())  # ผลลัพธ์: ขื่อพนักงาน = โจโจ้ , แผนก = แผนกพัฒนาระบบ , เงินเดือน = 40000

# สร้างออบเจกต์พนักงานฝ่ายขาย
sale = Sale("นัท", 35000)
print(sale.__str__())  # ผลลัพธ์: ขื่อพนักงาน = นัท , แผนก = ฝ่ายขายสินค้า , เงินเดือน = 35000