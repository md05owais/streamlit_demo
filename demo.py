
# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title('My first app')
# st.header('Car Price prediction')
# st.subheader('House Prediction')

# st.text_input( any)
# st.text('Like this video and subsribe it')

# st.title("Salary Pridiction")
# nav = st.sidebar.radio("Navigation",["Home","Prediction", "contribution"])
# if nav == "Home":
#     st.write('Home')
#     # st.image('data//premium_photo-1664637952648-8f0b876bad49.avif')
# elif nav=="Prediction":
#     st.write('Pred')
# else:
#     st.write('contri')
import streamlit as st
import pickle
import numpy as np

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('true.png')
# import base64
# @st.cache(peristtt=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str

#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return
# set_png_as_page_bg('true.png')
# bin_str = get_base64_of_bin_file('true.png')
# page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str

# st.markdown(page_bg_img, unsafe_allow_html=True)

# st.image('C:\Users\md.owais\Desktop\Python\decorators\true.png')


# classifier_name=['XGBoost Classifier', 'Random Forest Classifier']
# option = st.sidebar.selectbox('Which model would you like to use?', classifier_name)
# st.subheader(option)



#Importing model and label encoders
# model=pickle.load(open("final_xg_model.pkl","rb"))
# model_1 = pickle.load(open("final_rf_model.pkl","rb"))
# le_pik=pickle.load(open("label_encoding_for_gender.pkl","rb"))
# le1_pik=pickle.load(open("label_encoding_for_geo.pkl","rb"))


# def predict_churn(CreditScore, Geo, Gen, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):
#     input = np.array([[CreditScore, Geo, Gen, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]]).astype(np.float64)
#     if option == 'XGBoost Classifier':
#         prediction = model.predict_proba(input)
#         pred = '{0:.{1}f}'.format(prediction[0][0], 2)

#     else:
#         prediction = model_1.predict_proba(input)
#         pred = '{0:.{1}f}'.format(prediction[0][0], 2)

#     return float(pred)


def main():
    st.title("Prediction of churn customers")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:yellow;text-align:center;">Churn Classification</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)





    st.sidebar.subheader("Designed By")
    st.sidebar.text("Md Owais")


    CreditScore = st.slider('Select credit score', 300, 900)

    Geography = st.selectbox('Enter geography', ['France', 'Germany', 'Spain'])
    # Geo = int(le1_pik.transform([Geography]))

    area_code = st.selectbox('Enter the area code', ['Male', 'Female'])
    # Gen = int(le_pik.transform([Gender]))

    Age = st.slider("Select Age(in years)", 10, 95)

    Tenure = st.selectbox("Select tenure(in years)", ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','10', '11', '12', '13', '14', '15'])

    Balance = st.slider("Select balance", 0.00, 250000.00)

    NumOfProducts = st.selectbox('Select number of products', ['1', '2', '3', '4'])

    HasCrCard = st.selectbox("Has credit card or not.(yes-1,no-0)", ['0', '1'])

    IsActiveMember = st.selectbox("Is an active member or not.(yes-1,no-0)", ['0', '1'])

    EstimatedSalary = st.slider("Select the estimated salary", 0.00, 200000.00)

    churn_html = """  
              <div style="background-color:#F6EFEF;padding:10px >
               <h2 style="color:red;text-align:center;"> A churn customer</h2>
               </div>
            """
    no_churn_html = """  
              <div style="background-color:#F0F6EF;padding:10px >
               <h2 style="color:green ;text-align:center;"> not a churn customer</h2>
               </div>
            """

    if st.button('Predict'):
        # output = predict_churn(CreditScore, Geo, Gen, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary)
        output = 0.6
        st.success('The probability of customer being churned is {}'.format(output))
        st.balloons()

        if output >= 0.5:
            st.markdown(churn_html, unsafe_allow_html= True)
            

        else:
            st.markdown(no_churn_html, unsafe_allow_html= True)

# if __name__=='__main__':
main()