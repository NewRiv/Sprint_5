from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from const import Const

class TestTransferAccountPage:

    def test_check_transfer_to_account_page(self, driver, page):
        #Проверка перехода по клику на «Личный кабинет».
        driver.get(Const.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_log_in_account)))
        driver.find_element(*page.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_log_in)))
        assert driver.find_element(*page.header_log_in_page)
