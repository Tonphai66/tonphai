# Class Variable (การใช้งานตัวแปรระดับคลาส)
class Employee:
    
    # Class Variables (ตัวแปรส่วนกลางของคลาส ใช้ร่วมกันทุก Object และทำเป็น Private ด้วย __)
    __minSalary = 12000
    __maxSalary = 50000
    __companyName = "บริษัท XYZ จำกัด"
    
    # Constructor สำหรับรับค่าข้อมูลพนักงาน
    def __init__(self, name, salary, department):
        # Instance Variables (ตัวแปรเฉพาะของแต่ละ Object ที่สร้างขึ้น)
        self.__name = name
        self.__salary = salary
        self.__department = department

    # Private Method สำหรับแสดงข้อมูลพนักงาน
    def _showData(self):
        print("ชื่อพนักงาน = " + self.__name)
        print("เงินเดือน = ", format(self.__salary))
        print("ตำแหน่ง = " + self.__department)


# --- ส่วนของการสร้างวัตถุและการเรียกใช้งาน ---

# สร้างวัตถุ obj1 พร้อมส่งข้อมูลพนักงานเข้าไป
obj1 = Employee("ก้อง", 20000, "บัญชี")

# ทดลองเรียกดู Class Variable ผ่านชื่อคลาสโดยตรง (เนื่องจากมีการทำ Name Mangling กับ __ ไว้ 
# ใน Python จริงๆ การเรียก Employee.__companyName ตรงๆ อาจต้องระวังเรื่อง Private Class Variable 
# แต่ในตัวอย่างเป็นการเรียกใช้งานเพื่อดึงค่าตัวแปรกลางของคลาสครับ)
print(Employee._companyName)