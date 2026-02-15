import streamlit as st
from bank import Bank

st.write("App Loaded Successfully")

bank = Bank()

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Option",
    ["Create Account", "Login & Manage"]
)

if menu == "Create Account":
    st.header("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    pin = st.text_input("4 Digit PIN", type="password")
    email = st.text_input("Email")

    if st.button("Create"):
        result = bank.create_account(name, age, int(pin), email)
        if isinstance(result, dict):
            st.success("Account Created Successfully!")
            st.write("Your Account Number:", result["Account_No."])
        else:
            st.error(result)

elif menu == "Login & Manage":
    st.header("Login")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Login"):
        user = bank.authenticate(acc_no, int(pin))
        if user:
            st.success("Login Successful!")

            action = st.selectbox("Choose Action", ["Deposit", "Withdraw", "View Details", "Delete Account"])

            if action == "Deposit":
                amount = st.number_input("Amount", min_value=1)
                if st.button("Deposit"):
                    if bank.deposit(user, amount):
                        st.success("Money Deposited!")
                    else:
                        st.error("Invalid Amount")

            elif action == "Withdraw":
                amount = st.number_input("Amount", min_value=1)
                if st.button("Withdraw"):
                    if bank.withdraw(user, amount):
                        st.success("Money Withdrawn!")
                    else:
                        st.error("Insufficient Balance")

            elif action == "View Details":
                st.write(user)

            elif action == "Delete Account":
                if st.button("Confirm Delete"):
                    bank.delete_account(user)
                    st.success("Account Deleted")

        else:
            st.error("Invalid Credentials")
