# 🛠️ Automated Web Test for Intervue.io - Selenium with Python

This repository contains an **automated web test** using **Selenium and Python** to validate the login functionality of [Intervue.io](https://www.intervue.io).

The script:

- Opens **Intervue.io**
- Navigates to the **login page**
- Attempts login with provided credentials
- Captures a **screenshot** if the login fails
- Closes the browser after execution

This project is designed for **QA automation testing**, ensuring the login mechanism functions as expected.

---

## 📌 **Project Structure**
```

📂 intervue-qa-test/
├── test_intervue.py # Main automation script
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── screenshots/ # Folder to store failure screenshots

````

---

## 🚀 **Setup & Installation**

### 1️⃣ **Clone This Repository**
```sh
git clone https://github.com/yourusername/intervue-qa-test.git
cd intervue-qa-test
````

### 2️⃣ **Install Dependencies**

Ensure you have Python installed, then run:

```sh
pip install -r requirements.txt
```

### 3️⃣ **Install WebDriver (Chrome)**

Selenium requires a **WebDriver** to automate the browser.

- Download **ChromeDriver**: [Download Here](https://sites.google.com/chromium.org/driver/)
- Place it in the project directory **OR** add it to your system **PATH**

🔹 Want to use **Edge** or **Firefox**? Install the respective WebDriver:

- **Edge**: [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- **Firefox**: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

---

## ▶️ **Run the Script**

Execute the script using:

```sh
python test_intervue.py
```

💡 **Example with Arguments**

```sh
python test_intervue.py --email test@example.com --password wrongpassword
```

---

## 📌 **Code Breakdown & Explanation**

### 🔹 **1. Initializing the WebDriver**

```python
if browser.lower() == "chrome":
    self.driver = webdriver.Chrome()
elif browser.lower() == "firefox":
    self.driver = webdriver.Firefox()
elif browser.lower() == "edge":
    self.driver = webdriver.Edge()
else:
    raise ValueError(f"Unsupported browser: {browser}")
```

📌 **Why?**

- This ensures flexibility by allowing different browsers (Chrome, Firefox, Edge).
- If an unsupported browser is passed, an error is raised.

---

### 🔹 **2. Opening the Website**

```python
def open_website(self):
    self.driver.get("https://www.intervue.io")
    print("Website opened successfully")
```

📌 **Why?**

- This function loads the Intervue.io website using **Selenium's `get()` method**.

---

### 🔹 **3. Navigating to Login Page**

```python
def navigate_to_login(self):
    login_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Login') or contains(@class, 'login')]"))
    )
    login_button.click()
    print("Navigated to login page")
```

📌 **Why?**

- Uses **Explicit Wait** to ensure the login button is clickable before clicking.
- Uses **XPath selectors** to dynamically locate the login button.

---

### 🔹 **4. Attempting Login**

```python
email_field = self.driver.find_element(By.XPATH, "//input[@type='email']")
password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")
submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
```

📌 **Why?**

- Locates **email** and **password fields** dynamically using XPath.
- Uses `send_keys()` to input credentials.

---

### 🔹 **5. Capturing Screenshot on Failure**

```python
def take_screenshot(self, filename):
    self.driver.save_screenshot(filename)
    print(f"Screenshot saved as {filename}")
```

📌 **Why?**

- If login fails, the script captures the current screen state and saves it as an image for debugging.

📌 **Example Screenshot File:**

```
📂 intervue-qa-test/
   ├── login_button_not_found_20250301-091259.png  👈 Saved screenshot of failed login
```

---

## 📸 **Screenshot Handling**

🔹 The script saves screenshots in the **screenshots/** directory with a timestamped filename:

```sh
login_failed_20250228-153000.png
```

🔹 This helps **QA teams** analyze why the login failed.

---

## 🔧 **Customization**

🔹 **Modify Login Credentials**  
Edit `test_intervue.py` and update:

```python
test_email = "your-email@example.com"
test_password = "your-password"
```

🔹 **Use a Different Browser**  
Change `"chrome"` to `"firefox"` or `"edge"` in:

```python
test = IntervueTest(browser="chrome")
```

---

## ❌ **Troubleshooting**

| Issue                        | Solution                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------- |
| `WebDriverNotFoundException` | Ensure **ChromeDriver** is installed and in the system **PATH**.                            |
| `ElementNotFoundException`   | The website structure might have changed. Update **XPath selectors** in `test_intervue.py`. |
| `TimeoutException`           | Increase wait times using `WebDriverWait(driver, 15)` if the website is slow.               |

---

🚀 Happy Testing!

```

```
