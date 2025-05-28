import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase, Client
from django.contrib.auth import get_user_model
import core.settings as settings

from apps.home.api_functions import get_servers, delete


class TestStartServerIntegration(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Client()

        cls.password = '43faasf3qRa)8@.a'

        cls.user = get_user_model().objects.create_user(
            username='testuser',
            password=cls.password
        )

        for server in get_servers(cls.user.username):
            delete(cls.user.username, server["NAME"])

        super().setUpClass()
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # Close the browser window
        super().tearDownClass()

    def test_login(self):
        self.driver.get(f"{self.live_server_url}/")

        # 2. Interact with the form elements
        username_field = self.driver.find_element(By.ID, "id_username")
        password_field = self.driver.find_element(By.ID, "id_password")
        submit_button = self.driver.find_element(By.NAME, "login")

        # Fill in the form
        username_field.send_keys(self.user.username)
        password_field.send_keys(self.password)

        submit_button.click()

        time.sleep(1)

        available_servers = self.driver.find_elements(By.ID, "available_server_list")
        self.assertEqual(len(available_servers), 0)

    def test_create_server(self):
        self.test_login()

        create_button = self.driver.find_element(By.ID, "create")
        create_button.click()

        time.sleep(1)

        name_field = self.driver.find_element(By.ID, "name")
        port_field = self.driver.find_element(By.ID, "PORT")
        version_field = self.driver.find_element(By.ID, "VERSION")
        mode_field = self.driver.find_element(By.ID, "MODE")
        memory_field = self.driver.find_element(By.ID, "MEMORY")
        motd_field = self.driver.find_element(By.ID, "MOTD")

        name_field.send_keys("testserver")
        port_field.send_keys("25565")
        version_field.send_keys("1.16.5")
        mode_field.send_keys("survival")
        memory_field.send_keys("2G")
        motd_field.send_keys("just a testserver")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(1)

        available_servers = self.driver.find_elements(By.ID, "available_server_list")
        self.assertEqual(len(available_servers), 1)
        created_server = available_servers[0]
        self.assertTrue("testserver" in created_server.text)
        self.assertTrue(f"{settings.DISPLAY_SERVER_IP}:25565" in created_server.text)
        self.assertTrue("1.16.5" in created_server.text)

    def test_start_server(self):
        self.test_create_server()

        available_servers = self.driver.find_elements(By.ID, "available_server_list")
        self.assertEqual(len(available_servers), 1)
        created_server = available_servers[0]
        created_server.find_element(By.NAME, "start_button").click()

        time.sleep(3)

        running_servers = self.driver.find_elements(By.ID, "running_server_list")
        self.assertEqual(len(running_servers), 1)

        available_servers = self.driver.find_elements(By.ID, "available_server_list")
        self.assertEqual(len(available_servers), 0)


