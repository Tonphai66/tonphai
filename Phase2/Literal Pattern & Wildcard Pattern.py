# กำหนดค่าตัวแปร service เป็น 1 เพื่อจำลองการเลือกหมายเลขบริการ
service = 1

# ใช้คำสั่ง match-case (Pattern Matching) สำหรับตรวจสอบค่าในตัวแปร service
match service:
    # Literal Pattern: ถ้าค่าใน service เท่ากับ 1
    case 1:
        print("ฝากเงิน")  # แสดงข้อความฝากเงิน
        
    # Literal Pattern: ถ้าค่าใน service เท่ากับ 2
    case 2:
        print("ถอนเงิน")  # แสดงข้อความถอนเงิน
        
    # Literal Pattern: ถ้าค่าใน service เท่ากับ 3
    case 3:
        print("สอบถามยอดเงินคงเหลือ")  # แสดงข้อความสอบถามยอดเงิน
        
    # Wildcard Pattern (Default Case): ถ้าค่าใน service ไม่ตรงกับเคสด้านบนเลย
    case _:  
        print("หมายเลขบริการไม่ถูกต้อง")  # แจ้งเตือนว่าหมายเลขไม่ถูกต้อง