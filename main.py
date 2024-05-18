from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from data import *
from time import sleep


def main():
    # setting necessary options
    options = ChromeOptions()
        

    # the loop is used to repeat the action by big range of accounts
    for key in accounts:
        # options.add_argument("--headless=new")  # comment if you want to use gui version of chrome
        driver = webdriver.Chrome(options=options) # I have used chrome web driver, you can use any driver you want.
        driver.maximize_window()
        driver.implicitly_wait(2)
        
        # opening instagram.com login page
        driver.get("https://instagram.com/")

        # preparing account details buttons
        login, passwd = driver.find_elements(by=By.TAG_NAME, value="input")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
            
        # sending username and password the the necessary fields
        login.send_keys(key)
        passwd.send_keys(accounts[key])
        submit_button.click()
        
        # loggin in to an account
        try:
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="x9f619 x3nfvp2 xr9ek0c xjpr12u xo237n4 x6pnmvc x7nr27j x12dmmrz xz9dl7a xn6708d xsag5q8 x1ye3gou x80pfx3 x159b3zp x1dn74xm xif99yt x172qv1o x10djquj x1lhsz42 xzauu7c xdoji71 x1dejxi8 x9k3k5o xs3sg5q x11hdxyr x12ldp4w x1wj20lx x1lq5wgf xgqcy7u x30kzoy x9jhf4c"]')))
        except TimeoutException:
            print("\tTimed out while logging in")
            print(f"Username: {key}, password: {accounts[key]}")
            continue

        driver.get("https://instagram.com/"+target_user)

        # selection the options button
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="Options"]')))
        except TimeoutException:
            print("\tTimed out while opening target account")
            print(f"Username: {key}, password: {accounts[key]}")
            print(f"Target: ", target_user)
            exit(1)
        opt = driver.find_element(by=By.CSS_SELECTOR, value='svg[aria-label="Options"]')
        opt.click()
        sleep(2)

        # selecting the report button from options
        try:
            report_btn = driver.find_elements(by=By.CSS_SELECTOR, value="button[class='xjbqb8w x1qhh985 xcfux6l xm0m39n x1yvgwvq x13fuv20 x178xt8z x1ypdohk xvs91rp x1evy7pa xdj266r x11i5rnm xat24cr x1mh8g0r x1wxaq2x x1iorvi4 x1sxyh0 xjkvuk6 xurb0ha x2b8uid x87ps6o xxymvpz xh8yej3 x52vrxo x4gyw5p xkmlbd1 x1xlr1w8']")[2]
        except NoSuchElementException:
            print("\tCould not access the report button in options")
            exit(1)
        report_btn.click()

        # selecting the "report account" button
        try:
            report_account_btn = driver.find_elements(by=By.CSS_SELECTOR, value="._abn2")[1]
        except NoSuchElementException:
            print("\tCould not access the report account button")
            exit(1)
        report_account_btn.click()
        sleep(2)

        # selecting "It's posting content that shouldn't be on Instagram" option button
        spam_content = driver.find_elements(by=By.CSS_SELECTOR, value="button._abn2")
        spam_content[0].click()
        sleep(2)

        # focusing on the menu of report buttons
        layer = driver.find_element(by=By.CSS_SELECTOR, value="div[aria-label=\"Report\"]")
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(layer).perform()
        driver.switch_to.active_element

        # selecting the "Hate speech or symbols" option button
        hate_speech = driver.find_elements(by=By.CSS_SELECTOR, value='button._abn2')
        hate_speech[5].click()
        sleep(2)

        # selecting the submit button
        submit_btn = driver.find_element(by=By.CSS_SELECTOR, value="button[class=' _acan _acap _acas _aj1- _ap30']")
        submit_btn.click()
        sleep(3)
        print("Reported")
        driver.close()

main()
