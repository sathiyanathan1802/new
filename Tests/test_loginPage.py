from Pages.LoginPage import LoginPage
from Tests.test_base import Test_Base
from configuration.config import TestData


class TestLogin(Test_Base):

      def test_loginpagetitle(self):
          self.loginpage=LoginPage(self.driver)
          actualtitle=self.loginpage.get_login_pagetitle()
          expectedtitle="HubSpot Login"
          assert actualtitle==expectedtitle

      def test_login(self):
          self.loginpage = LoginPage(self.driver)
          self.loginpage.do_login(TestData.USERNAME,TestData.PASSWORD)

