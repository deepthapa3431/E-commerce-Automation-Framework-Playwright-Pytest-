# 🛒 Playwright E-commerce Automation Framework

## 📌 Overview
<<<<<<< HEAD
A scalable test automation framework built using Python, Playwright, and Pytest following Page Object Model (POM) design with CI/CD integration.
=======

This project is a **scalable UI automation framework** built using Python, Playwright, and Pytest.

It follows the **Page Object Model (POM)** design pattern and supports **end-to-end testing of an e-commerce workflow**, including login, cart operations, and checkout.
>>>>>>> 90fdd71 (Fix CI issue, improve conftest, enhance README)

---

## 🚀 Features

* Page Object Model (POM)
* Pytest fixtures for setup/teardown
* Environment-based configuration
* Logging system
* Parallel execution using `pytest-xdist`
* HTML reporting
* Screenshot capture on failure
* CI/CD integration using GitHub Actions

---

## 🧱 Project Structure

```
ecommerce-automation/
│
├── pages/        # Page classes (POM)
├── tests/        # Test cases
├── utils/        # Helpers (logger, waits, etc.)
├── config/       # Config files
├── screenshots/  # Failure screenshots
├── conftest.py   # Fixtures & hooks
├── pytest.ini
├── requirements.txt
```

---

## 🧪 Test Scenarios

* Login Test
* Add to Cart Test
* Remove from Cart Test
* Checkout Flow Test
* End-to-End Flow Test

---

## ⚙️ Setup Instructions

### 1. Clone Repository
git clone https://github.com/deepthapa3431/E-commerce-Automation-Framework-Playwright-Pytest-.git
cd E-commerce-Automation-Framework-Playwright-Pytest-
=======

```
git clone https://github.com/deepthapa3431/playwright-ecom-automation.git
cd ecom-auto
```
(Fix CI issue, improve conftest, enhance README)

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
playwright install --with-deps
```

---

## ▶️ Running Tests

### Run all tests

```
pytest -n 2 --html=report.html --self-contained-html
```

### Run specific test

```
pytest tests/test_login.py
```

### Run with markers

```
pytest -m smoke
```

### Run in headed mode (local)

```
set HEADLESS=false
pytest
```

---

## 📊 Reports

* HTML report generated after execution
* Screenshots captured automatically on failure

> Tip: Add a screenshot of the HTML report here to improve project presentation.

---

## 🔄 CI/CD Integration

This project uses **GitHub Actions** to:

* Install dependencies and Playwright browsers
* Execute tests in parallel
* Generate HTML reports
* Upload artifacts (reports and screenshots)

> Tip: Add a GitHub Actions badge here once your pipeline is stable.

---

## 🧠 Design Decisions

* **POM (Page Object Model)**: Improves maintainability and reusability by separating UI logic from test logic
* **Fixtures**: Centralized setup and teardown for better test management
* **Parallel Execution**: Reduces test execution time using `pytest-xdist`
* **Environment-based configuration**: Enables flexibility across different environments (QA, staging, etc.)

---

## ⚠️ Challenges & Solutions

**Challenge:** Tests failed in CI due to missing display server
**Solution:** Configured Playwright to run in headless mode and added CI-specific settings

**Challenge:** Flaky tests due to timing issues
**Solution:** Leveraged Playwright’s auto-waiting and implemented stable interaction methods

---

## 🚀 Future Enhancements

* Integrate Allure reporting
* Add API + UI hybrid testing
* Dockerize test execution
* Implement test data management strategy

---

## 🔌 API Testing

- Implemented API testing using `requests` library
- Created reusable API client for GET and POST operations
- Validated response status codes and data
- Demonstrates hybrid testing (API + UI)

Example APIs tested:
- GET /posts
- POST /posts

---

## 🔥 Tech Stack

* Python
* Playwright
* Pytest
* GitHub Actions

---

## 👨‍💻 Author
<<<<<<< HEAD
=======

>>>>>>> 90fdd71 (Fix CI issue, improve conftest, enhance README)
Deep Thapa
