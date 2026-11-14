# Encapsulation (การห่อหุ้มข้อมูลและการกำหนดการเข้าถึง)
class Employee:
    
    def __init__(self, name, salary, department):
        # กำหนดระดับการเข้าถึงของตัวแปร (Attributes)
        self._name = name          # Protected Attribute (มีขีดล่าง 1 ตัว)
        self.__salary = salary      # Private Attribute (มีขีดล่าง 2 ตัว ซ่อนข้อมูลไว้ภายใน)
        self.__department = department # Private Attribute
        
        # เรียกใช้งาน Private Method ภายใน Constructor ทันทีที่มีการสร้าง Object
        self.__showData()

    # #private method (เมธอดส่วนตัวที่มีขีดล่างคู่ ทำให้ภายนอกคลาสเรียกใช้งานตรงๆ ไม่ได้)
    def __showData(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self.__department))


# --- การสร้างวัตถุ (Object / Instance) ---
obj1 = Employee("ก้อง", 20000, "บัญชี")

# ตัวอย่างการพยายามแก้ไขค่าแอตทริบิวต์จากภายนอกคลาส
obj1._name = "โจโจ้"        # Protected สามารถแก้ไขภายนอกได้ (แต่ไม่แนะนำตามหลัก OOP)
obj1.__salary = 40000       # Private ไม่สามารถแก้ไขค่าภายในคลาสโดยตรงแบบนี้ได้ (จะเป็นการสร้างแอตทริบิวต์ใหม่ขึ้นมาแทน ไม่ได้เปลี่ยนค่า __salary ข้างใน)
obj1.__department = "ฝ่ายขาย" # Private เช่นเดียวกัน