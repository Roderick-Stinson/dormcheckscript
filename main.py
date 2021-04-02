from selenium import webdriver
import time

url = str('https://www.wenjuan.com/s/UZBZJvG0Jy/')
t = int(10)
score_list = [20, 13, 8, 10, 3, 7, 10, 10, 4, 3]
# 设置提交问卷次数
for times in range(501, 519):
    driver = webdriver.Firefox()
    driver.get(url)
    # 定位所有的问卷问题
    questions = driver.find_elements_by_css_selector('div.matrix')
    counter = 0
    for question in questions:
        blank_potion = question.find_element_by_css_selector('.blank.option')
        blank_potion.clear()
        if counter == 0:
            blank_potion.send_keys(times)
        else:
            blank_potion.send_keys(score_list[counter-1])
        counter += 1

    print('{}班提交成功'.format(str(501 + int(counter))))
    subumit_button = driver.find_element_by_css_selector('#next_button')
    subumit_button.click()

    # 延迟问卷结果提交时间，以免间隔时间太短而无法提交
    time.sleep(1)
    driver.quit()
