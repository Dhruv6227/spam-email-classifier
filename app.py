import streamlit as st
import pickle

model = pickle.load(open("model/model.pkl","rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl","rb"))

st.title("📧 Spam Email Classifier")
st.write("Enter email text below to check whether it is Spam or Not Spam")

email_text = st.text_area("Enter Email")

if st.button("Predict"):

    if email_text.strip() == "":
        st.warning("Please enter some text")
    
    else:
        email_vector = vectorizer.transform([email_text])
        
        prediction = model.predict(email_vector)

        if prediction[0] == 1:
            st.error("🚨 This is SPAM mail")
        else:
            st.success("✅ This is NOT spam mail")