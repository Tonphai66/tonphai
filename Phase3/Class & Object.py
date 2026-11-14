# ฟังก์ชั่นเสริม / คลาสหลักสำหรับพนักงาน
class Employee:
    
    # Constructor สำหรับรับค่าข้อมูลพนักงานและกำหนดให้กับ Attributes
    def __init__(self, name, salary, department):
        self.name = name              # ชื่อพนักงาน
        self.salary = salary          # เงินเดือน
        self.department = department  # แผนก/ตำแหน่ง

    # เมธอดสำหรับแสดงข้อมูลของพนักงาน
    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))


# --- การสร้างวัตถุ (Object / Instance) จากคลาส Employee ---
obj1 = Employee("ก้อง", 20000, "บัญชี")
obj2 = Employee("โจโจ้", 40000, "โปรแกรมเมอร์")
obj3 = Employee("นัด", 100000, "ผู้จัดการ")

# ตรวจสอบและแสดงผลว่า obj1 ถูกสร้างมาจากคลาสอะไร
# คำสั่ง obj1.__class__ จะคืนค่าเป็นข้อมูลคลาสต้นทาง (ในที่นี้จะแสดงผลเป็น <class '__main__.Employee'>)
print(obj1.__class__)