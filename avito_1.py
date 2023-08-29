import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    browser = webdriver.Chrome()
    try:
        link = "https://www.avito.ru/favorites"
        browser.get(link)
        browser.get("https://www.avito.ru/moskva/detskaya_odezhda_i_obuv/yubka_bezhevaya_dlya_devochki_zhenskaya_v_siniyu_polosku_3223057602")
        add_to_favorites_button=browser.find_element(
            By.XPATH, "//button[@data-marker='favorite-button']")
        add_to_favorites_button.click()
        browser.get("https://www.avito.ru/moskva/detskaya_odezhda_i_obuv/platya_i_yubki-dlya_devochek-ASgBAgICAkTkAuwL5gL6Cw?q=%D0%AE%D0%B1%D0%BA%D0%B0+%D0%B1%D0%B5%D0%B6%D0%B5%D0%B2%D0%B0%D1%8F+%D0%B4%D0%BB%D1%8F+%D0%B4%D0%B5%D0%B2%D0%BE%D1%87%D0%BA%D0%B8%2C+%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%B2+%D1%81%D0%B8%D0%BD%D0%B8%D1%8E+%D0%BF%D0%BE%D0%BB%D0%BE%D1%81%D0%BA%D1%83")
        first_listing=browser.find_element(By.XPATH,
            "//div[@data-marker='item-photo']"
        )
        first_listing.click()
        add_to_favorites_button=browser.find_element(
            By.XPATH,
            "//button[@data-marker='favorite-button']"
        )
        add_to_favorites_button.click()
        browser.get("https://www.avito.ru/favorites")
        remove_from_favorities_button= browser.find_element(
            By.XPATH,
            "//button[@data-marker='favorite-button']//*[name()='svg']"
        )
        remove_from_favorities_button.click()
        browser.quit()
        browser=webdriver.Chrome()
        browser.get("https://www.avito.ru/favorites")
        saved_listing = browser.find_element(By.XPATH, "//div[@data-marker='saved-listing']")
        assert saved_listing.is_displayed()
    finally:
        time.sleep(2)
        browser.quit()
