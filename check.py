from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver with incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

# URL of the Google Form
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdiDl_sgvqMFtOv45fUCVegya6IbqattwhpgFAe9im3PmD_Xw/viewform"  # Replace with your form URL

# Sample data to fill in the form (modify according to your form's required fields)
form_data = {
    "First Name": "John",
    "Last Name": "Doe",
    "Email": "john.doe@example.com",
    "Phone Number": "1234567890",
    "Comments": "This is a test comment"
}

try:
    # Open the Google Form
    driver.get(form_url)
    time.sleep(2)
    email_input = driver.find_element(By.XPATH, "//input[@type='email']")
    email_input.send_keys("i230532@isb.nu.edu.pk")
    email_input.send_keys(Keys.RETURN)

    # === Enter Password ===
    time.sleep(5)
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys("I$b2341742")
    password_input.send_keys(Keys.RETURN)
    time.sleep(20)
    # Wait for the form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "freebirdFormviewerComponentsQuestionBaseRoot"))
    )
    
    # Find all question containers in the form
    questions = driver.find_elements(By.CLASS_NAME, "freebirdFormviewerComponentsQuestionBaseRoot")
    
    for question in questions:
        # Check if the field is required (look for the red asterisk)
        is_required = question.find_elements(By.CLASS_NAME, "freebirdFormviewerComponentsQuestionBaseRequiredAsterisk")
        
        if is_required:
            # Get the label of the question
            label = question.find_element(By.CLASS_NAME, "freebirdFormviewerComponentsQuestionBaseTitle").text.strip()
            
            # Remove the asterisk if present in the label
            label = label.replace("*", "").strip()
            
            # Find the input field (text input or textarea)
            try:
                input_field = question.find_element(By.CLASS_NAME, "quantumWizTextinputPaperinputInput")
            except:
                try:
                    input_field = question.find_element(By.CLASS_NAME, "quantumWizTextinputPapertextareaInput")
                except:
                    continue  # Skip if no input field found
            
            # Fill the field if the label matches the form_data keys
            if label in form_data:
                input_field.clear()
                input_field.send_keys(form_data[label])
                print(f"Filled field '{label}' with value '{form_data[label]}'")
    
    # Wait briefly to ensure all fields are filled
    time.sleep(1)
    
    # Find and click the submit button
    submit_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Submit')]")
    submit_button.click()
    
    # Wait for the submission confirmation
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "freebirdFormviewerViewResponseConfirmationMessage"))
    )
    print("Form submitted successfully!")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Close the browser
    time.sleep(2)
    driver.quit()
