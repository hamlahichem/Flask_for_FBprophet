from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FloatField, DateField, FileField, IntegerField,SelectField,FieldList,BooleanField  
from wtforms.validators import DataRequired

class ParamaterForm(FlaskForm):
    growth= SelectField("growth",choices=['linear', 'logistic','flat'])
    yearly_seasonality=  SelectField("yearly seasonality",choices=['auto', 'True','False'])
    weekly_seasonality=  SelectField("weekly seasonality",choices=['auto', 'True','False'])
    daily_seasonality=  SelectField("daily seasonality",choices=['auto', 'True','False'])
    seasonality_mode=  SelectField("seasonality mode",choices=['additive', 'multiplicative'])
    seasonality_prior_scale= FloatField("seasonality prior scale")
    holidays_prior_scale= FloatField("holidays_prior_scale")
    changepoint_prior_scale= FloatField("changepoint_prior_scale")
    mcmc_samples= IntegerField("mcmc_samples")
    interval_width= FloatField("interval_width")
    uncertainty_samples= IntegerField("uncertainty_samples")
    stan_backend=StringField("stan_backend")
    #csvfile= FileField("Upload data csv file")

    submit= SubmitField("Submit")


   
