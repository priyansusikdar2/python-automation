# **🚀 Python Automation Scraper**



Smart Amazon Product Scraper & Price Tracker using Python, Selenium, SQLite and Streamlit

Welcome to Python Automation Scraper, an automated system that scrapes product information from Amazon, stores it in a database, tracks prices, and visualizes the data in an interactive dashboard.

This project demonstrates real-world automation, web scraping, database management, and data visualization using Python.

# ✨ Features

✅ Automated Amazon product scraping
✅ Extracts Product Name, Price, Rating, and Link
✅ Stores data in SQLite database
✅ Product image downloading
✅ Email alerts when price drops
✅ Interactive Streamlit dashboard
✅ Modular and scalable code structure
✅ Easy to extend for price tracking over time

# 🧠 Technologies Used

Python

Selenium

SQLite

Streamlit

Requests

Pandas

# 📂 Project Structure

# python-automation
│
├── main.py
├── scraper.py
├── database.py
├── email_alert.py
├── config.py
├── dashboard.py
│
├── data/
│   └── products.db
│
├── images/
│
├── requirements.txt
└── README.md
⚙️ Installation

# Clone the repository:

git clone https://github.com/priyansusikdar2/python-automation.git

Go to the project folder:

cd python-automation

# Install dependencies:

pip install -r requirements.txt
▶️ Run the Scraper
python main.py

This will:

Launch the scraper

Collect product information

Store the data in SQLite database

# 📊 Run the Dashboard
streamlit run dashboard.py

Open in browser:

http://localhost:8501

The dashboard will show:

Product list

Prices

Ratings

Direct links

📧 Email Alerts

Configure your email in config.py

EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
RECEIVER = "receiver_email@gmail.com"

When the scraper detects a price drop, it automatically sends an alert.

# 📸 Example Output

The database stores information like:

Product	     Price	     Rating	        Link
Laptop	    ₹55,999	     4.3 ⭐	     Amazon Link
Headphones	 ₹2,499	     4.1 ⭐ 	   Amazon Link

# 💡 Future Improvements

Price history tracking

Graphs for price changes

Multi-page scraping

Telegram / WhatsApp alerts

Machine Learning price prediction

Deployment on cloud

# 👨‍💻 Author

Priyansu Sikdar

Computer Science Developer interested in:

Automation

AI Projects

Web Scraping

Machine Learning

GitHub:
https://github.com/priyansusikdar2

# ⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork it
📢 Share it with others

# 🚀 Why This Project?

This project demonstrates real-world automation skills useful in:

Data engineering

Market analysis

Price monitoring systems

AI-powered shopping assistants
