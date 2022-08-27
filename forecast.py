
# just return csv prediction
import pandas as pd
from prophet import Prophet


def forcast(data, params=None):
    print("-----------forcast methode------------------")

        
    growth=params["growth"]
    print(" check if the paramas is arriver to forcast growth ", growth)
    changepoints=None
    n_changepoints=1,
    changepoint_range=0.8
    yearly_seasonality=params["yearly_seasonality"]
    weekly_seasonality=params["weekly_seasonality"]
    daily_seasonality=params["daily_seasonality"]
    holidays=None
    seasonality_mode=params["seasonality_mode"]
    seasonality_prior_scale=float(params["seasonality_prior_scale"])
    holidays_prior_scale=float(params["holidays_prior_scale"])
    changepoint_prior_scale=float(params["changepoint_prior_scale"])
    mcmc_samples=int(params["mcmc_samples"])
    interval_width=float(params["interval_width"])
    uncertainty_samples=int(params["uncertainty_samples"])
    stan_backend=params["stan_backend"]


    model= Prophet ( growth= growth,
                     changepoints= changepoints,
                     n_changepoints=1, 
                     changepoint_range=changepoint_range, 
                     yearly_seasonality=yearly_seasonality,
                     weekly_seasonality=weekly_seasonality,
                     daily_seasonality=daily_seasonality, 
                     holidays=holidays, 
                     seasonality_mode=seasonality_mode,
                     seasonality_prior_scale=seasonality_prior_scale,
                     holidays_prior_scale=holidays_prior_scale,
                     mcmc_samples=mcmc_samples,
                     interval_width=interval_width,
                     uncertainty_samples=uncertainty_samples,
                     stan_backend=stan_backend



                     )
    model.fit(data)
    future = model.make_future_dataframe(periods=10)
 
    forecast = model.predict(future)
 
    print("-----------print forcast --------")

    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])


    fig1 = model.plot(forecast)
    fig2 = model.plot_components(forecast)

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

if __name__ =="__main__":
    forcast()




