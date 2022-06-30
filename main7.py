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





    with open("data/duel.html", encoding="utf_8_sig") as file:
        data = file.read()
        
# newline=''  убирает пустые строки
    with open(f"data/draw.csv", "w", encoding="utf_8_sig", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "date",
                "number",
                "a",
                "b",
                "c",
                "d"
            )
        )


#собираем цифры с сайта
    soup = BeautifulSoup(data, "lxml")

    dr = soup.find_all("div", class_="elem")
    draw = []
#берём в списке единственный элемент под индексом 0 и вынимаем из него текст       
    for r in dr: 
        date = r.find_all("div", class_="draw_date")[0].text
        num = r.find_all("a")[0].text
        items_right = r.find_all("b", class_="right") #собираем правые цифры
        if len(items_right) != 0:# проверяем чтобы список не был пуст, пустые списки отсеиваем.        
            a = items_right[0].text.strip()
            b = items_right[1].text.strip()    

        items_left = r.find_all("b", class_="left") #собираем правые цифры
        if len(items_left) != 0:# проверяем чтобы список не был пуст, пустые списки отсеиваем.        
            c = items_left[0].text.strip()
            d = items_left[1].text.strip()
            draw.append(
              {
                "date": date,
                "number": num,
                "a": a,
                "b": b,
                "c": c,
                "d": d
              }
            )
            
# newline=''  убирает пустые строки          
            with open(f"data/draw.csv", "a", encoding="utf_8_sig", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(           

                    (
                      date,
                      num,
                      a,
                      b,
                      c,
                      d
                   )
                )    

            
        
          
        
def main():
    get_all_pages()



if __name__ == '__main__':
    main()
