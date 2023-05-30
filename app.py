from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route("/")
# def user():
#     return render_template("index.html")


@app.route("/calculations")
def calculate():
    return render_template("calculations.html")


@app.route("/names")
def home():
    names = ['Jonas', 'Antanas', 'Petras']
    return render_template("names.html", my_list=names)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        vardas = request.form['vardas']
        return render_template("greetings.html", vardas=vardas)
    else:
        return render_template("login.html")


# """ex1"""


# @app.route("/")
# def user():
#     return "Labas rytas Lietuva!"


# """ex2"""


# @app.route('/<word>')
# def repeat_word(word):
#     repeated_words = []
#     for word in range(5):
#         repeated_words.append(word)
#     return ' '.join(repeated_words)


"""ex3"""


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


@app.route("/leap", methods=['GET', 'POST'])
def display_leap_years():
    if request.method == "POST":
        start_year = int(request.form["start_year"])
        end_year = int(request.form["end_year"])
        leap_years = [year for year in range(
            start_year, end_year + 1) if is_leap_year(year)]
        return render_template('l.html', start_year=start_year, end_year=end_year, leap_years=leap_years)
    else:
        return render_template("i.html")


if __name__ == "__main__":
    app.run(debug=True)
