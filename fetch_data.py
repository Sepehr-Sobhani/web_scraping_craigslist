from bs4 import BeautifulSoup as bs
import requests
import mysql.connector


cnx = mysql.connector.connect(user='root', password='',
                            host='127.0.0.1',
                            database='Craigslist')

cursor = cnx.cursor()

cursor.execute("CREATE TABLE mytable (price INT, bedroom INT, space INT NOT NULL, location TEXT NOT NULL);")


page_number = 0
price_list = []
housing_bedroom = []
housing_space = []
area = []

while page_number < 3000:
    URL = 'https://vancouver.craigslist.org/search/apa'
    page = requests.get(URL)
    soup = bs(page.text, 'html.parser')
    overall_result = soup.select('.result-row')

    for i in range(len(overall_result)):
        price = overall_result[i].select_one(".result-price")
        bedroom = overall_result[i].select_one(".housing")      
        hood = overall_result[i].select_one(".result-hood")

        if str(price.getText()) == "$0":
            continue
        elif bedroom == None or "ft" not in bedroom.getText() or "br" not in bedroom.getText():
            continue
        elif hood == "" or hood == None:
            continue
        else:
            price_list.append(price.getText().replace("$", ""))
            housing_bedroom.append(bedroom.getText().strip().split("-")[0].strip().replace("br", ""))
            housing_space.append(bedroom.getText().strip().split("-")[1].strip().replace("ft2", ""))
            area.append(hood.getText().strip())
    
    page_number += 120
    URL = URL + "?s=" + str(page_number)



for i in range(len(price_list)):
    query_string = "INSERT IGNORE INTO mytable (price, bedroom, space, location) VALUES ('%s', '%s', '%s', '%s');" % (price_list[i], housing_bedroom[i], housing_space[i], area[i])
    cursor.execute(query_string)

cnx.commit()

cnx.close()
