import csv
import json
import requests
from bs4 import BeautifulSoup



def get_all_pages():


    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    
#определяем переменные
#    r = requests.get(url="https://www.stoloto.ru/duel/archive", headers=headers)
#    src = r.text

    
#создаем папку
#    if not os.path.exists("data"):
#        os.mkdir("data")

#    with open("data/page_1.html", "w", encoding="utf_8_sig") as file:
#        file.write(r.text)



    with open("data/page_1.html", encoding="utf_8_sig") as file:
        data = file.read()


        
#собираем цифры с сайта
    soup = BeautifulSoup(data, "lxml")
    items= soup.find_all("span", class_="zone")
    left_right = []
    right = []    
    for i in items: 
        items_left = i.find_all("b", class_="left")# собираем левые цифрры
        if len(items_left) != 0:# проверяем чтобы список не был пуст, пустые списки отсеиваем.        
            a = items_left[0].text.strip()
            b = items_left[1].text.strip()            
            left_right.append(
                  {'1': a,
                   '2': b
                  }
                )

            with open(f"data/duel.csv", "a", encoding="utf_8_sig") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                    a,
                    b
                    )
                 )

            
    for i in items:        
        items_right = i.find_all("b", class_="right") #собираем правые цифры
        if len(items_right) != 0:# проверяем чтобы список не был пуст, пустые списки отсеиваем.
            c = items_right[0].text.strip() # забираем [0] элемент в списке добавляем метод text чтобы отсеять ненужные символы
            d = items_right[1].text.strip() # метод strip() отсекает ненужные символы
            right.append(
                  {'3': c,
                   '4': d
                  }
               )
            
            with open(f"data/duel.csv", "a", encoding="utf_8_sig") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                    c,
                    d
                    )
                 )
            
    

                
    left_right.extend(right)
    #print(left_right)

        
def main():
    get_all_pages()



if __name__ == '__main__':
    main()

