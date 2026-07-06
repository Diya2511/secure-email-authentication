# 🔐 Secure Email Authentication System

A modern desktop-based authentication system built with **Python**, **Tkinter (ttkbootstrap)**, and **SQLite** that provides secure user registration, login, password hashing, and Email OTP verification.

---

## 📌 Features

- 👤 User Registration
- 🔑 Secure Login Authentication
- 🔒 SHA-256 Password Hashing
- 📧 Email OTP Verification
- 🗄️ SQLite Database Integration
- 👁️ Show/Hide Password
- 🎨 Modern GUI using ttkbootstrap
- ⚡ Fast and Lightweight Desktop Application

---

## 📸 Screenshots

> Add screenshots here after completing the project.

Example:

```
assets/screenshots/login.png
assets/screenshots/register.png
assets/screenshots/otp.png
```

---

## 🛠️ Tech Stack

- Python 3.11+
- ttkbootstrap
- Tkinter
- SQLite3
- hashlib
- smtplib
- python-dotenv
- Pillow

---

## 📂 Project Structure

```
secure-email-authentication/
│
├── assets/
│   └── images/
│       └── security.png
│
├── database/
│   └── users.db
│
├── src/
│   ├── auth.py
│   ├── database.py
│   ├── email_service.py
│   ├── otp.py
│   ├── main.py
│   └── ui/
│       ├── login_page.py
│       ├── register_page.py
│       ├── otp_page.py
│       └── dashboard_page.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Diya2511/secure-email-authentication.git
```

Move into the project directory

```bash
cd secure-email-authentication
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Environment Variables

Create a `.env` file in the project root.

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_google_app_password
```

> **Note:** Use a Google App Password instead of your Gmail password.

---

## ▶️ Run the Application

```bash
python src/main.py
```

---

## 🔐 Authentication Flow

```
Register
      │
      ▼
Password Hashed (SHA-256)
      │
      ▼
Stored in SQLite
      │
      ▼
Login
      │
      ▼
Credential Verification
      │
      ▼
Generate OTP
      │
      ▼
Send OTP via Gmail
      │
      ▼
Verify OTP
      │
      ▼
Dashboard
```

---

## 📚 Concepts Used

- Object-Oriented Programming (OOP)
- Authentication Systems
- SHA-256 Password Hashing
- Email OTP Verification
- SQLite Database Management
- Environment Variables
- GUI Development
- Error Handling
- Modular Programming

---

## 🚀 Future Improvements

- Forgot Password
- Password Reset via Email
- Session Management
- OTP Expiry Timer
- Login History
- User Profile
- Dark Mode
- Admin Dashboard
- Account Lock after Failed Attempts
- Logging & Audit Trail

---

## 📦 Dependencies

```
ttkbootstrap
Pillow
python-dotenv
```

---

## 👩‍💻 Author

**Diya S**

- GitHub: https://github.com/Diya2511

---

## ⭐ If you found this project useful, consider giving it a star!
