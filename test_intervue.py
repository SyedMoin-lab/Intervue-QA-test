import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class IntervueTest:
    def __init__(self, browser="chrome"):
        """Initialize WebDriver based on browser choice"""
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif browser.lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif browser.lower() == "edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        self.driver.maximize_window()

    def open_website(self):
        """Open the Intervue.io website"""
        self.driver.get("https://www.intervue.io")
        print("✅ Website opened successfully")

    def navigate_to_login(self):
        """Find and click the login button"""
        try:
            # Wait for the page to fully load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Adjust XPath if needed
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Login') or contains(@href, 'login')]"))
            )
            login_button.click()
            print("✅ Navigated to login page")
            return True
        except TimeoutException:
            print("❌ Failed to find the login button")
            self.take_screenshot("login_button_not_found")
            return False

    def attempt_login(self, email, password):
        """Attempt to log in with the provided credentials"""
        try:
            # Wait for the login form to load
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
            )

            # Enter email
            email_field = self.driver.find_element(By.XPATH, "//input[@type='email']")
            email_field.clear()
            email_field.send_keys(email)

            # Enter password
            password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")
            password_field.clear()
            password_field.send_keys(password)

            # Click submit button
            submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()

            # Wait for potential error message or dashboard redirect
            time.sleep(3)

            # Check if an error message is displayed
            error_elements = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'error') or contains(@class, 'alert')]")
            
            if error_elements:
                print("❌ Login failed: Error message detected")
                self.take_screenshot("login_failed")
                return False
            else:
                # Check if login was successful by verifying a logged-in element
                try:
                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'dashboard')]"))
                    )
                    print("✅ Login successful")
                    return True
                except TimeoutException:
                    print("❌ Login might have failed, taking screenshot")
                    self.take_screenshot("login_status_uncertain")
                    return False

        except Exception as e:
            print(f"⚠️ Error during login attempt: {str(e)}")
            self.take_screenshot("login_error")
            return False

    def take_screenshot(self, filename):
        """Take a screenshot and save it with a timestamp"""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{filename}_{timestamp}.png"
        try:
            self.driver.save_screenshot(filename)
            print(f"📸 Screenshot saved as {filename}")
        except Exception as e:
            print(f"⚠️ Failed to take screenshot: {str(e)}")

    def close_browser(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()
            print("🚪 Browser closed")

    def run_test(self, email, password):
        """Execute the full test"""
        try:
            self.open_website()
            if self.navigate_to_login():
                login_result = self.attempt_login(email, password)
                print(f"🎯 Test completed. Login {'successful' if login_result else 'failed'}")
            else:
                print("❌ Test failed: Could not navigate to login page")
        finally:
            self.close_browser()

# Example usage
if __name__ == "__main__":
    # Replace with actual test credentials
    test_email = "test@example.com"
    test_password = "wrongpassword"  # Using wrong password to trigger screenshot

    test = IntervueTest(browser="chrome")
    test.run_test(test_email, test_password)
