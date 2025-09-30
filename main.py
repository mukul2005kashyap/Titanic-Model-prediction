import joblib
import streamlit as st
titanic_model=joblib.load("titanicmodel.pkl")


page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://wallpapercave.com/wp/wp2563741.jpg");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"]{
right: 2rem;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

pclass=st.sidebar.number_input("enter p_class", 1,3)
sex=st.sidebar.selectbox("enter gender",["Male","Female"])
age=st.sidebar.number_input("enter age", 0.0, 80.0)
sibsp=st.sidebar.number_input("enter sibsp", 0 ,8)
parch=st.sidebar.number_input("enter parch", 0 ,6)
fare=st.sidebar.number_input("enter fare", 0.0, 512.0)

if sex==0:
    sex="female"
else:
    sex="male"

st.title("🚢 Titanic Survival Prediction App")
st.write("### Enter passenger Details to Sidebar for check Predection Chance..")

st.subheader("👤 Passenger Details")
st.write(f"**P_Class:** {pclass}")
st.write(f"**Gender:** {sex}")
st.write(f"**Age:** {age}")
st.write(f"**Siblings/Spouse:** {sibsp}")
st.write(f"**Parents/Children:** {parch}")
st.write(f"**Fare:** ${fare}")

if st.button("Predict"):
    result=titanic_model.predict([[pclass, sex ,age ,sibsp ,parch ,fare]])
    if result ==1:
        st.success("Survived")
    else:
        st.success("Not Survived")
