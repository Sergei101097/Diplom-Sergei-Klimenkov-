from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from BaseApp.BasePage import BasePage


class MyStoreClickLocators:
    """AUTHENTICATION"""

    LOCATOR_MY_STORE_CLICK_ENTER = (By.CLASS_NAME, "login")
    LOCATOR_MY_STORE_CLICK_CREATE_AN_ACCOUNT = (By.ID, "SubmitCreate")
    LOCATOR_MY_STORE_EMAIL_INVALID = (By.XPATH, "//*[@id='create_account_error']/ol/li")
    LOCATOR_MY_STORE_EMAIL_ADDRESS = (By.ID, "email_create")
    LOCATOR_MY_STORE_YOUR_PERSONAL_INFORMATION = (By.CSS_SELECTOR,"#account-creation_form > div:nth-child(1) > h3")
    LOCATOR_MY_STORE_AUTHENTICATION = (By.CLASS_NAME, "page-heading")
    """YOUR PERSONAL INFORMATION"""
    LOCATOR_MY_STORE_Title = (By.CSS_SELECTOR, "#id_gender1")
    LOCATOR_MY_STORE_First_name = (By.CSS_SELECTOR, "#customer_firstname")
    LOCATOR_MY_STORE_Last_name = (By.CSS_SELECTOR, "#customer_lastname")
    LOCATOR_MY_STORE_Email = (By.CSS_SELECTOR, "#email")
    LOCATOR_MY_STORE_Password = (By.CSS_SELECTOR, "#passwd")
    LOCATOR_MY_STORE_date = (By.CSS_SELECTOR, "#days")
    LOCATOR_MY_STORE_month = (By.CSS_SELECTOR, "#months")
    LOCATOR_MY_STORE_year = (By.CSS_SELECTOR, "#years")
    LOCATOR_MY_STORE_our_news = (By.CSS_SELECTOR, "#newsletter")
    """YOUR ADDRESS"""
    LOCATOR_MY_STORE_First_name_1 = (By.XPATH, "//*[@id='firstname']")
    LOCATOR_MY_STORE_Last_name_1 = (By.XPATH, "//*[@id='lastname']")
    LOCATOR_MY_STORE_Company = (By.XPATH, "//*[@id='company']")
    LOCATOR_MY_STORE_Address = (By.XPATH, "//*[@id='address1']")
    LOCATOR_MY_STORE_Address_1 = (By.XPATH, "//*[@id='address2']")
    LOCATOR_MY_STORE_City = (By.XPATH, "//*[@id='city']")
    LOCATOR_MY_STORE_State = (By.CSS_SELECTOR, "#id_state")
    LOCATOR_MY_STORE_Zip_Postal_Code = (By.CSS_SELECTOR, "#postcode")
    LOCATOR_MY_STORE_Country = (By.CSS_SELECTOR, "#id_country")
    LOCATOR_MY_STORE_Additional_information = (By.CSS_SELECTOR, "#other")
    LOCATOR_MY_STORE_Home_phone = (By.CSS_SELECTOR, "#phone")
    LOCATOR_MY_STORE_Mobile_phone = (By.CSS_SELECTOR, "#phone_mobile")
    LOCATOR_MY_STORE_Assign_an_address_alias_for_future_reference = (By.CSS_SELECTOR, "#alias")
    LOCATOR_MY_STORE_Register = (By.CSS_SELECTOR, "#submitAccount")


