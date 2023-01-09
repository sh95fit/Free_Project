from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
from info import email, password

chrome = webdriver.Chrome("./Prac4_OracleCloud_Auto/chromedriver.exe")
url = "https://www.oracle.com/kr/cloud/free/"
wait = WebDriverWait(chrome, 20)


def find_present(css_selector):
    # 내부를 튜플로 받아야 한다!
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


def finds_present(css_selector):
    find_present(css_selector)
    return chrome.find_elements(By.CSS_SELECTOR, css_selector)


def find_visible(css_selector):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))


def finds_visible(css_selector):
    find_visible(css_selector)
    return chrome.find_elements(By.CSS_SELECTOR, css_selector)


try:

    chrome.get(url)
    time.sleep(5)

    iframes = chrome.find_elements(By.TAG_NAME, 'iframe')

    chrome.switch_to.frame(f"{iframes[1].get_attribute('id')}")

    find_visible(
        "body > div:nth-child(16) > div.mainContent > div > div.pdynamicbutton > a.required").click()

    find_visible("#gwt-debug-close_id").click()

    chrome.switch_to.parent_frame()

    find_visible("body > div.f20w1 > section.rh03.rh03v3.rw-theme-30bg.bgimgw1 > div.rh03w1.cwidth > div.herotitle.rh03twocol > div.rh03col1 > div > div.obttn1 > a").click()

    find_visible("#cloudAccountName").send_keys("h95fit")

    find_visible("#cloudAccountButton").click()

    find_visible("#submit-domain").click()

    find_visible("#idcs-signin-basic-signin-form-username").send_keys(email)
    find_visible(
        "#idcs-signin-basic-signin-form-password\|input").send_keys(password)

    find_visible("#idcs-signin-basic-signin-form-submit > button").click()

    # 로그인 후 instance 이동
    time.sleep(10)

    find_visible("#nav-menu-button").click()

    find_visible("#container-elements1-0 > div:nth-child(1) > div > a").click()

    # 인스턴스 연결 탭으로 이동
    time.sleep(5)

    chrome.switch_to.frame("sandbox-compute-container")

    find_visible("#__tab10 > a").click()

    find_visible(
        "div.oui-savant__compartment-select__tree-dropdown div a").click()

    find_visible("div.infinite-scroll-component li.node.tree span").click()

    find_visible(
        "#oui-savant__listing-content > div:nth-child(2) > div > div.chakra-stack > button.chakra-button.css-ria1w7").click()

    # + 선택 후 목록에서 선택하기 (목록에서 선택이 적용되지 않음!)
    # find_visible(
    #     "div.dropdown-content ul.root div.infinite-scroll-component li > i.toggle.collapsed").click()

    # time.sleep(3)

    # find_visible(
    #     "div.dropdown-content ul.root div.infinite-scroll-component li > i.toggle.collapsed").click()

    # find_visible(
    #    "div.dropdown-content ul.root li:nth-child(2)").send_keys(Keys.ENTER)

    # Create compute instance (인스턴스 생성 페이지)

    # OS image 선택
    time.sleep(5)

    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Contents > div.fullscreen-two-thirds-width > div > fieldset:nth-child(5) > div.oui-legend-wrapper.oui-flex.oui-flex-between.oui-flex-top > div.oui-margin-left.oui-flex.oui-flex-top.oui-flex- > button").click()

    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Contents > div.fullscreen-two-thirds-width > div > fieldset:nth-child(5) > div.oui__fieldset-content.oui-fieldset-content-top-zero-padding > div:nth-child(1) > span > div > div.create-instance-dialog__picker-result__box > div.create-instance-dialog__picker-result__button-container > button").click()

    find_visible("#oui-savant__viewstack__container > div:nth-child(3) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--medium.oui-savant__Panel__animate > div.oui-savant__Panel--Contents > div.oui-margin-medium-top > div > section > div > div > table > tbody > tr:nth-child(1) > td.oui-table-shrink > input").click()

    find_visible("#oui-savant__viewstack__container > div:nth-child(3) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--medium.oui-savant__Panel__animate > div.oui-savant__Panel--Footer > button.oui-button.oui-button-primary").click()

    # Shape 선택
    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Contents > div.fullscreen-two-thirds-width > div > fieldset:nth-child(5) > div.oui__fieldset-content.oui-fieldset-content-top-zero-padding > div:nth-child(1) > div:nth-child(3) > div > div.oui-margin-medium-left > button").click()

    find_visible(
        "#oui-savant__viewstack__container > div:nth-child(3) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--medium.oui-savant__Panel__animate > div.oui-savant__Panel--Contents > div > div:nth-child(4) > div.oui-display-label-padding > div > div:nth-child(3) > div").click()

    find_visible("#oui-savant__viewstack__container > div:nth-child(3) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--medium.oui-savant__Panel__animate > div.oui-savant__Panel--Contents > div > section > div > div > table > tbody > tr:nth-child(1) > td.oui-table-shrink > input").click()

    # find_visible(
    #     "div.oui-display-label-padding div.oui-margin-large-left input").click()

    # time.sleep(1)

    # find_visible(
    #     "div.oui-display-label-padding div.oui-margin-large-left input").clear()

    # time.sleep(5)

    find_visible(
        "div.oui-display-label-padding div.oui-margin-large-left input").send_keys("\b4")

    # find_visible(
    #     "div.slider-VM_Standard_A1_Flexmemory div.oui-margin-large-left input").click()

    # time.sleep(1)

    # find_visible(
    #     "div.slider-VM_Standard_A1_Flexmemory div.oui-margin-large-left input").clear()

    # time.sleep(5)

    find_visible(
        "div.slider-VM_Standard_A1_Flexmemory div.oui-margin-large-left input").send_keys("\b\b24")

    find_visible("#oui-savant__viewstack__container > div:nth-child(3) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--medium.oui-savant__Panel__animate > div.oui-savant__Panel--Footer > button.oui-button.oui-button-primary").click()

    # Networking 선택
    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Contents > div.fullscreen-two-thirds-width > div > fieldset:nth-child(6) > div.oui-legend-wrapper.oui-flex.oui-flex-between.oui-flex-top > div.oui-margin-left.oui-flex.oui-flex-top.oui-flex- > button").click()

    find_visible(
        "#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Contents > div.fullscreen-two-thirds-width > div > fieldset:nth-child(6) > div.oui__fieldset-content.oui-fieldset-content-top-zero-padding > div > div:nth-child(4) > div > span > span.oui-savant__compartment-scoped-field-toggle-link.oui-react-form-label > a").click()

    find_visible("#rdts1-0-0_li > label > span").click()

    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Contents > div.fullscreen-two-thirds-width > div > fieldset:nth-child(6) > div.oui__fieldset-content.oui-fieldset-content-top-zero-padding > div > div:nth-child(8) > div > span > span.oui-savant__compartment-scoped-field-toggle-link.oui-react-form-label > a").click()

    find_visible("#rdts2-0-0_li > label > span").click()

    # SSH 인증키 받기
    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Contents > div.fullscreen-two-thirds-width > div > fieldset:nth-child(7) > div.oui__fieldset-content.oui-fieldset-content-top-zero-padding > div > div.oui-margin-bottom.oui-form-field.oui-react-form-field > div.oui-display-label-padding > div > div.oui-info-block__content > div.key-pair-wrapper > div > span.oui-margin-right > button").click()

    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Contents > div.fullscreen-two-thirds-width > div > fieldset:nth-child(7) > div.oui__fieldset-content.oui-fieldset-content-top-zero-padding > div > div.oui-margin-bottom.oui-form-field.oui-react-form-field > div.oui-display-label-padding > div > div.oui-info-block__content > div.key-pair-wrapper > div > span:nth-child(2) > button").click()

    # boot 볼륨 설정
    find_visible(
        "input[name='enableCustomBootVolumeSize']").click()

    find_visible(
        "section.oui-section div.oui-margin-bottom.oui-form-field.oui-react-form-field div.oui-display-label-padding input[id^='bootVolumeSize-']").send_keys("\b\b100")

    find_visible("input[name='uhpSlider']").send_keys("\b\b120")

    # 생성하기!

    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Footer > button.oui-button.oui-button-primary").click()

    time.sleep(3)

    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Footer > button.oui-button.oui-button-primary").click()

    time.sleep(3)

    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Footer > button.oui-button.oui-button-primary").click()

    time.sleep(3)

    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Footer > button.oui-button.oui-button-primary").click()

    time.sleep(3)

    find_visible("#oui-savant__viewstack__container > div:nth-child(2) > div:nth-child(2) > div > div.oui-savant__Panel.oui-savant__Panel--large.oui-savant__Panel__animate > div.oui-savant__Panel--Footer > button.oui-button.oui-button-primary").click()

    time.sleep(5)

    chrome.quit()

except:
    pass
    chrome.quit()
