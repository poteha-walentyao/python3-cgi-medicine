#!/usr/bin/env python3
import main as db


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>БД</title>
        </head>
        <body>
        <header class="header">
    <nav>
        <div class="submit" style="max-width:max-content; margin-top:20px;">
        <a href="../index.html">Главная страница</a>
        </div>
    </nav>
</header>""")
print("""<div class="body">""")
get_client = """select * from client"""
connection = db.create_connection('db.sqlite')
get_client = db.execute_read_query(connection, get_client)
for el in get_client:
    get_division = """select name from division where id_division =={}""".format(el[4])
    get_division = db.execute_read_query(connection, get_division)
    get_doctor = """select name from doctor where id_doctor =={}""".format(el[5])
    get_doctor = db.execute_read_query(connection, get_doctor)
    print("""
    <div class="form" >
        <p class="tag_p ic1 p" >Пациент:</p>
      <div class="input-container  input">
          <p class="tag_p">{}</p>
      </div>
        <p class="tag_p ic2" >Возраст:</p>
      <div class="input-container input">
          <p class="tag_p">{}</p>
      </div>
        <p class="tag_p ic2" >Диагноз:</p>
        <div class="input-container input">
            <p class="tag_p" >{}</p>
      </div>
        <p class="tag_p ic2" >Отдел:</p>
        <div class="input-container input">
            <p class="tag_p">{}</p>
      </div>
        <p class="tag_p ic2" >Врач:</p>
        <div class="input-container input">
            <p class="tag_p">{}</p>
      </div>
    </div>
    """.format(el[1], el[2], el[3], get_division[0][0], get_doctor[0][0]))
print("""
</div>
""")
print("""
<style>
body{margin:0;
background-color:#fff;}
  .body {
  align-items: center;
  background-color:#fff;
  justify-content: center;
  display: flex;
  flex-flow: row wrap;
  padding: 0;
  margin: 0;

}
.p{font-size:24px;}
.header{margin: 20px 0px 20px 0px;}
.header a{margin-left:30px;
          margin-right:30px;}
nav {display:flex;
    justify-content: center;}
.tag_p{margin:0;
margin-top:9px;
color:white;
font-family: sans-serif;
margin-bottom:5px;}
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
  margin-left:30px;
  margin-top:20px;
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
  margin-top: 30px;
}

.ic2 {
  margin-top: 20px;
}

.input {
  background-color: #303245;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: #eee;
  font-size: 18px;
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
  display:flex;
justify-content: center;
color:white;
font-family: sans-serif;
}
.submit a{padding-top:14px;
color:white;
font-family: sans-serif;
text-decoration:none;}
.submit:active {
  background-color: #06b;
}
</style>
""")    # style
print("""</body>
        </html>""")
