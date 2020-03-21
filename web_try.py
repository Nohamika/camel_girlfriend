import time
from selenium import webdriver
from selenium.webdriver import ActionChains

""" this program will calculate the girlfriend that gets the most camel in the website 
how many camels your girlfriend worth"""


def press_click_return_camels(driver):
    # presses the calculate button
    calc = driver.find_element_by_class_name("button-primary")
    calc.click();

    # waits 5 seconds fot the camel number animation to complete
    time.sleep(5)
    # takes the number of camels and prints it
    x = int(driver.find_element_by_class_name("result").text)
    print(x)
    return x


def find_best_eyecolor():
    lst_eyes = ['blue', 'green', 'brown', 'grey']
    results = 0
    j = 0
    for i in range(4):
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://kamelrechner.eu/en/female")
        # the actions of click and such
        move = ActionChains(driver)

        # finds chooses the radio button
        content = driver.find_elements_by_name("eyecolor")[i]
        print(content)
        move.click(content).perform()

        # clicks on calculate button and returns the number of camels
        x = press_click_return_camels(driver)

        if (x > results):
            results = x
            j = lst_eyes[i]
        driver.quit()
    return results, j


# print(find_best_eyecolor())

def find_best_boobs_size():
    results = 0
    lst_boob = ["boob-a", "boob-b", "boob-c", "boob-d"]
    for b in lst_boob:
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://kamelrechner.eu/en/female")
        # the actions of click and such
        move = ActionChains(driver)

        # checks the boob size image

        boob_size_label = driver.find_element_by_xpath('//label[@for="{}"]'.format(b))
        boob_size_label.click()

        # clicks on calculate button and returns the number of camels
        x = press_click_return_camels(driver)

        if (x > results):
            results = x
            j = b
        driver.quit()
    return results, j


# print(find_best_boobs_size())


def find_best_hair_length():
    results = 0
    lst_length = ["s", "m", "l"]
    for b in lst_length:
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://kamelrechner.eu/en/female")
        # the actions of click and such
        move = ActionChains(driver)

        # checks the hair length image
        hair_length_label = driver.find_element_by_xpath('//label[@for="{}"]'.format(b))
        hair_length_label.click()

        # clicks on calculate button and returns the number of camels
        x = press_click_return_camels(driver)

        if (x > results):
            results = x
            j = b
        driver.quit()
    return results, j


# print(find_best_hair_length())

def find_best_hair_color():
    results = 0
    lst_color = ["blonde", "brown", "black", "red", "grey"]
    for b in lst_color:
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://kamelrechner.eu/en/female")
        # the actions of click and such
        move = ActionChains(driver)

        # select the hair color
        hair_color_label = driver.find_element_by_xpath(
            '//select[@class="u-full-width"]/option[text()="{}"]'.format(b)).click()

        # clicks on calculate button and returns the number of camels
        x = press_click_return_camels(driver)

        if (x > results):
            results = x
            j = b
        driver.quit()
    return results, j


# print(find_best_hair_color())

def find_best_figure():
    results = 0
    i = 0
    lst_color = ["thin", "sporty", "normal", "chubby", "fat"]
    for b in lst_color:

        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://kamelrechner.eu/en/female")
        # the actions of click and such
        move = ActionChains(driver)

        # select the hair color
        hair_color_label = driver.find_element_by_xpath(
            '//select[@class="u-full-width"]/option[text()="{}"]'.format(b)).click()

        print(b)
        # clicks on calculate button and returns the number of camels
        x = press_click_return_camels(driver)

        if (x > results):
            results = x
            j = b
        driver.quit()
        i = i + 1
    return results, j


# find_best_figure()

def find_best_age():
    # the best result
    result = 0
    # how many camels got the round that just happened
    x = 1
    # the offset of ages i want from 18. if it is worth 5 so the age will be 23
    age_offset = 0

    while x >= result:
        # opens the website
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://kamelrechner.eu/en/female")
        move = ActionChains(driver)

        age_range = driver.find_element_by_xpath('//div[@class="rangeslider__handle"]')
        move.click_and_hold(age_range).move_by_offset(9 * age_offset, 0).release().perform()

        # clicks on calculate button and returns the number of camels
        x = press_click_return_camels(driver)
        if result < x:
            result = x
        print("for age", 18 + age_offset, "camels:", x)
        age_offset = age_offset - 1
        driver.quit()


#find_best_age()


def find_best_height():
    # the best result
    result = 0
    # how many camels got the round that just happened
    x = 1
    # the offset of height i want from 168. if it is worth 5 so the height will be 173
    height_offset = 0

    while x >= result:
        # opens the website
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://kamelrechner.eu/en/female")
        move = ActionChains(driver)

        age_range = driver.find_elements_by_xpath('//div[@class="rangeslider__handle"]')[1]
        move.click_and_hold(age_range).move_by_offset(6 * height_offset, 0).release().perform()

        # clicks on calculate button and returns the number of camels
        x = press_click_return_camels(driver)
        if result < x:
            result = x
        print("for height", 168 + height_offset, "camels:", x)
        height_offset = height_offset + 1
        driver.quit()

find_best_height()