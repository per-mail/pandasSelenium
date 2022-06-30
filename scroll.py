from selenium import webdriver
import time
from selenium.webdriver.common.by import By



options = webdriver.ChromeOptions()

# user-agent
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

# 1 вариант написания кода для перехода в фоновый режжим
# options.add_argument("--headless")
# 2 вариант написания кода для перехода в фоновый режжим 
#options.headless = True

driver = webdriver.Chrome(
    executable_path="C:\\Users\\dfg\\Desktop\\stoloto\\chromedriver\\chromedriver.exe",
    options=options
)



def get_source_html(url):    

    #увеличиваем экран
    driver.maximize_window()
    driver.get(url=url)
    i = 1
    time.sleep(0.2)
    while i < 10:
        i += 1
        print(i)
        time.sleep(0.2)
        content = driver.find_element(By.XPATH, '//div[@class="more"]/span[@class="pseudo"]')
        content.click()
        
    
    
    
    # content = driver.find_element(By.XPATH, '//span[@class="pseudo"]/span')
    #content = driver.find_element(By.CLASS_NAME, 'pseudo')
  
    
    
    #driver.implicitly_wait(10) - альтернативная возможность для паузы.click()

    

    with open("data/page.html", "w", encoding="utf_8_sig") as file:
        file.write(driver.page_source)
        




   
def main():
    get_source_html(url="https://www.stoloto.ru/duel/archive")
       
if __name__ == "__main__":
    main()
