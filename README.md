# **Mirath - Islamic Inheritance Distribution App**

**Mirath** is a web application designed to help users calculate and distribute inheritance according to Islamic (Sharia) laws. The app allows users to input their inherited assets (money, property, etc.) and calculate the rightful share for each heir. This tool aims to make the process of inheritance distribution clear, transparent, and in full compliance with Islamic principles.

## **Features**
- **Inheritance Calculation**: Automatically calculates the inheritance distribution based on Islamic inheritance laws.
- **Asset Input**: Users can input money, properties (houses, cars, etc.), and other assets to be included in the calculation.
- **Heir Management**: Users can add heirs (sons, daughters, spouses) and their respective shares based on their Islamic rights.
- **User Authentication**: Secure user login and registration for a personalized experience.
- **Results Display**: Provides a breakdown of inheritance distribution and shares for each heir in a simple, understandable format.

## **Tech Stack**
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Authentication**: Flask-Login (or Flask-JWT)
- **Hosting**: Heroku (for deployment)

## **Installation**

### Prerequisites
Make sure you have the following installed:
- Python (3.7+)
- MySQL or any database of your choice
- Node.js (if you plan to modify the frontend assets)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/mirath.git
   cd mirath
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use: venv\Scriptsctivate
   ```

3. **Install the backend dependencies**:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Set up the database**:
   - Ensure that MySQL is running on your local machine.
   - Update the `SQLALCHEMY_DATABASE_URI` in `backend/config.py` with your database credentials.

5. **Run the application**:
   ```bash
   python backend/app.py
   ```

6. **Access the app**:
   Open your browser and go to `http://127.0.0.1:5000`.

### Frontend Setup

1. Navigate to the `frontend/` directory:
   ```bash
   cd frontend
   ```

2. Open `index.html` in any web browser to start testing the frontend or deploy it to your server.

## **Usage**

1. **Register and log in**: Users must register an account to access the inheritance calculator.
2. **Input Assets and Heirs**: Enter the total inherited money and properties. Specify the heirs (sons, daughters, etc.), and the app will calculate the shares.
3. **View Results**: The app displays the inheritance shares for each heir based on Islamic law.
   
## **Contributing**

Contributions are welcome! If you'd like to improve the project or add new features, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature/your-feature-name`).
5. Submit a pull request.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Authors**

- **Isah Abdulsalam** - *Initial work* - [Your GitHub](https://github.com/isahabdulsalam)

## **Acknowledgments**

- Inspired by the need for a transparent and automated inheritance distribution tool in compliance with Islamic laws.
- Special thanks to the open-source community for providing tools like Flask and MySQL that made this project possible.
