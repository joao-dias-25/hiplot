import streamlit as st
import hiplot as hip
import pandas as pd


st.set_page_config(layout="wide")

st.title("""parallel coordinates vizualization tool """)

col1, col2 = st.beta_columns(2)

with col2:
    st.write('''Explore your dataset ''')
    path = st.file_uploader("Upload Files",type=['csv'])


with col1:
    st.write('Datasets examples')


#@st.cache
def load_data():
    with col1:
        dataset = st.selectbox("choose dataset",
                                  ['anscombe', 'attention', 'brain_networks', 'car_crashes', 'dots',
                                   'exercise', 'flights', 'fmri', 'gammas', 'iris', 'planets', 'tips'])

    df = pd.read_csv(f'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/{dataset}.csv')
    return df

data = load_data().to_dict(orient='records')

if path:
    data = pd.read_csv(path).to_dict(orient='records')

xp = hip.Experiment.from_iterable(data)

# Display with `display_st` instead of `display`
ret_val = xp.display_st(ret="selected_uids", key="hip")

#st.markdown("hiplot returned " + json.dumps(ret_val))
