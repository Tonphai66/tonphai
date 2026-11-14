# para + return function
# ฟังก์ชันสำหรับตรวจสอบว่าเป็นเลขคู่หรือเลขคี่ (รับพารามิเตอร์ 1 ตัว และ return ผลลัพธ์กลับไป)
def checkNumber(number):
    # ตรวจสอบว่าหาร 2 ลงตัวหรือไม่ (เศษเหลือเป็น 0)
    if number % 2 == 0:
        return "เลขคู่"
    else:
        return "เลขคี่"


# ฟังก์ชันสำหรับหาผลรวม (ใช้ *data หรือ *args เพื่อรับพารามิเตอร์หลายตัวในรูปแบบ Tuple)
def summation(*data):
    total = 0  # ตัวแปรเก็บผลรวมเริ่มต้นเป็น 0
    
    # วนลูปหยิบข้อมูลแต่ละตัวใน Tuple มาบวกสะสมเข้ากับ total
    for item in data:
        total += item
        
    return total  # ส่งค่าผลรวมทั้งหมดกลับออกไป


# ตัวอย่างการเรียกใช้งานฟังก์ชัน checkNumber (ถูกคอมเมนต์ไว้)
# result = checkNumber(13)
# print("ผลลัพธ์ = ", result)

# ตัวอย่างการเรียกใช้งานฟังก์ชัน summation (ส่งค่าตัวเลขหลายๆ ตัวเข้าไปคำนวณ)
print(summation(10, 20))  # ผลลัพธ์: 30
print(summation(10, 20, 30, 40, 50))  # ผลลัพธ์: 150