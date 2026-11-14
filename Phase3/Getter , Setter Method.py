# Getter Setter Method และการใช้งาน Private Attributes
class Employee:
    
    def __init__(self, name, salary, department):
        # Private Attributes (ขึ้นต้นด้วย __ สองตัว เพื่อซ่อนข้อมูล ป้องกันไม่ให้ภายนอกแก้ไขได้โดยตรง)
        self.__name = name
        self.__salary = salary
        self.__department = department

    # เมธอดสำหรับแสดงข้อมูล (เรียกใช้ผ่าน Getter ด้านล่าง)
    def _showData(self):
        print("ชื่อพนักงาน = " + self.getName())
        print("เงินเดือน = ", format(self.getSalary()))
        print("ตำแหน่ง = " + self.getDepartment())

    # --- Getter Methods (เมธอดสำหรับดึงค่า Private Attribute ออกมาใช้งาน) ---
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department

    # --- Setter Methods (เมธอดสำหรับแก้ไขหรือกำหนดค่าใหม่ให้กับ Private Attribute) ---
    def setName(self, newname):
        self.__name = newname

    def setSalary(self, newsalary):
        self.__salary = newsalary

    def setDepartment(self, department):
        self.__department = department


# --- ส่วนของการสร้างวัตถุ (Object) และการทดสอบใช้งาน ---
obj1 = Employee("ก้อง", 20000, "บัญชี")

# ทดลองเรียกใช้ Getter เพื่อดึงชื่อพนักงานออกมาแสดงผล
print(obj1.getName())  # ผลลัพธ์: ก้อง
