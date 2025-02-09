from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import base64
import os

# Initialize FastAPI
app = FastAPI()

# Function to run WebGL in a headless browser and capture output
def capture_webgl_screenshot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--enable-webgl")
    chrome_options.add_argument("--use-gl=swiftshader")

    # Verify Chrome installation and set binary path
    chrome_path = "/usr/bin/google-chrome-stable"
    if not os.path.exists(chrome_path):
        chrome_path = "/usr/bin/google-chrome"
    
    chrome_options.binary_location = chrome_path

    # Corrected WebDriver setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Load Google for testing network connectivity
        driver.get("https://www.google.com/")
        time.sleep(5)  # Ensure full page load
        
        # Log page title for debugging
        print("Page title:", driver.title)
        
        # Screenshot and save
        screenshot_path = "webgl_screenshot.png"
        driver.save_screenshot(screenshot_path)

        # Convert screenshot to base64
        with open(screenshot_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")

        # Extract WebGL-related content (keeping for WebGL future use)
        webgl_text = "Test completed. Check logs for page title."

    finally:
        driver.quit()

    return {"image": base64_image, "text": webgl_text}

# API Endpoint for Operator
@app.get("/fetch_webgl")
def fetch_webgl():
    result = capture_webgl_screenshot()
    return {"webgl_data": result}
