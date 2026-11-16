# รับค่า username และ password จากผู้ใช้
username = input("Enter username: ")
password = input("Enter password: ")

# กำหนดชุดอักขระพิเศษตามโจทย์
special_chars = "!@#$%^&*()-_=+[]{};:,.?"

# ตรวจสอบเงื่อนไขทั้ง 5 ข้อ
cond1 = len(password) >= 9
cond2 = any(c.isupper() for c in password)
cond3 = any(c.islower() for c in password)
cond4 = any(c.isdigit() for c in password)
cond5 = any(c in special_chars for c in password)

# แสดงผลแยกตามแต่ละเงื่อนไข
print(f"\nผลการตรวจสอบสำหรับผู้ใช้: {username}")
print(f"1. ความยาวอย่างน้อย 9 ตัวอักษร: {'PASS' if cond1 else 'FAIL'}")
print(f"2. มีตัวอักษรพิมพ์ใหญ่อย่างน้อย 1 ตัว: {'PASS' if cond2 else 'FAIL'}")
print(f"3. มีตัวอักษรพิมพ์เล็กอย่างน้อย 1 ตัว: {'PASS' if cond3 else 'FAIL'}")
print(f"4. มีตัวเลขอย่างน้อย 1 ตัว: {'PASS' if cond4 else 'FAIL'}")
print(f"5. มีอักขระพิเศษอย่างน้อย 1 ตัว: {'PASS' if cond5 else 'FAIL'}")

# สรุปผลรวม
overall = cond1 and cond2 and cond3 and cond4 and cond5
print("-" * 40)
print(f"สรุปผลรวม: {'PASS' if overall else 'FAIL'}")
