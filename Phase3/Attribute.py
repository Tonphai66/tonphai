# การสร้าง class (พิมพ์เขียวสำหรับสร้างวัตถุ)
class Employee:
    
    # 1. สร้าง Method สำหรับรับค่าข้อมูลพนักงานและเก็บไว้ใน Attribute ของวัตถุนั้นๆ
    def detail(self, name, salary, department):
        self.name = name              # เก็บชื่อพนักงาน
        self.salary = salary          # เก็บเงินเดือนพนักงาน
        self.department = department  # เก็บตำแหน่งพนักงาน

    # 2. สร้าง Method สำหรับแสดงข้อมูลพนักงานที่ถูกเก็บไว้ในวัตถุ
    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))


# --- การสร้างวัตถุ (Object / Instance) และกำหนดข้อมูลผ่าน Method detail ---

# สร้างวัตถุตัวที่ 1 (obj1) และกำหนดข้อมูลพนักงานคนแรก
obj1 = Employee()
obj1.detail("ก้อง", 50000, "บัญชี")

# สร้างวัตถุตัวที่ 2 (obj2) และกำหนดข้อมูลพนักงานคนที่สอง
obj2 = Employee()
obj2.detail("โจโจ้", 40000, "โปรแกรมเมอร์")

# สร้างวัตถุตัวที่ 3 (obj3) และกำหนดข้อมูลพนักงานคนที่สาม
obj3 = Employee()
obj3.detail("นัด", 100000, "ผู้จัดการ")


# --- การเรียกใช้งาน Method เพื่อแสดงผลข้อมูล ---

# สั่งให้ obj1 แสดงข้อมูลของตัวเองทางหน้าจอ
obj1.showData()

# สั่งให้ obj2 แสดงข้อมูลของตัวเองทางหน้าจอ
obj2.showData()

# (หมายเหตุ: obj3 มีการสร้างและใส่ข้อมูลไว้แล้ว แต่ในรูปยังไม่ได้เรียกใช้ obj3.showData())