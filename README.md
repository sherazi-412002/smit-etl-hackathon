# Banggood Product Data Analysis Project

A comprehensive web scraping and data analysis project that extracts product information from Banggood.com, performs data cleaning and feature engineering, visualizes insights through Streamlit, and stores data in Microsoft SQL Server.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Pipeline](#data-pipeline)
- [Database Schema](#database-schema)
- [Analysis & Insights](#analysis--insights)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Project Overview

This project scrapes product data from multiple categories on Banggood.com, processes and analyzes the data, and provides interactive visualizations through a Streamlit dashboard. The cleaned data is stored in a Microsoft SQL Server database for persistent storage and querying.

## ✨ Features

- **Web Scraping**: Automated scraping of product data from multiple Banggood categories
- **Data Cleaning**: Comprehensive data preprocessing and cleaning pipeline
- **Feature Engineering**: Creation of two additional features for enhanced analysis
- **Interactive Dashboard**: Streamlit-based visualization dashboard
- **Database Integration**: Microsoft SQL Server database for data persistence
- **SQL Queries**: Pre-written queries for data validation and analysis

## 🛠 Technologies Used

- **Python 3**
- **Web Scraping**: BeautifulSoup, Request, Selenium
- **Data Processing**: Pandas, NumPy
- **Visualization**: Streamlit, Matplotlib, Seaborn, Plotly
- **Database**: Microsoft SQL Server, pyodbc
- **Others**: CSV for data storage

## 📁 Project Structure

```
smit-etl-hackathon/
│ 
├── hackathon_project.ipynb/      # (1.Main web scraping script,2. Data cleaning script,
                                     3. Exploratory Analysis,4. Load to SQL )         
│
├── data/
│   ├── bgd_products.csv/                        # Raw scraped data
│   └── cleaned_products_data.csv/               # Cleaned CSV files

├── analysis.py/                                 # Streamlit dashboard
│                 
│
├── queries.sql                                  # SQL queries for data validation
│           
├── report.txt                                   # Dinal Report of the Project
├── requirements.txt                             # Python dependencies
└── README.md                                    # Project documentation
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Microsoft SQL Server (or SQL Server Express)
- SQL Server Management Studio (SSMS)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/sherazi-412002/smit-etl-hackathon.git
   cd smit-etl-hackathon
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database connection**
   - Update database credentials in `hackathon_project.ipynb ->>  Step 4 (cell)`
   ```python
   SERVER = 'your_server_name'
   DATABASE = 'BanggoodDB'
   USERNAME = 'your_username'
   PASSWORD = 'your_password'
   ```

## 💻 Usage

### 1. Web Scraping

Run the scraper to collect product data:

In hackathon_project.ipynb run Scraper Cells

This will scrape products from different categories and save raw data to `data/bgd_products.csv/`.

### 2. Data Cleaning

Execute the cleaning script or notebook:

Execute the cells of Data cleaning.

Cleaned data will be saved to `data/cleaned_products_data.csv/`.

### 3. Run Streamlit Dashboard

Launch the interactive dashboard:

```bash
streamlit run analysis.py
```

The dashboard will open in your default browser at `http://localhost:8501`.

### 4. Database Operations

**Create database and dump data:**

Run the SQL Load Data Cells in hackathon_project.ipynb

**Run SQL queries in SSMS:**

Open `queries.sql` in SQL Server Management Studio and execute queries to validate data.

## 🔄 Data Pipeline

1. **Scraping**: Extract product data (name, price, rating, reviews, link, etc.)
2. **Cleaning**: Handle missing values, remove duplicates, standardize formats
3. **Feature Engineering**: Create additional features for analysis
4. **Analysis**: Generate insights and visualizations
5. **Deployment**: Deploy dashboard on Streamlit
6. **Storage**: Dump cleaned data into SQL Server database
7. **Validation**: Run SQL queries to verify data integrity



## 📊 Analysis & Insights

The Streamlit dashboard provides:

- Price distribution across categories
- Rating analysis and trends
- Product popularity metrics
- Category-wise comparison
- Custom filters and interactive charts

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This project is for educational purposes only. Please ensure you comply with Banggood.com's Terms of Service and robots.txt file when scraping data. Always respect rate limits and website policies.

## 📧 Contact

Syed Shoaib Sherazi - syedshoaibsherazi412002@gmail.com

Project Link: [https://github.com/sherazi-412002/smit-etl-hackathon](https://github.com/sherazi-412002/smit-etl-hackathon)

---

**Happy Scraping! 🚀**