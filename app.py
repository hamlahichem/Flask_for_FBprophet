from crypt import methods
import os
from flask import Flask
from flask import render_template, request
import pandas as pd
from datetime import datetime
from forecast import forcast
from forms import ParamaterForm
app = Flask(__name__)
app.config['SECRET_KEY']="0123456789"

@app.route("/")
def index():
        paramform= ParamaterForm()
        return render_template("index.html",form= paramform)



@app.route("/form",methods=["POST","GET"])
def form():
    print(request.files["file"])
    growth=request.form.get("growth")
    yearly_seasonality=request.form.get("yearly_seasonality")
    weekly_seasonality=request.form.get("weekly_seasonality")
    daily_seasonality=request.form.get("daily_seasonality")
    seasonality_mode=request.form.get("seasonality_mode")
    seasonality_prior_scale=request.form.get("seasonality_prior_scale")
    holidays_prior_scale=request.form.get("holidays_prior_scale")
    changepoint_prior_scale=request.form.get("changepoint_prior_scale")
    mcmc_samples=request.form.get("mcmc_samples")
    interval_width=request.form.get("interval_width")
    uncertainty_samples=request.form.get("uncertainty_samples")
    stan_backend=request.form.get("stan_backend")
    
    params={
        "growth":growth,
        "yearly_seasonality":yearly_seasonality,
        "weekly_seasonality":weekly_seasonality,
        "daily_seasonality":daily_seasonality,
        "seasonality_mode": seasonality_mode,
        "seasonality_prior_scale": seasonality_prior_scale,
        "holidays_prior_scale": holidays_prior_scale,
        "changepoint_prior_scale": changepoint_prior_scale,
        "mcmc_samples":mcmc_samples,
        "interval_width": interval_width,
        "uncertainty_samples": uncertainty_samples,
        "stan_backend":stan_backend
    }

    file= request.files['file']

    newfilename= f"{file.filename.split('.')[0]}_{str(datetime.now())}.csv" 

    save_location=os.path.join("uploads",newfilename) 
    file.save(save_location)
    # read csv and start process
    df=pd.read_csv(save_location)
    print("print input csv dataframe : \n",df)
    forcastdf=forcast(df,params)
    return render_template("prediction.html", tables=[forcastdf.to_html(classes='data')], titles=df.columns.values)



@app.route('/upload',methods=["GET", "POST"])
def upload():
    
    if request.method == "GET":
        return render_template("upload.html")
    else :
        # save uploaded file to 
        file= request.files['file']
        if file:
            print(type(file))
            newfilename= f"{file.filename.split('.')[0]}_{str(datetime.now())}.csv" 
            save_location=os.path.join("uploads",newfilename) 
            file.save(save_location)
            # read csv and start process
            df=pd.read_csv(save_location)
            print("print input csv dataframe : \n",df)

            forcastdf=forcast(df)
            return render_template("index.html",filename= newfilename,tables=[forcastdf.to_html(classes='data')], titles=df.columns.values);
            

     
 

if __name__ == "__main__":
    app.run()
