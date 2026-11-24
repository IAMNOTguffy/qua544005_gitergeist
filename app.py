from flask import Flask, render_template, request
import pyautogui as auto
from datetime import date

app = Flask(__name__)

def abrir_terminal(repositorio):
    auto.hotkey("win","r")
    auto.write("cmd")
    auto.press("enter")
    auto.write(f"cd {repositorio}")
    auto.press("enter")

def commitar(hoje):
    auto.write("git add .")
    auto.press("enter")
    auto.write(f'git commit -m "Aula do dia {hoje}"')
    auto.press("enter")
    auto.write("git push")
    auto.write("enter")
    auto.sleep(3)
    auto.write("exit")
    auto.press("enter")

@app.route("/", methods = ['GET', 'POST']) # associa uma url especifica a uma funcao python
def index():  # cria uma funcao com a funcao abrir que abre o repositorio
    hoje = date.today().strftime("%D/%m/%Y")
    repositorio = None
    if request.method == 'POST':
        repositorio = request.form.get("repositorio","")
        auto.PAUSE = 1
        abrir_terminal(repositorio)
        commitar(hoje)
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)