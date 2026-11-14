# การสร้าง class
class Employee:
    # สร้าง Method ชื่อ detail สำหรับจัดการข้อมูลและแสดงผลภายในคลาส
    def detail(self):
        # กำหนดค่า Attribute (คุณลักษณะ) ให้กับวัตถุกผ่าน self
        self.name = "ก้องรักสยาม"
        self.salary = 50000
        
        # แสดงผลข้อมูลชื่อพนักงานและเงินเดือน โดยใช้ฟังก์ชัน .format()
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))


# การสร้างวัตถุ (Object / Instance) จากคลาส Employee
emp1 = Employee()

# เรียกใช้งาน Method detail ผ่านวัตถุ emp1 เพื่อสั่งให้รันคำสั่งแสดงข้อมูลด้านใน
emp1.detail()