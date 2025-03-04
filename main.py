from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

d = pd.read_csv("data_small/stations.txt", skiprows=17)
v = d[["STAID" , "STANAME                                 "]]
@app.route("/") #connects that tag to function
def home():
    return render_template("home.html", data = v.to_html())


@app.route("/api/v1/<station>/<date>") #connects that tag to function
def about(station,date):
    filename = "data_small/TG_STAID"+str(station).zfill(6)+".txt"
    df = pd.read_csv(filename, skiprows=20,parse_dates=["    DATE"])
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10


    return {"station": station,
            "date": date,
            "temperature": temp}
@app.route("/api/v1/<station>") #connects that tag to function
def alldata(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    res = df.to_dict(orient = "records")
    return (res)


@app.route("/api/v1/yearly/<station>/<year>") #connects that tag to function
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    res = df[df["    DATE"].str.startswith(str(year))]

    return (res.to_dict(orient="records"))

if __name__ == "__main__": # website run only if main is executed directly and not imported
    app.run(debug=True)
