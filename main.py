from flask import Flask, request, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
@app.route('/')
def my_form():
    return render_template('index.html') + "<h3>يرجى ادخال رقم الهوية</h3>"

@app.route('/', methods=['POST'])
def my_form_post():
    
    text = request.form['text']

    import pandas as pd
    df = pd.read_excel('2.xlsx')
    try:
        fnl = df.loc[df['رقم الهوية'] == int(text)]["الفصل"]
        name = df.loc[df['رقم الهوية'] == int(text)]["الاسم"]
        lajna = df.loc[df['رقم الهوية'] == int(text)]["اللجنة"]
        return render_template('index.html') + f"<h3>اسم الطالب: {name.values[0]} <h3>" + "" + f"<h3>اللجنة: {lajna.values[0]}<h3>" + "" + f"<h>القاعة: {fnl.values[0]}<h3>"
    except Exception:
        return render_template('index.html') + "<h3>يرجى ادخال رقم صحيح<h3>"


app.run(host="0.0.0.0", port=8080)
