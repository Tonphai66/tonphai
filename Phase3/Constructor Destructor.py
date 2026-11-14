# การสร้าง Constructor (__init__)
class Employee:
    
    # เมธอดพิเศษ __init__ (Constructor) จะถูกเรียกใช้โดยอัตโนมัติเมื่อสร้าง Object
    # ทำหน้าที่รับค่าพารามิเตอร์มาตั้งต้นให้กับ Attributes ของวัตถุตัวนั้นๆ
    def __init__(self, name, salary, department):
        self.name = name              # กำหนดค่าชื่อพนักงาน
        self.salary = salary          # กำหนดค่าเงินเดือน
        self.department = department  # กำหนดค่าตำแหน่ง/แผนก

    # เมธอดสำหรับแสดงข้อมูลพนักงาน
    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))


# --- การสร้างวัตถุ (Object / Instance) และการใช้งาน ---

# 1. สร้าง obj1 พร้อมส่งค่าข้อมูลเข้าไปผ่าน Constructor ทันที
obj1 = Employee("ก้อง", 20000, "บัญชี")

# ตัวอย่างการเข้าถึงและแก้ไขค่า Attribute ของ obj1 โดยตรงหลังจากสร้างเสร็จ
obj1.name = "ก้องรักสยาม"  # เปลี่ยนชื่อจาก "ก้อง" เป็น "ก้องรักสยาม"
obj1.salary = 70000      # เปลี่ยนเงินเดือนจาก 20,000 เป็น 70,000

# สั่งให้ obj1 แสดงข้อมูลล่าสุดทางหน้าจอ
obj1.showData()
print("-" * 25)

# 2. สร้าง obj2 พร้อมส่งข้อมูลพนักงานคนที่สองเข้าไปทาง Constructor
obj2 = Employee("โจโจ้", 40000, "โปรแกรมเมอร์")
obj2.showData()  # แสดงข้อมูลของ obj2 ทันที
print("-" * 25)

# 3. สร้าง obj3 พร้อมส่งข้อมูลพนักงานคนที่สามเข้าไปทาง Constructor
obj3 = Employee("นัด", 100000, "ผู้จัดการ")
obj3.showData()  # แสดงข้อมูลของ obj3 ทันที