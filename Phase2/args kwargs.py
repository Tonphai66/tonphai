# args / kwargs
# ข้อมูลแบบลำดับ *args
# ข้อมูลแบบกำหนดชื่อ **kwargs

# สร้าง Function โดยใช้ **kwargs เพื่อรับค่าพารามิเตอร์ในรูปแบบ Dictionary (Keyword Arguments)
def saveEmployee(**kwargs):  # dictionary
    # ดึงค่าจาก Dictionary มาแสดงผลโดยอ้างอิงจากชื่อคีย์ เช่น kwargs["name"]
    print(f"ชื่อพนักงาน {kwargs['name']} , แผนก {kwargs['department']}")
    print(f"เงินเดือน {kwargs['salary']} บาท")
    print(f"ที่อยู่ {kwargs['country']} ")
    print("------------------------")


# เรียกใช้งานฟังก์ชัน โดยส่งค่า arguments แบบกำหนดชื่อ (key=value) 
# ซึ่งสามารถสลับตำแหน่งหรือเพิ่มข้อมูลได้อิสระ เพราะข้อมูลจะถูกเก็บเป็น Dictionary
saveEmployee(name="ก้อง", department="ไอที", salary=30000, country="ภูเก็ต")
saveEmployee(name="นัด", department="กราฟิก", salary=35000, country="อุดรธานี")
saveEmployee(name="โจ้", department="การตลาด", salary=50000, country="น่าน")
