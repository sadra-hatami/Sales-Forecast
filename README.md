<div align="center">

# Sales Forecast
# 📈

### A small sales regression in Python

A linear model that reads a sales CSV, turns the date and advertising level into features, and scores how far the predicted sales sit from the real numbers.

<br>

# 👨‍💻 **Sadra Hatami**

### *Developer • Software Engineer • Creator*

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/license/mit)
![Open Source](https://img.shields.io/badge/Open_Source-Project-black?style=for-the-badge&logo=github)


<br>

[🌐 GitHub Profile](https://github.com/sadra-hatami)
•
[📧 Email](mailto:sadra.hatami.1732@gmail.com)

</div>

---

# 📑 Table of Contents

- [About](#-about)
- [Why This Project?](#-why-this-project)
- [Key Features](#-key-features)
- [Expected CSV](#-expected-csv)
- [Project Structure](#-project-structure)
- [Technologies](#️-technologies)
- [Installation](#-installation)
- [Usage](#️-usage)
- [Notes](#-notes)
- [FAQ](#-faq)
- [Contact](#-contact)
- [License](#-license)
- [Support](#-support)

---

# 📖 About

**Sales Forecast** is a small regression script.

`Sales_Forecast.py` loads a CSV, fills missing rows, splits the date into year, month, and day, and turns the advertising level into numeric columns. A linear regression model is trained on price, date parts, and advertising, then scored with mean squared error and root mean squared error.

> **Tagline:** *A Python sales regression that predicts a number from date, price, and advertising level.*

This is a study script, not a business forecast.

---

# 🚀 Why This Project?

A forecast demo is a clean place to practice a table, a split, and an error score.

This one keeps that path short:

- Read a sales CSV
- Build date and advertising features
- Scale the numbers
- Fit a linear model and print the error

The broader course notebooks live in [AI and Machine Learning Training](https://github.com/sadra-hatami/AI-ML-Training).

---

# ✨ Key Features

- 📄 CSV loader with a second encoding if UTF-8 fails
- 📅 Date split into year, month, and day
- 📣 Advertising levels turned into columns
- 📏 Standard scaling
- 📉 Linear regression
- 📊 MSE and RMSE on the test split

---

# 📄 Expected CSV

The script looks for these columns:

| Column | Role |
|---|---|
| `Date` | Turned into year, month, and day |
| `Price` | Numeric feature |
| `Advertising` | `High`, `Low`, or `Medium` |
| `Sales` | The number to predict |

No sample CSV is in this repository. Put your own file next to the script and point `filepath` at it.

---

# 📁 Project Structure

```text
Sales-Forecast/
├── Sales_Forecast.py
└── README.md
```

---

# 🛠️ Technologies

- Python 3.8+
- pandas
- NumPy
- scikit-learn

---

# 🚀 Installation

```bash
git clone https://github.com/sadra-hatami/Sales-Forecast.git
cd Sales-Forecast
pip install pandas scikit-learn
```

---

# ▶️ Usage

1. Place a CSV with the columns above next to the script.
2. In `Sales_Forecast.py`, replace the placeholder path:

```python
filepath = 'C:/path/to/your/sales_data.csv'
```

3. Run:

```bash
python Sales_Forecast.py
```

The script prints MSE and RMSE. If the file is missing, it stops with a clear message.

---

# 📝 Notes

- The path in the file is still a placeholder. It is not connected to a CSV in this repository.
- Missing values are filled forward. A bad date column will fail at conversion.
- The model is linear. It does not handle seasonality beyond the date parts.

---

# ❓ FAQ

### Is a dataset included?

No. Bring a CSV with `Date`, `Price`, `Advertising`, and `Sales`.

### Does it forecast a future day by itself?

No. It trains and scores on a held-out slice of the same file.

---

# 📬 Contact

**Developer:**

### Sadra Hatami

📧 [Email](mailto:sadra.hatami.1732@gmail.com)

🌐 [GitHub](https://github.com/sadra-hatami)

---

# 📄 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If this script is useful as a study sample, please consider giving it a ⭐ on GitHub.

---

<div align="center">

## Designed & Developed with ❤️ for the developer community of Iran and the world by **Sadra Hatami**

</div>
