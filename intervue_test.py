import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class IntervueTest:
    def __init__(self, browser="chrome"):
        """Initialize the WebDriver based on browser choice"""
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
        """Open the intervue.io website"""
        self.driver.get("https://www.intervue.io")
        print("Website opened successfully")
        
    def navigate_to_login(self):
        """Find and click the login button on the homepage"""
        try:
            # Wait for the page to load completely
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Find and click the login button (this selector might need adjustment)
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Login') or contains(@class, 'login')]"))
            )
            login_button.click()
            print("Navigated to login page")
            return True
        except TimeoutException:
            print("Failed to find login button")
            self.take_screenshot("login_button_not_found.png")
            return False
            
    def attempt_login(self, email, password):
        """Attempt to login with provided credentials"""
        try:
            # Wait for the login form to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//form[contains(@class, 'login') or .//input[@type='email']]"))
            )
            
            # Enter email
            email_field = self.driver.find_element(By.XPATH, "//input[@type='email' or @name='email' or @id='email']")
            email_field.clear()
            email_field.send_keys(email)
            
            # Enter password
            password_field = self.driver.find_element(By.XPATH, "//input[@type='password' or @name='password' or @id='password']")
            password_field.clear()
            password_field.send_keys(password)
            
            # Click submit button
            submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit' or contains(text(), 'Sign in') or contains(text(), 'Login')]")
            submit_button.click()
            
            # Wait to see if login was successful (look for dashboard element or error message)
            time.sleep(3)  # Give time for the page to load or error to appear
            
            # Check if there's an error message
            error_elements = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'error') or contains(@class, 'alert')]")
            
            if error_elements:
                print("Login failed: Error message detected")
                self.take_screenshot("login_failed.png")
                return False
            else:
                # Check if we're redirected to dashboard or some authenticated page
                current_url = self.driver.current_url
                if "dashboard" in current_url or "account" in current_url:
                    print("Login successful")
                    return True
                else:
                    print("Login might have failed, taking screenshot")
                    self.take_screenshot("login_status_uncertain.png")
                    return False
                
        except Exception as e:
            print(f"Error during login attempt: {str(e)}")
            self.take_screenshot("login_error.png")
            return False
            
    def take_screenshot(self, filename):
        """Take a screenshot and save it with the given filename"""
        try:
            self.driver.save_screenshot(filename)
            print(f"Screenshot saved as {filename}")
        except Exception as e:
            print(f"Failed to take screenshot: {str(e)}")
            
    def close_browser(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()
            print("Browser closed")
            
    def run_test(self, email, password):
        """Run the complete test flow"""
        try:
            self.open_website()
            if self.navigate_to_login():
                login_result = self.attempt_login(email, password)
                print(f"Test completed. Login {'successful' if login_result else 'failed'}")
            else:
                print("Test failed: Could not navigate to login page")
        finally:
            self.close_browser()


# Example usage
if __name__ == "__main__":
    # Replace with actual test credentials
    test_email = "test@example.com"
    test_password = "wrongpassword"  # Using wrong password to test screenshot on failure
    
    test = IntervueTest(browser="chrome")
    test.run_test(test_email, test_password)