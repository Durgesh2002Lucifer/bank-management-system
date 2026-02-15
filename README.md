🏦 Bank Management System (Streamlit Web App)
📌 Overview

The Bank Management System is a web-based banking application built using Python and Streamlit.
It allows users to create accounts, authenticate securely, and perform core banking operations such as deposit, withdrawal, updating details, and account deletion.

This project demonstrates backend logic design, file-based data persistence, authentication handling, and modular Python architecture.

🚀 Features

✅ Create new bank account

✅ Secure login using Account Number & PIN

✅ Deposit money

✅ Withdraw money

✅ View account details

✅ Update account information

✅ Delete account

✅ Persistent data storage using JSON

🛠️ Tech Stack

Frontend: Streamlit

Backend: Python

Database: JSON file (file-based persistence)

Version Control: Git & GitHub

📂 Project Structure
Bank Management System/
│
├── app.py        # Streamlit UI
├── bank.py       # Core banking logic
├── data.json     # Data storage
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the repository

git clone https://github.com/your-username/bank-management-system.git
cd bank-management-system

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Run the application
python -m streamlit run app.py


Then open:

http://localhost:8501

🔐 Authentication Logic

Users must log in using:

Account Number

4-digit PIN

All operations such as deposit, withdrawal, and account updates require authentication.

📈 Learning Outcomes

Through this project, I practiced:

Object-Oriented Programming (OOP)

File handling and JSON data management

Authentication logic implementation

Modular project structure

Debugging import and deployment issues

Web app deployment using Streamlit

🌐 Deployment

This application can be deployed using:

Streamlit Cloud

Render

Railway

📌 Future Improvements

Replace JSON with SQLite database

Add transaction history

Add PIN hashing for enhanced security

Improve UI with dashboard layout

Add admin panel

👨‍💻 Author

Durgesh
B.Tech Computer Science Student
Interested in Full-Stack Development & AI-Driven Applications
