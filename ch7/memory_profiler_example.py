
import pandas as pd

@profile
def get_non_clicks(filename):
    
    ad_frame = pd.read_csv(filename)
    
    non_clicks = ad_frame[ad_frame.click == 0]
    
    return non_clicks

get_non_clicks("data/ads_data_sample.csv")