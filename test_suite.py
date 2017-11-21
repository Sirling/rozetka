import unittest
import xmlrunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


search_field_css = "input.rz-header-search-input-text.passive"
search_button = "button.btn-link-i.js-rz-search-button"
butovaya_tehnika_id = "4306"
chainiki_linktext = "Электрочайники"
metal_plastik = "img[title='Металл + пластик']"
result_page = "https://bt.rozetka.com.ua/philips_hd9358_11/p13296383/"
chainik_name = "Электрочайник PHILIPS Viva Collection HD9358/11"

class rozetka_test(unittest.TestCase):
    def setUp(self):                                                                                                      # Функция, которая вызывается перед каждым тестом

        self.driver = webdriver.Chrome()                                                                                  # Инициализация драйвера для Хрома
        self.driver.get("https://rozetka.com.ua/")                                                                        # Переход по ссылке сайта
        self.driver.maximize_window()                                                                                     # Максимизирует окно

    # Логин / логаут
    def test_run1(self):

        driver = self.driver
        driver.get("https://my.rozetka.com.ua/")

        try:
            element_login = driver.find_element_by_name("login")                                                          # Поиск поля логин по имени
            element_login.send_keys("test.shvets@gmail.com")                                                              # Передача данных в поле
            element_pass = driver.find_element_by_name("password")                                                        # Поиск поля пароль по имени
            element_pass.send_keys("Test21")                                                                              # Передача данных в поле

            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//span[@class='btn-link-i']")))      # Ожидание пока елемент не появится
            driver.find_element_by_xpath("//span[@class='btn-link-i']").click()                                           # Клик по элементу

        except NoSuchElementException:                                                                                    # кетчи на случай ошибок
            self.fail("Element missing")

        except TimeoutException:
            self.fail("Timeout")

        finally:                                                                                                          # Блок, который выполнится в любом случае
            driver.close()

    # Переход по категориям
    def test_run2(self):

        driver = self.driver

        try:
           driver.find_element_by_id(butovaya_tehnika_id).click()
           WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, chainiki_linktext)))
           driver.find_element_by_link_text(chainiki_linktext).click()
           WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, metal_plastik)))
           driver.find_element_by_css_selector(metal_plastik).click()

           driver.find_element_by_link_text(chainik_name).click()                                                         # Поиск элемента по тексту и клик по нему
           result = driver.current_url                                                                                    # Определение текущего урла
           self.assertEqual(result, result_page)                                                                          # Сравнение ожидаемого урла с фактического

        except NoSuchElementException:                                                                                    # кетчи на случай ошибок
            self.fail("Element missing")

        except TimeoutException:
            self.fail("Timeout")

        finally:
            driver.close()                                                                                                # Блок, который выполнится в любом случае

    # Прямой поиск
    def test_run3(self):

        driver = self.driver

        try:
            el_search = driver.find_element_by_css_selector(search_field_css)                                             # Поиск поля поиска по имени класса
            el_search.send_keys("PHILIPS HD9358/11")                                                                      # Заполнение найденого поля
            driver.find_element_by_css_selector(search_button).click()                                                    # Клик по кнопке поиска
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "base_image")))                         # Ожидание появления картинки

            result = driver.current_url                                                                                   # Определение текущего урла
            self.assertEqual(result, result_page)                                                                         # Сравнение ожидаемого урла с фактического

        except NoSuchElementException:                                                                                    # кетчи на случай ошибок
            self.fail("Element missing")

        except TimeoutException:
            self.fail("Timeout")

        finally:
            driver.close()                                                                                                # Блок, который выполнится в любом случае

    # Добавление в корзину
    def test_run4(self):

        driver = self.driver

        try:
            el_search = driver.find_element_by_css_selector(search_field_css)                                  # Поиск поля поиска по имени класса
            el_search.send_keys("PHILIPS HD9358/11")                                                                      # Заполнение поля
            driver.find_element_by_css_selector(search_button).click()                                                       # Поиск кнопки "поиск" по имени и клик по ней
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "topurchases")))                      # Ожидание элемента
            driver.find_element_by_name("topurchases").click()                                                            # Клик по элементу

            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                       "//*[@id='cart-popup']/div[2]/div[1]/h2")))        # Ожидание появления элемента
            driver.find_element_by_xpath("//*[@id='cart-popup']/div[2]/div[1]/h2")                                        # Поиск элемента для проверки


        except NoSuchElementException:                                                                                    # кетчи на случай ошибок
            self.fail("Element missing")

        except TimeoutException:
            self.fail("Timeout")

        finally:
            driver.close()                                                                                                # Блок, который выполнится в любом случае

    # Доступность товара
    def test_run5(self):

        driver = self.driver

        try:
            el_search = driver.find_element_by_css_selector(search_field_css)                                  # Поиск элемента "поиск" по имнеи класса
            el_search.send_keys("Intel Core i7-6900K 3.2GHz/20MB")                                                        # Ввод текста в это поле
            driver.find_element_by_css_selector(search_button).click()                                                       # Поиск кнопки "поиск" по имени и клик по ней
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "base_image")))                         # Ожидание появления картинки по айди


            driver.find_element_by_class_name("detail-unavailable")                                                       # Поиск ранее скрытого элемента


        except NoSuchElementException:                                                                                    # кетчи на случай ошибок
            self.fail("Element missing")

        except TimeoutException:
            self.fail("Timeout")

        finally:
            driver.close()                                                                                                # Блок, который выполнится в любом случае

unittest.main(testRunner=xmlrunner.XMLTestRunner(verbosity=2, failfast=False, output='C:\\Work\\Jenkins\\workspace\\Rozetka\\test-reports'))

