# import unittest
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

# # obs.: para o teste rodar corretamente, esteja com o codigo rodando em outro terminal :)

# # teste inicial do estudo de TDD
# # browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# # browser.get('http://localhost:8000')
# # assert 'To-Do' in browser.title, 'Browser title was ' + browser.title

# class NewVisitorTest(unittest.TestCase):
#     # setUp e tearDown são métodos especiais executados antes e depois de cada teste
#     # nesse caso, eles estao iniciando e encerrando o navegador
#     def setUp(self):
#         self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#     def tearDown(self):
#         self.browser.quit()

#     def test_can_start_a_new_list_and_retrieve_later(self):
#         self.browser.get('http://127.0.0.1:8000')

#         self.assertIn('To-Do', self.browser.title)

# if __name__ == '__main__':
#     unittest.main(warnings='ignore')

