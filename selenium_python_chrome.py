# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)


from selenium.webdriver import ActionChains
# импортируем необходимые библиотеки и элементы
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# создаем и настраиваем экземпляр driver класса webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# создаем переменную содержащую базовую ссылку и открываем её с помощью созданного ранее driver
base_url = 'http://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

# создаем переменную для поля ввода даты, и очищаем его
date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
date_input.send_keys(Keys.CONTROL + 'a')
date_input.send_keys(Keys.DELETE)
time.sleep(1)

# подставляем в поле ввода текущую дату +10 дней
current_date = datetime.now()
test_date = (current_date + timedelta(days=10)).strftime("%m.%d.%Y")
date_input.send_keys(test_date)