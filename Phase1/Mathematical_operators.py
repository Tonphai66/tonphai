# ตัวดำเนินการทางคณิตศาสตร์ (Arithmetic Operators) ใน Python

number1, number2 = (
    5,
    2,
)  # กำหนดค่าเริ่มต้นให้ตัวแปร number1 เป็น 5 และ number2 เป็น 2

print("ตัวเลขที่ 1 = ", number1)  # แสดงค่าของตัวแปร number1 ออกทางหน้าจอ
print("ตัวเลขที่ 2 = ", number2)  # แสดงค่าของตัวแปร number2 ออกทางหน้าจอ

# ส่วนการคำนวณและแสดงผลลัพธ์ด้วยตัวดำเนินการทางคณิตศาสตร์รูปแบบต่างๆ
print("=============")
print(
    "ผลบวก = ", number1 + number2
)  # นำค่า number1 มาบวกกับ number2 (5 + 2 ได้ 7)
print(
    "ผลลบ = ", number1 - number2
)  # นำค่า number1 มาลบด้วย number2 (5 - 2 ได้ 3)
print(
    "ผลคูณ = ", number1 * number2
)  # นำค่า number1 มาคูณกับ number2 (5 * 2 ได้ 10)
print(
    "ยกกำลัง = ", number1**number2
)  # นำค่า number1 มายกกำลังด้วย number2 (5 ยกกำลัง 2 ได้ 25)
print(
    "ผลหาร = ", number1 / number2
)  # นำค่า number1 มาหารด้วย number2 (ได้ผลลัพธ์เป็นทศนิยม: 5 / 2 ได้ 2.5)
print(
    "ผลหารไม่เอาจุดทศนิยม = ", number1 // number2
)  # หารปัดเศษทิ้ง / Floor Division (5 // 2 ได้ 2)
print(
    "เศษ = ", number1 % number2
)  # หาเศษจากการหาร / Modulus (5 หารด้วย 2 จะเหลือเศษ 1)