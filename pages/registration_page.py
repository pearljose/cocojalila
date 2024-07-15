from selenium.webdriver.common.by import By
from base.base_page import PageBase
from utilities import excelutils
class Registration(PageBase):
    def __int__(self,driver):
        super().__init__(driver)

    #Locators
    LOGIN = (By.XPATH, "//*[text()='Login']")
    CLOSE = (By.XPATH, "(//button[@class='close'])[1]")
    REGISTER1 = (By.XPATH, "//*[text()='Register']")
    REGISTER2 = (By.XPATH, "(//input[@class='btn btn-primary mr-3 mb-3'])[2]")
    ASSERTION_ELEMENT1 = (By.XPATH, "//*[text()='Register']")
    FIRST_NAME = (By.XPATH, "//input[@class='form-control name']")
    EMAIL = (By.XPATH, "(// input[@class ='form-control'])[2]")
    PASSWORD = (By.XPATH, "(//input[@class='form-control'])[3]")
    CONFIRM_PASSWORD = (By.XPATH, "(//input[@class='form-control'])[4]")
    ALREADY_REGISTERED_MSG = (By.XPATH, "//*[text()='The email has already been taken.']")
    PASSWORD_STRENGTH = (By.XPATH, "//*[text()='The password must be at least 8 characters.']")
    PASSWORD_MISMATCH = (By.XPATH, "//*[text()='The password confirmation does not match.']")

    def login(self):
        self.click(self.LOGIN)

    def close(self):
        self.click(self.CLOSE)

    def register1(self):
        self.click(self.REGISTER1)

    def register2(self):
        self.click(self.REGISTER2)

    def assert_tc1(self):
        ele = self.is_ele_displayed(self.REGISTER2)
        assert ele

    def first_name(self, firstname):
        self.click(self.FIRST_NAME)
        self.fill_text(self.FIRST_NAME, firstname)

    def enter_email(self, email):
        self.click(self.EMAIL)
        self.fill_text(self.EMAIL, email)

    def enter_password(self, password):
        self.click(self.PASSWORD)
        self.fill_text(self.PASSWORD, password)

    def confirm_password(self, confirm_password):
        self.click(self.CONFIRM_PASSWORD)
        self.fill_text(self.CONFIRM_PASSWORD, confirm_password)

    def assert_tc2(self):
        ele = self.is_ele_displayed(self.ALREADY_REGISTERED_MSG)
        assert ele

    def add(self):
        self.first_name((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 2, 1)))
        self.enter_email((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 2, 2)))
        self.enter_password((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 2, 3)))
        self.confirm_password((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 2, 4)))

    def password_strength_verification(self):
        self.first_name((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 3, 1)))
        self.enter_email((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 3, 2)))
        self.enter_password((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 3, 3)))
        self.confirm_password((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 3, 4)))

    def password_mismatch(self):
        self.first_name((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 4, 1)))
        self.enter_email((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 4, 2)))
        self.enter_password((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 4, 3)))
        self.confirm_password((excelutils.get_cell_data("excelfiles/TestData.xlsx", "sheet1", 4, 4)))

    def assert_tc3(self):
        ele = self.is_ele_displayed(self.PASSWORD_STRENGTH)
        assert ele

    def assert_tc4(self):
        ele = self.is_ele_displayed(self.PASSWORD_MISMATCH)
        assert ele
    def assert_tc5(self):
        ele = self.is_ele_displayed(self.FIRST_NAME)
        assert ele

    def assert_tc6(self):
        ele = self.is_ele_displayed(self.EMAIL)
        assert ele

    def assert_tc7(self):
        ele = self.is_ele_displayed(self.PASSWORD)
        assert ele

    def assert_tc8(self):
        ele = self.is_ele_displayed(self.CONFIRM_PASSWORD)
        assert ele

    def assert_tc9(self):
        ele = self.is_ele_displayed(self.REGISTER2)
        assert ele





