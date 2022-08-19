#!/usr/bin/python
import cgi, os
import cgitb
import xml.etree.ElementTree as et
import main as db


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>INPUT XML</title>
        </head>
        <body>""")
cgitb.enable()
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from file name to avoid
    # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open(fn, 'wb').write(fileitem.file.read())
    message = 'Файл "' + fn + '" успешно загружен'
else:
    message = 'Файл не загружен'
if message != 'Файл не загружен':
    tree = et.parse(fn)
    root = tree.getroot()
    connection = db.create_connection('db.sqlite')
    doctor = "select * from doctor"
    doctor = db.execute_read_query(connection, doctor)
    flag = 0
    for elem in root:
        list_doctor = []
        if elem.tag == "doctor":
            for subelem in elem:
                list_doctor.append(subelem.text)
            for index in range(0, len(list_doctor), 3):
                create_doctor = """INSERT INTO
                    doctor (name,post,work_exp)
                    VALUES
                    ('{}','{}','{}');
                    """.format(list_doctor[index], list_doctor[index + 1], list_doctor[index + 2])
                create_doctor = db.execute_query(connection, create_doctor)
print("""
<div class="body">
<div class="form"><h2>{}</h2></div>
<div class="form href"> <a href="../index.html">Главная страница</a></div>
</div>""".format(message))
print("""
<style>
body{margin:0;
background-color:#fff;}
  .body {
  align-items: center;
  background-color:#fff;
  margin-top:10%;

}
.href{margin:0 auto;
      margin-top:30px;
      display:flex;
      justify-content: center;
      }
.href a{color:white;
font-family: sans-serif;
text-decoration:none;}
.form {
  background-color: #15172b;
  border-radius: 20px;
  box-sizing: border-box;
  padding: 20px;
  width: 420px;
  color:white;
  font-family: sans-serif;
text-decoration:none;
margin:0 auto;
margin-bottom:20px;
}

.title {
  color: #eee;
  font-family: sans-serif;
  font-size: 36px;
  font-weight: 600;
  margin-top: 30px;
}

.subtitle {
  color: #eee;
  font-family: sans-serif;
  font-size: 16px;
  font-weight: 600;
  margin-top: 10px;
}

.input-container {
  height: 50px;
  position: relative;
  width: 100%;
}

.ic1 {
  margin-top: 40px;
}

.ic2 {
  margin-top: 30px;
}

.input {
  background-color: #303245;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: #eee;
  font-size: 18px;
  height: 100%;
  outline: 0;
  padding: 4px 20px 0;
  width: 100%;
}

.cut {
  background-color: #15172b;
  border-radius: 10px;
  height: 20px;
  left: 20px;
  position: absolute;
  top: -20px;
  transform: translateY(0);
  transition: transform 200ms;
  width: 76px;
}

.cut-short {
  width: 50px;
}

.input:focus ~ .cut,
.input:not(:placeholder-shown) ~ .cut {
  transform: translateY(8px);
}

.placeholder {
  color: #65657b;
  font-family: sans-serif;
  left: 20px;
  line-height: 14px;
  pointer-events: none;
  position: absolute;
  transform-origin: 0 50%;
  transition: transform 200ms, color 200ms;
  top: 20px;
}

.input:focus ~ .placeholder,
.input:not(:placeholder-shown) ~ .placeholder {
  transform: translateY(-30px) translateX(10px) scale(0.75);
}

.input:not(:placeholder-shown) ~ .placeholder {
  color: #808097;
}

.input:focus ~ .placeholder {
  color: #dc2f55;
}

.submit {
  background-color: #08d;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: #eee;
  cursor: pointer;
  font-size: 18px;
  height: 50px;
  margin-top: 38px;
  // outline: 0;
  text-align: center;
  width: 100%;
}

.submit:active {
  background-color: #06b;
}
</style>
""")  # style
print("""</body>
        </html>""")
