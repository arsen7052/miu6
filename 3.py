from flask import Flask 
import sqlite3

def novgorod(s):
    return ' '.join(s.split('_'))

app = Flask(__name__)
@app.route("/")
def home_pag1():
    stil = """
h1{
    display: flex;
    justify-content: center;
    align-items: center;
}
.btn{
    width: 400px;
    height: 70px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: auto;
    margin-top: 4%;
    border-style: solid;
    background-color: red;
    color: white;
    border-radius: 30px;
    text-decoration: none;
    font-size: 22px;
    h1{
    display: flex;
    justify-content: center;
    align-items: center;
}
}"""
    return f"""
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Главное меню</title>
        
        <link
            rel="stylesheet"
            href="Main.css">
        <style>
        {stil}
        </style>
    </head>
    <body>
        <h1>Главное меню</h1>
        <div class="container">
            <a class="btn" href="Raspisanie.html" role="button">Расписание</a>
            <a class="btn" href="http://127.0.0.1:8080/inf" role="button">Информация о городах</a>
            <a class="btn" href="" role="button">Погода</a>
            <a class="btn" href="food_menu.html" role="button">Заказать еду и напитки</a>
            <a class="btn" href="" role="button">Получить плед</a>
        </div>
    </body>
</html>
"""

@app.route("/in/<name_city>")
def home_pag(name_city):
    stil = """
h1{
    display: flex;
    justify-content: center;
    align-items: center;
}

.btn{
     width: 400px;
    height: 70px; 
      display: flex;  
     flex-direction: row;
    justify-content: center;
    align-items: center; 
    margin: auto;
    margin-top: 10%; 
    border-style: solid;
    background-color: red;
    color: white;
    border-radius: 30px;
    text-decoration: none;
    font-size: 22px;
}
.container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 14px;
    font-size: 22px;
}
"""
    conn = sqlite3.connect('city.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT dost FROM city WHERE name='{name_city}'")
    row = cursor.fetchall()
    print(row)
    row = row[0][0].split("\n")
    print(row)
    dost = ""
    for i in row:
        dost += "<li>"+i+"</li>"
    conn.close()
    return f"""
<!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Space</title>
          <link rel="stylesheet" href="{app.url_for('static', filename='css/style.css')}">
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <style>
        {stil}
        </style>
        </head>
        <body>
        <div>
        <h1>{novgorod(name_city)}</h1>
        <div class="container">
            Достопримечательности, которые стоит посетить:<br><br>
            <ul>
                {dost}
            </ul>
        </div>
        <div class="d-flex justify-content-evenly">
            <a class="btn btn-danger" href="http://127.0.0.1:8080/inf" role="button">Назад</a>
        <a class="btn btn-danger " href="http://127.0.0.1:8080/inf/{name_city}" role="button">Дальше</a>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
        </html>
"""



@app.route("/inf")
def home_page():
    stil = """"
    h1{
    display: flex;
    justify-content: center;
    align-items: center;
}
.btn{
    width: 400px;
    height: 70px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: auto;
    margin-top: 4%;
    border-style: solid;
    background-color: red;
    color: white;
    border-radius: 30px;
    text-decoration: none;
    font-size: 22px;
    
}
h1{
    display: flex;
    justify-content: center;
    align-items: center;
}
    """
    return f"""
            <!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Информация о городах</title>
        <style>{stil}</style>
    </head>
    <body>
        <h1>Информация о городах</h1>
        <div class="container">
            <a class="btn" href="http://127.0.0.1:8080/in/Москва" role="button">Москва</a>
            <a class="btn" href="http://127.0.0.1:8080/in/Тверь" role="button">Тверь</a>
            <a class="btn" href="http://127.0.0.1:8080/in/Великий_Новгород" role="button">Великий Новгород</a>
            <a class="btn" href="http://127.0.0.1:8080/in/Санкт-Петербург" role="button">Санкт-Петербург</a>
            <a class="btn" class="back" href="http://127.0.0.1:8080/" role="button">Назад</a>

        </div>
    </body>
</html>
        """



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)