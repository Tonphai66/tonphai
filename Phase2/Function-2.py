# 1. ฟังก์ชัน sayHello: รับพารามิเตอร์ 3 ตัว (time, username, age) เพื่อพิมพ์ข้อความทักทาย
def sayHello(time, username, age):  # parameter (ตัวรับค่าที่ส่งเข้ามาในฟังก์ชัน)
    print("สวัสดี ", time, username)
    print("ปีนี้คุณมีอายุ ", age, " ปี")

# 2. ฟังก์ชัน showTable: รับพารามิเตอร์ num (ตัวเลขแม่สูตรคูณ) เพื่อพิมพ์ตารางสูตรคูณ
def showTable(num):
    print(f"---แม่ {num}------")
    # วนลูปค่า i ตั้งแต่ 1 ถึง 12 สำหรับนำไปคูณ
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

# 3. ฟังก์ชัน saveEmployee: รับพารามิเตอร์ 3 ตัว (name, department, salary) เพื่อแสดงข้อมูลพนักงาน
def saveEmployee(name, department, salary):
    print(f"ชื่อ {name} , แผนก {department}")
    print(f"เงินเดือน {salary} บาท")
    print("-----------------------")

# (โค้ดส่วนนี้ถูกคอมเมนต์ไว้ เป็นตัวอย่างการเรียกใช้ฟังก์ชัน sayHello และ showTable)
# myTime = "ตอนเช้า"
# sayHello(myTime, "ก้อง", 30)  # ส่ง Arguments เข้าไปทำงานในฟังก์ชัน sayHello
# sayHello(myTime, "โจโจ้", 40)
# showTable(3)
# showTable(5)
# showTable(12)

# โค้ดส่วนที่เปิดใช้งานจริง: เรียกฟังก์ชัน saveEmployee พร้อมส่งข้อมูลพนักงานแต่ละคนเข้าไป
saveEmployee("ก้อง", "ไอที", 30000)
saveEmployee("นัด", "กราฟิก", 35000)
saveEmployee("โจ้", "การตลาด", 30000)