class Clichome(BasePage):

    # Invalid_email_address
    def click_enter(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK_ENTER, time=20).click()

    def click_create_an_account(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK_CREATE_AN_ACCOUNT, time=20).click()

    def Invalid_email_address(self):
        inval = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_EMAIL_INVALID, time=20).text
        return inval

    # enter_my_store
    def click_email_address(self):
        facker = Faker()
        email = facker.email()
        email_address = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_EMAIL_ADDRESS, time=20)
        email_address.send_keys(email)
        return email_address

    def your_personal_information(self):
        your_personal_information = self.find_element(
            MyStoreClickLocators.LOCATOR_MY_STORE_YOUR_PERSONAL_INFORMATION, time=20
        ).text
        return your_personal_information

    # AUTHENTICATION
    def authentication(self):
        authentication = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_AUTHENTICATION, time=20).text
        return authentication

    # YOUR PERSONAL INFORMATION
    def Title(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Title, time=20).click()

    def First_name(self):
        faker = Faker()
        name = faker.last_name()
        First_name = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_First_name, time=20)
        First_name.send_keys(name)

    def Last_name(self):
        faker = Faker()
        surname = faker.first_name()
        Last_name = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Last_name, time=20)
        Last_name.click()
        Last_name.send_keys(surname)

    def Email(self):
        Email = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Email, time=20)
        Email.click()

    def password(self):
        faker = Faker()
        passwor = faker.password()
        password = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Password, time=20)
        password.send_keys(passwor)

    def date(self):
        facker = Faker()
        dat = facker.random_int(1, 25)
        date = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_date, time=20)
        date.click()
        date.send_keys(dat)
        # date.click()

    def month(self):
        facker = Faker()
        mon = facker.month_name()
        month = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_month, time=20)
        month.click()
        month.send_keys(mon)
        # month.click()

    def year(self):
        facker = Faker()
        yer = facker.year()
        year = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_year, time=20)
        year.click()
        year.send_keys(yer)
        # year.click()

    def our_news(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_our_news, time=20).click()

    # YOUR ADDRESS
    def First_name_1(self):
        First_name_1 = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_First_name_1, time=20)
        First_name_1.click()

    def Last_name_1(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Last_name_1, time=20).click()

    def Company(self, word):
        Company = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Company, time=20)
        Company.send_keys(word)

    def Address(self, word):
        Address = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Address, time=20)
        Address.send_keys(word)

    def Address_1(self, word):
        Address = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Address_1, time=20)
        Address.send_keys(word)

    def City(self):
        faker = Faker()
        cit = faker.city()
        City = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_City, time=20)
        City.send_keys(cit)

    def State(self, word):
        State = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_State, time=20)
        State.click()
        State.send_keys(word)
        State.click()

    def Zip_Postal_Code(self):
        faker = Faker()
        zip_cod = faker.zipcode()
        Zip_Postal_Code = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Zip_Postal_Code, time=20)
        Zip_Postal_Code.send_keys(zip_cod)

    def Country(self, word):
        Country = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Country, time=20)
        Country.click()
        Country.send_keys(word)
        Country.click()

    def Additional_information(self, word):
        Additional_information = self.find_element(
            MyStoreClickLocators.LOCATOR_MY_STORE_Additional_information, time=20
        )
        Additional_information.send_keys(word)

    def Home_phone(self):
        faker = Faker()
        hom_phone = faker.phone_number()
        Home_phone = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Home_phone, time=20)
        Home_phone.send_keys(hom_phone)

    def Mobile_phone(self):
        faker = Faker()
        mob_phone = faker.phone_number()
        Mobile_phone = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Mobile_phone, time=20)
        Mobile_phone.send_keys(mob_phone)

    def Assign_an_address_alias_for_future_reference(self, word):
        Assign_an_address_alias_for_future_reference = self.find_element(
            MyStoreClickLocators.LOCATOR_MY_STORE_Assign_an_address_alias_for_future_reference, time=20
        )
        Assign_an_address_alias_for_future_reference.send_keys(Keys.BACKSPACE)
        Assign_an_address_alias_for_future_reference.send_keys(Keys.BACKSPACE)
        Assign_an_address_alias_for_future_reference.send_keys(Keys.BACKSPACE)
        Assign_an_address_alias_for_future_reference.send_keys(Keys.BACKSPACE)
        Assign_an_address_alias_for_future_reference.send_keys(Keys.BACKSPACE)
        Assign_an_address_alias_for_future_reference.send_keys(Keys.BACKSPACE)
        Assign_an_address_alias_for_future_reference.send_keys(Keys.BACKSPACE)
        Assign_an_address_alias_for_future_reference.send_keys(Keys.BACKSPACE)
        Assign_an_address_alias_for_future_reference.send_keys(Keys.BACKSPACE)
        Assign_an_address_alias_for_future_reference.send_keys(Keys.BACKSPACE)
        Assign_an_address_alias_for_future_reference.send_keys(word)

    def click_register(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_Register, time=20).click()
