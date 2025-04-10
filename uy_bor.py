from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
import pandas as pd

url = "https://uybor.uz/listings?category__eq=7&isNewBuilding__eq=false"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


titles = []
rooms = []
areas = []
floors = []
renovations = []
materials = []
prices = []
adresses = []
lifts = []
securities = []
internets = []
playground = []
sewerages = []
bathrooms = []
video_monitor = []
parking_spaces = []
air_condition = []
furniture = []
counter = 1

driver.get(url)

for i in range(1):
    float_links = driver.find_elements(By.XPATH, "//a[@class='MuiBox-root mui-style-1vssrzj']")
    flat_urls = []
    for link in float_links:
        flat_urls.append(link.get_attribute('href'))
    print(flat_urls)
    print(len(flat_urls))

    for furl in flat_urls:
        driver.get(furl)
        try:
            title = driver.find_element(By.XPATH, "//h1[@class='MuiTypography-root MuiTypography-h2 mui-style-1tyknu']").text
        except:
            title = "No title"

        titles.append(title)
        print(counter)
        print(f"Title: {title}")
        counter += 1

        try:
            room = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
                                                 "and contains(text(), 'Комнат')]"
                                                 "/following-sibling::div").text
        except:
            room = "No room"

        rooms.append(room)
        print(f"Room: {room}")

        try:
            area = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
                                                 "and contains(text(), 'Площадь')]"
                                                 "/following-sibling::div").text
        except:
            area = "No area"
        areas.append(area)
        print(f"Area: {area}")

        try:
            floor = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
                                                 "and contains(text(), 'Этаж')]"
                                                 "/following-sibling::div").text
        except:
            floor = "No floor"
        floors.append(floor)
        print(f"Floor: {floor}")


        try:
            renovation = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
                                                 "and contains(text(), 'Ремонт')]"
                                                 "/following-sibling::div").text
        except:
            renovation = "No renovation"
        renovations.append(renovation)
        print(f"renovation: {renovation}")

        try:
            material = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
                                                 "and contains(text(), 'Материал')]"
                                                 "/following-sibling::div").text
        except:
            material = "No material"
        materials.append(material)
        print(f"material: {material}")

        try:
            price = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h2 mui-style-86wpc3']").text
        except:
            price = "No price"
        prices.append(price)
        print(f"price: {price}")

        try:
            adresse = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body2 mui-style-31fjox']").text
        except:
            adresse = "No adresse"
        adresses.append(adresse)
        print(f"adresse: {adresse}")

        try:
            lift = driver.find_element(By.XPATH, "//div[@class='MuiStack-root mui-style-ekcp1r'"
                                                 "and contains(text(), 'Лифт')]"
                                                 "/following-sibling::div").text
        except:
            lift = floor[-1].split('/') # "5/9" -> ["5","9"]
            if int(lift[-1]) > 5:
                lift = "1"
            else:
                lift = "0"
        lifts.append(lift)
        print(f"lift: {lift}")


        try:
            security = driver.find_element(By.XPATH, "//div[@class='MuiStack-root mui-style-ekcp1r' and contains(text(), 'Видеонаблюдение')]/following-sibling::div").text
        except:
            security = ""

        securities.append(security)
        print(f"security: {security}")



