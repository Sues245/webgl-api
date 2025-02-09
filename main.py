from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import base64

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

    # Use webdriver-manager to get ChromeDriver automatically
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


    try:
        # Load WebGL website
        driver.get("https://webglreport.com/")
        time.sleep(5)  # Ensure full page load

        # Screenshot and save
        screenshot_path = "webgl_screenshot.png"
        driver.save_screenshot(screenshot_path)

        # Convert screenshot to base64
        with open(screenshot_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")

        # Extract WebGL-related content (modify this for specific WebGL data)
        webgl_text = driver.find_element("xpath", "//*[@id='info']").text

    finally:
        driver.quit()

    return {"image": base64_image, "text": webgl_text}

# API Endpoint for Operator
@app.get("/fetch_webgl")
def fetch_webgl():
    result = capture_webgl_screenshot()
    return {"webgl_data": result}
