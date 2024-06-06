from flask import Flask
from flask import render_template
import random
import datetime

app = Flask(__name__)


current_day = datetime.datetime.now().weekday()


pizzas = [
    {
        "name": "Маргарита",
        "price": "150 грн.",
        "composition": "томатний соус, моцарелла, базилік.",
        "Diameter": "30 см.",
        "Weight": "550 грам.",
        "number": 1
    },
    {
        "name": "Пепероні",
        "price": "170 грн.",
        "composition": "томатний соус, моцарелла, пепероні.",
        "Diameter": "35 см.",
        "Weight": "600 грам.",
        "number": 1
    },
    {
        "name": "Гавайська",
        "price": "180 грн.",
        "composition": "томатний соус, моцарелла, шинка, ананаси.",
        "Diameter": "35 см.",
        "Weight": "620 грам.",
        "number": 1
    },
    {
        "name": "Чотири сири",
        "price": "190 грн.",
        "composition": "томатний соус, моцарелла, пармезан, горгонзола, дор-блю.",
        "Diameter": "35 см.",
        "Weight": "650 грам.",
        "number": 1
    },
    {
        "name": "М'ясна",
        "price": "200 грн.",
        "composition": "томатний соус, моцарелла, салямі, бекон, шинка.",
        "Diameter": "40 см.",
        "Weight": "700 грам.",
        "number": 1
    },
    {
        "name": "Вегетаріанська",
        "price": "180 грн.",
        "composition": "томатний соус, моцарелла, перець, гриби, цибуля, оливки.",
        "Diameter": "35 см.",
        "Weight": "620 грам.",
        "number": 1
    }
]


if current_day == 5:
    pizzas.append({        
        "name": "Суботня",
        "price": "200 грн.",
        "composition": "томатний соус, моцарелла, перець, гриби, папероні, чеддер.",
        "Diameter": "37 см.",
        "Weight": "700 грам.",
        "number": 1})
elif current_day == 6:
        for i in pizzas:
            if i ["name"] == "М'ясна":
                i ["price"] = "170 грн."
        for i in pizzas:
            if i ["name"] == "Чотири сири":
                i ["price"] = "175 грн."
elif current_day == 0:
        for i in pizzas:
            if i ["name"] == "Маргарита":
                i ["price"] = "140 грн."




@app.route('/')
def hellp_world():
    return render_template("base.html")


@app.route('/menu')
def name():
    return render_template("menu.html", date=pizzas)


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)