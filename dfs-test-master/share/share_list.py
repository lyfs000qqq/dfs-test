from lib import driver_instance
import time
from selenium.webdriver.common.keys import Keys


class Share():

    def __init__(self):
        driver_instance.open()
        self.driver = driver_instance.driver

    def get_share(self):
        self.driver.implicitly_wait(10)
        # time.sleep(3)
        self.driver.find_element_by_xpath("//span[text()=' 共享管理']").click()
        self.driver.find_element_by_id('share').click()
        time.sleep(5)

    def add_share(self):
        self.driver.find_element_by_id('share_add').click()

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//div[@id = 'share_add_name']/input").send_keys(driver_instance.share_name)
        # print (driver_instance.share_name)
        time.sleep(2)

        self.driver.find_element_by_xpath("//div[@id = 'share_add_volume']/input").click()
        self.driver.find_element_by_xpath("//span[text() = '%s']"%driver_instance.share_volume).click()
        time.sleep(2)

        self.driver.find_element_by_xpath("//div[@id = 'share_add_user']/input").click()
        self.driver.find_element_by_xpath("//span[text() = '%s']"%driver_instance.owner).click()
        time.sleep(2)

        self.driver.find_element_by_xpath("//div[@id = 'share_add_quota']/input").send_keys(driver_instance.share_size)

        self.driver.find_element_by_xpath("//input[@value = 'CIFS']").click()
        self.driver.find_element_by_xpath("//input[@value = 'NFS']").click()
        self.driver.find_element_by_xpath("//input[@value = 'FTP']").click()
        time.sleep(2)

        inputs = self.driver.find_elements_by_xpath("//input[@type = 'checkbox']")
        for input in inputs:
            if input.is_selected():
                print ('pass')
            else:
                input.send_keys(Keys.SPACE)
                time.sleep(1)

        self.driver.find_element_by_xpath("//button[@id = 'share_add_submit']").click()

    def close(self):
        driver_instance.close()


share = Share()
share.get_share()
share.add_share()
# user.close()