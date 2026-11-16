import os
import re

# รองรับการซ่อนรหัสผ่าน: ถ้ามี pwinput ให้ใช้ ถ้าไม่มีให้ใช้ getpass จาก standard library
try:
    import pwinput
    def read_password(prompt: str) -> str:
        return pwinput.pwinput(prompt=prompt, mask="*")
except ImportError:
    import getpass
    def read_password(prompt: str) -> str:
        return getpass.getpass(prompt)


def is_valid_email(email: str) -> bool:
    """ตรวจสอบรูปแบบ Username ให้เป็นไปตามมาตรฐานอีเมล"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email.strip()))


def validate_password(password: str) -> tuple[bool, str]:
    """
    ตรวจสอบรหัสผ่านตามแนวทาง OWASP และ NIST SP 800-63B:
    1. นับความยาวตาม Unicode characters จริง (Python len() คืนค่า code points ไม่ใช่ byte)
    2. ความยาวขั้นต่ำ 15 ตัวอักษร
    3. ไม่บังคับความซับซ้อน (ตัวพิมพ์ใหญ่-เล็ก ตัวเลข สัญลักษณ์)
    4. รองรับรหัสผ่านยาวอย่างน้อย 64 ตัวอักษรขึ้นไป
    """
    char_count = len(password)

    if char_count < 15:
        return False, f"รหัสผ่านต้องมีความยาวอย่างน้อย 15 ตัวอักษร (ปัจจุบันมี {char_count} ตัวอักษร)"

    if char_count > 128:
        return False, f"รหัสผ่านยาวเกิน 128 ตัวอักษร (เพื่อป้องกัน DoS Attack, ปัจจุบันมี {char_count} ตัวอักษร)"

    return True, "รหัสผ่านผ่านเกณฑ์ความปลอดภัย OWASP"


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("============================================================")
    print("     ระบบตรวจสอบบัญชีผู้ใช้และรหัสผ่าน (OWASP Standard)     ")
    print("============================================================\n")

    max_attempts = 3
    for attempt in range(max_attempts):
        # 1. รับค่า Username (รูปแบบ Email)
        username = input("กรุณากรอก Username (รูปแบบ Email): ").strip()
        if not is_valid_email(username):
            print("❌ ผลลัพธ์: ไม่ผ่าน")
            print("เหตุผล: รูปแบบอีเมลไม่ถูกต้อง (ตัวอย่างที่ถูกต้อง: user@example.com)")
            left = max_attempts - 1 - attempt
            if left > 0:
                print(f"(เหลือโอกาสอีก {left} ครั้ง)\n")
                continue
            else:
                print(f"\nใส่ข้อมูลผิดเกิน {max_attempts} ครั้ง เด้งออกจากระบบ!")
                break

        # 2. รับค่า Password
        # ข้อสำคัญ: ห้ามใช้ .strip() เพราะจะตัดช่องว่าง (Space) หัวท้ายที่ผู้ใช้ตั้งใจกรอก
        # ใช้ .removesuffix() เพื่อตัดเฉพาะ \r และ \n ที่เกิดจากการกด Enter
        password_raw = read_password("กรุณาใส่รหัสผ่าน (ขั้นต่ำ 15 ตัวอักษร, อนุญาตช่องว่าง/ภาษาไทย/Emoji): ")
        password = password_raw.removesuffix("\r\n").removesuffix("\n")

        # 3. ตรวจสอบรหัสผ่าน
        is_valid, reason = validate_password(password)

        if is_valid:
            print("\n✅ ผลลัพธ์: ผ่าน")
            print(f"เหตุผล: {reason}")
            print(f"ยินดีต้อนรับเข้าสู่ระบบ: {username}")
            # ข้อกำหนดความปลอดภัย OWASP:
            # - "ห้าม" แสดงค่ารหัสผ่านที่ผู้ใช้กรอกออกมาซ้ำบนหน้าจอ
            # - "ห้าม" บันทึกรหัสผ่านลงไฟล์ใดๆ ทั้งสิ้น
            break
        else:
            left = max_attempts - 1 - attempt
            print("\n❌ ผลลัพธ์: ไม่ผ่าน")
            print(f"เหตุผล: {reason}")
            if left > 0:
                print(f"(เหลืออีก {left} ครั้ง)\n")
            else:
                print(f"\nใส่ข้อมูลผิดเกิน {max_attempts} ครั้ง เด้งออกจากระบบ!")


if __name__ == "__main__":
    main()
