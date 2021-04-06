import random
import time

from selenium import webdriver

url = 'https://www.wenjuan.com/s/UZBZJvG0Jy/'
driver = webdriver.Firefox()

max_score = [0, 20, 15, 10, 10, 5, 10, 10, 10, 5, 5]
min_score = [0.75 * score for score in max_score]
mu = [(max_score[i] + min_score[i]) / 2 for i in range(len(max_score))]
sigma = [(max_score[i] - min_score[i]) / 6 for i in range(len(max_score))]

for room_id in range(501, 520):
    driver.get(url)
    time.sleep(1)
    inputboxes = driver.find_elements_by_css_selector('div.matrix > input.blank.option')
    for index, inputbox in enumerate(inputboxes):
        inputbox.clear()
        if index == 0:
            inputbox.send_keys(room_id)
        else:
            random_score = round(random.gauss(mu[index], sigma[index]))
            inputbox.send_keys(max(random_score, max_score[index]))
    subumit_button = driver.find_element_by_css_selector('#next_button')
    subumit_button.click()
    print('宿舍 {} 提交成功'.format(room_id))

driver.quit()
print('501-519宿舍全部提交成功')
