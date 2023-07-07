from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

my_national_id = "your national id here"
my_collage_value = "you collage value in drop list must be a string" 
chrome_options = Options()
# chrome_options.add_argument("--headless")  
# chrome_options.add_argument("--disable-notifications") 
# chrome_options.add_argument("--disable-gpu") 
# chrome_options.add_argument("--no-sandbox") 

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://online-services.fayoum.edu.eg/pg_show_result_test/')

    while True:
        try:
            national_ID = driver.find_element(By.ID, 'ContentPlaceHolder2_MainUsercontrol1_NationalNumTxt')
            select_dropdown = driver.find_element(By.ID, 'ContentPlaceHolder2_MainUsercontrol1_faclist')
            result_button = driver.find_element(By.ID, 'ContentPlaceHolder2_MainUsercontrol1_ResultButton')
            national_ID.clear()
            national_ID.send_keys(my_national_id)

            dropdown = Select(select_dropdown)
            dropdown.select_by_value(my_collage_value)

            result_button.click()

            current_datetime = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
            screenshot_name = f"my_screenshot_{current_datetime}.png"
            driver.save_screenshot(screenshot_name)

            driver.refresh()
            time.sleep(2)  

        except Exception as e:
            print(f"Error occurred: {e}. Attempting to recover...")
            driver.refresh()
            time.sleep(2)  
            print("in exception")

except Exception as e:
    print(e)
finally:
    driver.quit()
