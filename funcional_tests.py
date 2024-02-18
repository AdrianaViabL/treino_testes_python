import time
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# obs.: para o teste rodar corretamente, esteja com o codigo rodando em outro terminal :)

# teste inicial do estudo de TDD
# browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# browser.get('http://localhost:8000')
# assert 'To-Do' in browser.title, 'Browser title was ' + browser.title

class NewVisitorTest(unittest.TestCase):
    # setUp e tearDown são métodos especiais executados antes e depois de cada teste
    # nesse caso, eles estao iniciando e encerrando o navegador
    def setUp(self):
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_new_list_and_retrieve_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000')
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list


if __name__ == '__main__':
    unittest.main(warnings='ignore')

