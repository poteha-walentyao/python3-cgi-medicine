#!/usr/bin/env python3
import xml.etree.ElementTree as xml
import main as db


connection = db.create_connection('db.sqlite')
request_division = """select * from division;
"""
request_doctor = """select * from doctor;
"""
request_client = """select * from client;
"""


def create_xml(filename):
    # Start with the root element
    root = xml.Element("form")
    children1 = xml.Element("division")
    root.append(children1)
    for element in db.execute_read_query(connection, request_division):
        id_division = xml.SubElement(children1, "id_division")
        id_division.text = "{}".format(element[0])
        name = xml.SubElement(children1, "name")
        name.text = "{}".format(element[1])
        count = xml.SubElement(children1, "count")
        count.text = "{}".format(element[2])
        type = xml.SubElement(children1, "type")
        type.text = "{}".format(element[3])

    for element in db.execute_read_query(connection, request_doctor):
        children2 = xml.Element("doctor")
        root.append(children2)
        id_doctor = xml.SubElement(children2, "id_doctor")
        id_doctor.text = "{}".format(element[0])
        name = xml.SubElement(children2, "name")
        name.text = "{}".format(element[1])
        post = xml.SubElement(children2, "post")
        post.text = "{}".format(element[2])
        work_exp = xml.SubElement(children2, "work_exp")
        work_exp.text = "{}".format(element[3])

    for element in db.execute_read_query(connection, request_client):
        children3 = xml.Element("client")
        root.append(children3)
        id_client = xml.SubElement(children3, "client")
        id_client.text = "{}".format(element[0])
        name = xml.SubElement(children3, "name")
        name.text = "{}".format(element[1])
        age = xml.SubElement(children3, "age")
        age.text = "{}".format(element[2])
        diagnosis = xml.SubElement(children3, "diagnosis")
        diagnosis.text = "{}".format(element[3])
        id_division = xml.SubElement(children3, "id_division")
        id_division.text = "{}".format(element[4])
        id_doctor = xml.SubElement(children3, "id_doctor")
        id_doctor.text = "{}".format(element[5])

    tree = xml.ElementTree(root)
    with open(filename, "wb") as fh:
        tree.write(fh)


create_xml("test.xml")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>OUTPUT XML</title>
        </head>
        <body>""")
print("""
<div class="body">
<div class="form"><h2>База данных успешно скопирована в XML файл</h2></div>
<div class="form href"> <a href="../index.html">Главная страница</a></div>
</div>""")
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
