from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path
import time
from appium.webdriver.webdriver import ExtensionBase
import os

auth_token = os.environ.get("HS_TOKEN")
session_id = ''

class OCRCommand(ExtensionBase):
    def method_name(self):
        return 'ocr_command'
    def ocr_command(self, argument):
        return self.execute(argument)['value']
    def add_command(self):
        return ('post', '/session/$sessionId/appium/ocr'.format(session_id))


title = "abc news live"
# GTV Environment

dc={
    "deviceName": "Chromecast",
    "udid": "27301HFDD7MQGM",
    "automationName": "uiautomator2",
    "appPackage": "com.google.android.youtube.tv",
    "platformName": "android",
    "appActivity": "com.google.android.apps.youtube.tv.activity.ShellActivity",
    "headspin:controlLock":'true',
    # "headspin:capture.video":"true",
    "headspin:appiumVersion": "2.0.0-beta.52",
    "headspin:appiumPlugins": ["ocr"]

}
driver = webdriver.Remote(f"https://dev-ca-tor-0.headspin.io:7031/v0/{auth_token}/wd/hub", dc, extensions=[OCRCommand])


print("Driver started")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((AppiumBy.ID, "android:id/content")))

time.sleep(5)

#Navigate to Movie
print(f'navigating to {title}')





driver.press_keycode(21);
driver.press_keycode(21);

driver.press_keycode(19);
driver.press_keycode(66);


time.sleep(5)
print("running ocr command")
result = driver.ocr_command({})

print("switching context")
contexts = driver.contexts
driver.switch_to.context(contexts[1])
try:
    # result = driver.find_elements(AppiumBy.XPATH,"//lines/item[text() = 'abc news live stream')]")
    result=driver.find_element(AppiumBy.XPATH, '//item[contains(text(), "abc news live stream")]')
    result.click()
except Exception as e:
    print(e)
finally:
    driver.quit()


