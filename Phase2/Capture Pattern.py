# กำหนดค่าตัวแปร service เป็น 10 เพื่อจำลองการเลือกหมายเลขบริการ
service = 10

# ใช้คำสั่ง match-case (Pattern Matching) สำหรับตรวจสอบค่าในตัวแปร service
match service:
    # Literal Pattern: ถ้าค่าใน service เท่ากับ 1
    case 1:
        print("ฝากเงิน")
        
    # Literal Pattern: ถ้าค่าใน service เท่ากับ 2
    case 2:
        print("ถอนเงิน")
        
    # Capture Pattern: ถ้าค่าใน service ไม่ตรงกับเคส 1 หรือ 2 เลย 
    # ระบบจะทำการ "จับภาพ" (Capture) ค่าที่ส่งเข้ามาเก็บไว้ในตัวแปรชื่อ service 
    # เพื่อให้นำค่าดังกล่าวมาใช้งานต่อในบล็อกคำสั่งด้านล่างได้ทันที
    case service:  # นำค่าตัวแปรมาใช้ต่อ
        print(f"ไม่มีบริการหมายเลข {service} ในระบบ กรุณาทำรายการใหม่อีกครั้ง")