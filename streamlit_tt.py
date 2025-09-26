import streamlit as st
# streamlit run "d:\Project Ch 1\streamlit_tt.py"

st.title("hello chai app !")
st.subheader("order your beloved chai...")

chai=st.selectbox("choose flavour:",["Adrak","kesar","elaichi","lemon","masala","kadak special"])
masala=st.checkbox("add masala")

if masala:
    st.write("masala added")
st.write(f"you choose {chai} chai")

select=st.button("make chai")
if select:
    st.success("great ! mast chai coose kari hai")

st.radio("select your chai base: ", ["water","milk","almond milk"])

no_input=st.number_input("enter your input",min_value=1,max_value=5,step=1)

name=st.text_input("enter your name:")
if name:
    st.write(f"hello ! {name} ji apki chai bas thodi der me hazir ho jayegi..... ")

spoon=st.slider("select your tea spoon",min_value=0,max_value=5,value=2,step=1)
if spoon:
    st.write(f"{spoon} selected")