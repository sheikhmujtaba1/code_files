from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
browser = webdriver.Chrome(executable_path=r'C:\Users\sheik\Downloads\chromedriver_win32/chromedriver.exe', options=option)

browser.get("https://docs.google.com/forms/d/e/1FAIpQLSeRP3-IvxiGvLNoHL5efeXoukWIzehU7g-beVtVKQf_eJBqYQ/viewform")


##final = browser.find_element_by_class_name("quantumWizTextinputPapertextareaContentArea.exportContentArea")

for i in range(1500):
    textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    ##time.sleep(1)
    textboxes[0].send_keys("Muhammad Mujtaba")
    textboxes[1].send_keys("muhammad.mujtaba@centre.edu")
    radiobuttons[1].click()
    textboxes[2].send_keys("sheikhmujtaba")
    ##final.send_keys("Physical workouts, extreme sports")
    submit = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    another_response = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

browser.close()
