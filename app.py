from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

menu = {
    "Капучино": 80,
    "Лате": 85,
    "Еспресо": 60,
    "Чізкейк": 120,
    "Панкейки": 95
}


@app.route("/")
def home():
    current_time = datetime.now().strftime("%H:%M")
    current_hour = datetime.now().hour

    return render_template(
        "index.html",
        cafe_name="Coffee Time",
        current_hour=current_hour,
        current_time=current_time
    )


@app.route("/menu")
def menu_page():
    current_day = datetime.now().strftime("%A")

    return render_template(
        "menu.html",
        title="Меню кав'ярні",
        menu=menu,
        current_day=current_day
    )


if __name__ == "__main__":
    app.run(debug=True)