from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список для хранения всех ответов
results = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем данные из формы
        name = request.form.get("name")
        gender = request.form.get("gender")
        answer = int(request.form.get("study_habit"))

        # Сохраняем результат
        results.append({"name": name, "gender": gender, "answer": answer})

        # Переходим на страницу результатов
        return redirect(url_for('results_page'))

    # Показываем форму
    return render_template("index.html")

@app.route("/results")
def results_page():
    # Считаем средние по полу
    males = [r["answer"] for r in results if r["gender"] == "male"]
    females = [r["answer"] for r in results if r["gender"] == "female"]

    male_avg = sum(males)/len(males) if males else 0
    female_avg = sum(females)/len(females) if females else 0

    return render_template("results.html", male_avg=male_avg, female_avg=female_avg)

if __name__ == "__main__":
    app.run(debug=True)
