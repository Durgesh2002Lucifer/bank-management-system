import streamlit as st
from bank import Bank

st.set_page_config(page_title="Simple Bank App", layout="centered")
st.title("🏦 Welcome to Streamlit Bank")

menu = st.sidebar.selectbox("Choose Action", ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Info", "Delete Account"])

if menu == "Create Account":
    st.subheader("Create New Account")
    name = st.text_input("Your Name")
    age = st.number_input("Your Age", min_value=0, step=1)
    email = st.text_input("Your Email")
    pin = st.text_input("4-digit PIN", type="password")
    
    if st.button("Create"):
        if name and email and pin:
            bank = Bank()   # create object

            user = bank.create_account(
                name,
                int(age),
                int(pin),
                email
            )

            if isinstance(user, dict):
                st.success("Account created successfully")
                st.info(f"Your Account Number: {user['Account_No.']}")
            else:
                st.error(user)   # if error message returned
        else:
            st.warning("Fill all fields")


elif menu == "Deposit":
    st.subheader("Deposit Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    
    if st.button("Deposit"):
        bank = Bank()
        user = bank.authenticate(acc_no, int(pin))

        if user:
            success = bank.deposit(user, int(amount))
            if success:
                st.success("Amount deposited successfully")
            else:
                st.error("Invalid amount (Max 10000 allowed)")
        else:
            st.error("Invalid Account Number or PIN")


elif menu == "Withdraw":
    st.subheader("Withdraw Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        bank = Bank()
        user = bank.authenticate(acc_no, int(pin))

        if user:
            success = bank.withdraw(user, int(amount))
            if success:
                st.success("Withdrawal successful")
            else:
                st.error("Insufficient balance")
        else:
            st.error("Invalid Account Number or PIN")


elif menu == "Show Details":
    st.subheader("Account Details")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        bank = Bank()
        user = bank.authenticate(acc_no, int(pin))

        if user:
            st.json(user)
        else:
            st.error("Invalid Account Number or PIN")


elif menu == "Update Info":
    st.subheader("Update Your Info")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New Name (Optional)")
    email = st.text_input("New Email (Optional)")
    new_pin = st.text_input("New PIN (Optional)")

    if st.button("Update"):
        bank = Bank()
        user = bank.authenticate(acc_no, int(pin))

        if user:
            bank.update_user(user, name, email, new_pin)
            st.success("Account updated successfully")
        else:
            st.error("Invalid Account Number or PIN")


elif menu == "Delete Account":
    st.subheader("Delete Account")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        bank = Bank()
        user = bank.authenticate(acc_no, int(pin))

        if user:
            bank.delete_account(user)
            st.success("Account deleted successfully")
        else:
            st.error("Invalid Account Number or PIN")
