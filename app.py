from flask import Flask, render_template, request
import mylib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
  

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/myid')
def myid():
 return """    <html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>แถบเมนูตัวอย่าง</title>
    <style>
        /* สไตล์สำหรับแถบเมนู */
        .navbar {
            /* กำหนดพื้นหลังของแถบเมนู */
            background-color: #333;
            /* ลบระยะขอบและช่องว่างภายนอก */
            margin: 0;
            padding: 0;
            /* ใช้ Flexbox เพื่อจัดเรียงปุ่มในแนวนอน */
            display: flex;
            /* ให้แถบเมนูติดอยู่ด้านบนสุดของหน้าจอ */
            position: fixed;
            top: 0;
            width: 100%;
            /* เพิ่มเงาเล็กน้อยเพื่อให้ดูมีมิติ */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            /* จัดเรียงปุ่มไปทางซ้าย */
            justify-content: flex-start;
            z-index: 1000; /* ทำให้แถบเมนูอยู่ด้านบนสุดขององค์ประกอบอื่น ๆ */
        }

        /* สไตล์สำหรับปุ่ม/ลิงก์ในแถบเมนู */
        .navbar a {
            /* กำหนดสีข้อความเป็นสีขาว */
            color: white;
            /* จัดข้อความให้อยู่ตรงกลางของปุ่ม */
            text-align: center;
            /* เพิ่มช่องว่างภายในปุ่ม */
            padding: 14px 20px;
            /* ลบเส้นใต้ลิงก์ */
            text-decoration: none;
            /* กำหนดขนาดตัวอักษร */
            font-size: 17px;
            /* เปลี่ยนรูปแบบการแสดงผลเป็นแบบบล็อกเพื่อให้ควบคุมง่ายขึ้น */
            display: block;
            /* ทำให้การเปลี่ยนสีเมื่อเมาส์ชี้ดูนุ่มนวลขึ้น */
            transition: background-color 0.3s, color 0.3s;
            /* เพิ่มระยะห่างระหว่างปุ่มเล็กน้อย */
            margin-right: 1px;
        }

        /* สไตล์เมื่อนำเมาส์ไปชี้ที่ปุ่ม */
        .navbar a:hover {
            /* เปลี่ยนสีพื้นหลังเมื่อเมาส์ชี้ */
            background-color: #575757;
            /* เปลี่ยนสีข้อความเมื่อเมาส์ชี้ */
            color: #ffc107;
        }

        /* สไตล์สำหรับปุ่มที่ 'Active' (ถ้าต้องการเน้นปุ่มที่กำลังใช้งาน) */
        .navbar a.active {
            background-color: #04AA6D;
            color: white;
        }
    </style>
</head>
<body>

<div class="navbar">
    <a href='/' >หน้าแรก</a>
    <a href="/tech">เทคโนโลยีที่สนใจ</a>
    <a href="/myid">รหัสนักศึกษา</a>
    <a href="/draw">Draw</a>
</div>
    <h1 style="
        font-family: 'Arial Black', sans-serif;
        font-size: 40px;
        color: #d9534f; /* A bold red color */
        text-align: center;
        margin-top: 50px;
    ">
        STUDENT ID<br>
        รหัสนักศึกษา คือ<br>
        68130489
    </h1>

    """
    

@app.route('/draw')
def draw2():
    return render_template('draw.html')

@app.route('/run', methods=['POST'])
def run():
    x = 'x'
    y = int(request.form['turn'])
    results = [mylib.myfunc(x, i) for i in range(1, y + 1)]
    return render_template('result.html', x=x, y=y, results=results)


# Assignment เพิ่ม path /sum/xx/yy

@app.route('/sum/<xx>/<yy>') 
def sum_number(xx,yy):
    try:                           # try-except  ใช้ เพื่อ ตรวจสอบข้อผิดพลาด (Error) กรณีใส่ค่าผิด
        number_xx = int(xx)
        number_yy = int(yy)
        result_number = number_xx + number_yy
        return "The result of sum between " + str(number_xx) + " and " + str(number_yy) + " is " + str(result_number)
    except(ValueError,TypeError):       #  ValueError แปลงค่าผิดประเภท เช่น int("abc")   TypeError	ใช้ชนิดข้อมูลไม่ถูกต้อง	"5"+3
        return "You are using miss data type for operation"

# Assignment เพิ่ม path /concat/xx/yy
@app.route('/concat/<xx>/<yy>')
def concat(xx, yy):
    result_concat = xx + yy
    return "The result of concatenate between " + str(xx) + " and " + str(yy) + " is " + str(result_concat)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)