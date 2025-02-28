# Intervue.io Login Test Automation

Hey there! 👋 This repo contains a simple Selenium script to test the login functionality on intervue.io. It'll navigate to the site, try to log in, and take screenshots if anything goes wrong.

## What You'll Need

- Python 3.6 or newer
- A web browser (Chrome is recommended, but Firefox and Edge work too)
- A bit of patience with Selenium (it can be finicky sometimes!)

## Getting Started

### Setting Up Your Environment

1. **Clone this repo**
   ```
   git clone https://github.com/SyedMoin-Lab/intervue-login-test
   cd intervue-login-test
   ```

2. **Create a virtual environment** (keeps things clean)
   ```
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install Selenium**
   ```
   pip install selenium==4.15.2
   ```

4. **Get the right WebDriver**
   
   You'll need the driver that matches your browser:
   
   - **Chrome users (recommended)**:
     1. Check your Chrome version (Menu → Help → About Google Chrome)
     2. Download matching ChromeDriver from [here](https://sites.google.com/chromium.org/driver/)
     3. Extract it somewhere in your PATH (or you can specify the location in the code)

   - **Firefox users**:
     - Grab GeckoDriver from [here](https://github.com/mozilla/geckodriver/releases)
   
   - **Edge users**:
     - Download EdgeDriver from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

### Setting Up Your Test Credentials

Open `intervue_test.py` and find this part at the bottom:

```python
if __name__ == "__main__":
    # Replace these with your test credentials
    test_email = "test@example.com"
    test_password = "wrongpassword"
    
    test = IntervueTest(browser="chrome")
    test.run_test(test_email, test_password)
```

Change the email and password to whatever you want to test with.

## Running the Test

With your virtual environment activated, just run:

```
python intervue_test.py
```

Then sit back and watch as:
1. A browser window opens
2. It navigates to intervue.io
3. It clicks the login button
4. It enters your credentials and submits
5. It checks if the login worked
6. It takes a screenshot if there were problems
7. It closes the browser

## How the Code Works

Let me walk you through the main parts of the script:

### Browser Setup

```python
def __init__(self, browser="chrome"):
    # This part starts up your chosen browser
    if browser.lower() == "chrome":
        self.driver = webdriver.Chrome()
    # Firefox and Edge options also available
    
    self.driver.maximize_window()  # Full-screen mode
```

### Website Navigation

```python
def open_website(self):
    # Opens intervue.io in your browser
    self.driver.get("https://www.intervue.io")
```

### Finding the Login Button

```python
def navigate_to_login(self):
    # Waits for page to load
    # Finds and clicks the login button
    login_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Login') or contains(@class, 'login')]"))
    )
    login_button.click()
```

### Logging In

```python
def attempt_login(self, email, password):
    # Finds email field, types your email
    email_field = self.driver.find_element(By.XPATH, "//input[@type='email' or @name='email' or @id='email']")
    email_field.send_keys(email)
    
    # Finds password field, types your password
    password_field = self.driver.find_element(By.XPATH, "//input[@type='password' or @name='password' or @id='password']")
    password_field.send_keys(password)
    
    # Clicks submit
    submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit' or contains(text(), 'Sign in')]")
    submit_button.click()
```

### Taking Screenshots

```python
def take_screenshot(self, filename):
    # Saves a picture of what the browser is showing
    self.driver.save_screenshot(filename)
```

## Troubleshooting Tips

### If the script can't find elements:

1. **The website might have changed**
   - Open intervue.io and use browser inspection tools (F12) to check the actual element IDs/classes
   - Update the XPath selectors in the code

2. **WebDriver is outdated**
   - Make sure your WebDriver version matches your browser version

3. **Timing issues**
   - Try increasing the wait times in the code from 10 seconds to something higher

### If the browser crashes:

1. **Make sure the WebDriver is compatible with your system**
2. **Try running with a different browser**:
   ```python
   test = IntervueTest(browser="firefox")
   ```

## Need Help?

If you're stuck, feel free to open an issue in this repo. Happy testing! 🚀
