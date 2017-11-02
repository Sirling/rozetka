import unittest
import xmlrunner
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


butovaya_tehnika_id = "4306"
chainiki_linktext = "Электрочайники"
metal_plastik = "img[title='Металл + пластик']"
result_page = "https://bt.rozetka.com.ua/philips_hd9358_11/p13296383/"
chainik_name = "Электрочайник PHILIPS HD9358/11"


class MyTestCase(unittest.TestCase):
    def test_run2(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("https://rozetka.com.ua/")

        try:
           driver.find_element_by_id(butovaya_tehnika_id).click()
           WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, chainiki_linktext)))
           driver.find_element_by_link_text(chainiki_linktext).click()

           driver.find_element_by_css_selector(metal_plastik).click()

           driver.find_element_by_link_text(chainik_name).click()                                                         # Поиск элемента по тексту и клик по нему
           result = driver.current_url                                                                                    # Определение текущего урла
           self.assertEqual(result, result_page)                                                                          # Сравнение ожидаемого урла с фактического

        except NoSuchElementException:                                                                                    # кетчи на случай ошибок
            self.fail("Element missing")

        except TimeoutException:
            self.fail("Timeout")

        finally:
            driver.close()



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(verbosity=2, failfast=False, output='test-reports'))
