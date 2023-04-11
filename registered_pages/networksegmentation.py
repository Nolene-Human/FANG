
import streamlit as lit
import pandas as pd

@lit.cache_data
def network_segementatation():
    
    df=pd.Dataframe(
        [
        {"Ip Address":"265.265.265.265.265","Mac Address":"00:00:00:00:00","Manufacturer":"Tibro","Use":" "},
        {"Ip Address":"265.265.265.265.265","Mac Address":"00:00:00:00:00","Manufacturer":"TP-Link","Use":" "},
        {"Ip Address":"265.265.265.265.265","Mac Address":"00:00:00:00:00","Manufacturer":"Unknown","Use":" "},
        {"Ip Address":"265.265.265.265.265","Mac Address":"00:00:00:00:00","Manufacturer":"Philips LIghtimg","Use":" "},
        ]
    )
    lit.dataframe(df,use_container_width=True)


    edited_df = lit.experimental_data_editor(df)
   

