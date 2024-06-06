from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/") #connects that tag to function
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>") #connects that tag to function
def about(station,date):
    filename = "data_small/TG_STAID"+str(station).zfill(6)+".txt"
    df = pd.read_csv(filename, skiprows=20,parse_dates=["    DATE"])
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10


    return {"station": station,
            "date": date,
            "temperature": temp}



if __name__ == "__main__": # website run only if main is executed directly and not imported
    app.run(debug=True)
