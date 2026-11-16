# Security & Validation Tools (OWASP & NIST Standards)

ชุดเครื่องมือและสคริปต์สำหรับการตรวจสอบความปลอดภัยของบัญชีผู้ใช้ รหัสผ่าน และเบอร์โทรศัพท์ พัฒนาด้วยภาษา **Rust** และ **Python** โดยยึดตามแนวทางมาตรฐานความปลอดภัย **OWASP** และ **NIST SP 800-63B**

---

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

| ไฟล์ | ภาษา | รายละเอียด |
| :--- | :---: | :--- |
| [`main.rs`](main.rs) | Rust | ระบบตรวจสอบ Username (Email) และรหัสผ่านตามมาตรฐาน **OWASP / NIST SP 800-63B** |
| [`joker.py`](joker.py) | Python | ระบบตรวจสอบแบบเดียวกับ `main.rs` เวอร์ชัน Python (รองรับการซ่อนรหัสผ่านขณะพิมพ์) |
| [`password_checker.py`](password_checker.py) | Python | ตรวจสอบรหัสผ่านตามเกณฑ์ดั้งเดิม (ความยาวขั้นต่ำ 9 ตัว, พิมพ์ใหญ่, เล็ก, ตัวเลข, อักขระพิเศษ) |
| [`phone_lookup.py`](phone_lookup.py) | Python | ตรวจสอบและค้นหาข้อมูลหมายเลขโทรศัพท์สากล (ผู้ให้บริการ, ประเทศ, เขตเวลา) |

---

## 🛡️ มาตรฐานความปลอดภัยที่นำมาใช้ (OWASP & NIST SP 800-63B)

ในไฟล์ `main.rs` และ `joker.py` ได้ออกแบบตามข้อกำหนดความปลอดภัยยุคใหม่:
1. **ความยาวรหัสผ่าน (Password Length):**
   - ความยาวขั้นต่ำ **15 ตัวอักษร** เพื่อป้องกันการ Brute-force
   - รองรับความยาวสูงสุด **128 ตัวอักษร** เพื่อป้องกัน DoS Attack ในขั้นตอนการคำนวณ Cryptographic Hash
2. **นับตัวอักษรแบบ Unicode จริง (Character-based):**
   - รองรับตัวอักษรภาษาไทย, ช่องว่าง (Space), และ Emoji โดยนับตาม Unicode Scalar Values จริง ไม่ใช่นับ Byte
3. **ไม่บังคับความซับซ้อนที่ไร้ประโยชน์ (No Composition Rules):**
   - ไม่บังคับว่าต้องมีตัวพิมพ์ใหญ่/ตัวเลข/สัญลักษณ์ตามคำแนะนำของ NIST SP 800-63B เพราะมักทำให้ผู้ใช้ตั้งรหัสผ่านที่เดาง่าย เช่น `P@ssword1`
4. **ความปลอดภัยในการป้อนข้อมูล:**
   - ไม่แสดงรหัสผ่านซ้ำบนหน้าจอ และไม่มีการบันทึก (Log) รหัสผ่าน
   - จำกัดจำนวนครั้งในการกรอกผิดได้ไม่เกิน 3 ครั้ง

---

## 🚀 วิธีการใช้งาน (Getting Started)

### 1. การรันโปรแกรมภาษา Rust (`main.rs`)

#### สิ่งที่ต้องติดตั้ง:
- **Rust & Cargo** (ติดตั้งผ่าน `winget install Rustlang.Rustup` หรือดาวน์โหลดจาก [rustup.rs](https://rustup.rs))

#### วิธีรัน:
```powershell
# คอมไพล์ไฟล์ main.rs
rustc main.rs

# รันโปรแกรม (Windows)
.\main.exe
```

---

### 2. การรันโปรแกรมภาษา Python

#### สิ่งที่ต้องติดตั้ง:
- **Python 3.10+**
- ติดตั้งไลบรารีเสริม (ถ้าต้องการใช้งานฟังก์ชันเสริม):
```powershell
# สำหรับซ่อนรหัสผ่านเป็นดอกจัน (*) ใน joker.py
pip install pwinput

# สำหรับ phone_lookup.py
pip install phonenumbers
```

#### วิธีรันแต่ละไฟล์:

- **รันระบบตรวจสอบรหัสผ่าน OWASP (`joker.py`):**
  ```powershell
  python joker.py
  ```

- **รันตัวตรวจสอบเงื่อนไขรหัสผ่านดั้งเดิม (`password_checker.py`):**
  ```powershell
  python password_checker.py
  ```

- **รันระบบตรวจสอบเบอร์โทรศัพท์ (`phone_lookup.py`):**
  ```powershell
  python phone_lookup.py
  ```
  *(ตัวอย่างเบอร์ที่กรอก: `+66812345678`)*

---

## 👨‍💻 ผู้พัฒนา (Author)
- GitHub: [@YY1U](https://github.com/YY1U)
