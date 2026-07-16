import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')
list_of_states=list(df['State'].unique())
list_of_states.insert(0,'India')

st.sidebar.title('Indias data visualization')

selected_state= st.sidebar.selectbox('Select State',list_of_states)

primary=st.sidebar.selectbox('Select Primary parameter',sorted(df.columns[5:]))
secoundary=st.sidebar.selectbox('Select Secoundary parameter',sorted(df.columns[5:]))


plot=st.sidebar.button('Visulize')

if plot:
    st.text('Size Represent Primary Parameter')
    st.text('color Represent Secoundary Parameter')
    if selected_state=='India':
        # plot for india
        fig = px.scatter_map(df, lat="Latitude", lon="Longitude",size=primary,color=secoundary, color_continuous_scale=px.colors.cyclical.IceFire
                             ,zoom=3,size_max=35,width=1200,height=700,hover_name='District')
        
        st.plotly_chart(fig,use_container_width=True)
    else:
        #plot for satte
        stste_df=df[df['State']==selected_state]
        fig = px.scatter_map(stste_df, lat="Latitude", lon="Longitude",size=primary,color=secoundary, color_continuous_scale=px.colors.cyclical.IceFire
                             ,zoom=6,size_max=35,width=1200,height=700,hover_name='District')
        
        st.plotly_chart(fig,use_container_width=True)


