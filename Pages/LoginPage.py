from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from configuration.config import TestData


class LoginPage(BasePage):

    '''collect all the locators related to login page'''

    EMAIL= (By.ID,"username")
    PWD= (By.ID,"password")
    LOGIN= (By.ID,"loginBtn")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASEURL)

    '''Page actions for Login page'''

    ''' This method is used to get the page title '''

    def get_login_pagetitle(self):
        return self.driver.title

    '''This method will do login action'''
    def do_login(self,username, password):
        self.do_sendKeys(self.EMAIL,username)
        self.do_sendKeys(self.PWD,password)
        self.do_click(self.LOGIN)

        print("first commit")
        print("git bash here")
        print("its woring")
        print("its good")
        







