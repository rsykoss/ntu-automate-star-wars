
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys



options = Options()
# options.add_argument("--window-size=1680x1050")
options.add_experimental_option("excludeSwitches", ["enable-automation", 'enable-logging'])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--headless")

key={}
TIMEOUT = 20

def init():
    with open('config.txt') as f:
        for line in f:
            if line != "\n":
                (k, val) = line.split("=", 1)
                key[k.strip()] = val.strip()

def clicker():
    try:
        driver = webdriver.Chrome(executable_path=key.get('DRIVE'), options=options)
        driver.get('https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main')
        
        input = driver.find_element_by_id('UID')
        input.send_keys(key.get('USERNAME'))
        driver.find_element_by_xpath("//input[@type='submit']").click()
        input = driver.find_element_by_id('PW')
        input.send_keys(key.get('PASSWORD'))
        driver.find_element_by_xpath("//input[@type='submit']").click()


        done = False
        while not done:
            element_present = EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Add (Register) Selected Course(s)']"))
            WebDriverWait(driver, TIMEOUT).until(element_present)

            registration_open = False
            while not registration_open:
                driver.find_element_by_xpath("//input[@type='submit' and @value='Add (Register) Selected Course(s)']").click()
                try: 
                    alert = driver.switch_to.alert
                    if not alert.text.find('not allowed to register'):
                        registration_open = False
                    else: 
                        registration_open = True
                    alert.accept()
                except:
                    registration_open = True
            

            driver.find_element_by_xpath("//input[@type='submit' and @value='Confirm to add course(s)']").click()

            try: 
                alert = driver.switch_to.alert
                if alert.text.find('expired'):
                    alert.accept()
                    driver.quit()
                    clicker()
                alert.accept()
            except:
                pass
                    
            root = driver.find_element_by_tag_name('table').text
            print(driver.find_element_by_tag_name('table').text)
            if root.find('no more vacancy'):
                done = False
                driver.find_element_by_xpath("//input[@type='submit']").click()
                print("Number of courses still in process of adding: " + str(root.count('no more vacancy')))
            else:
                done = True
                print("--------------------- ADDED ALL COURSES --------------------")
    except Exception as e:
        print("ERROR:  " + str(e))
        print("--------------------- FAILED --------------------")
    finally:
        driver.close()
        driver.quit()
        
if __name__ == "__main__":
    init()
    if len(sys.argv) >= 2: 
        if sys.argv[1] == "-bg":
            options.add_argument("--headless")
    clicker()