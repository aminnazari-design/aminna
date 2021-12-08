from selenium import webdriver
# import requests
import bs4



options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.headless = True
# from webdriver_manager.chrome import GeckoDriverManager
driver = webdriver.Chrome(chrome_options=options)

# url = "https://amazon.com"
# driver.get(url)
def get_url(search_term):
    template = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={}"
    search_term = search_term.replace(" " , "+")
    url = template.format(search_term)
    url+='&page{}'
    return url
# url = get_url(search_term)
# print(url)

# results  = soup.find_all('div' , {'data-component-type' : 's-search-result'})
# item = results[0]



# def extractor(item):
#     atag = item.h2.a
#     description  = atag.text.strip()
#     url  = "http://www.amazon.com" + atag.get("href")
#     driver.get(url)

#     price_parent = item.find("span" , 'a-price')
#     price = price_parent.find('span' , 'a-offscreen').text
#     rating = item.i.text
#     review = item.find('span' ,{'class': 'a-size-base' , 'dir':'auto'} )
#     soup2 = bs4.BeautifulSoup(driver.page_source , 'html.parser')
#     pic = soup2.find('img' , {'class' : 'a-dynamic-image a-stretch-horizontal'})
#     result = (description ,price , pic , rating , review ,url)
#     return result
# records = []
# results  = soup.find_all('div' , {'data-component-type' : 's-search-result'})
# for item in results:
#     records.append(extractor(item))

def extractor(item):
    # print(item)
    atag = item.h2.a
    description  = atag.text.strip()
    # print(description)
    
    try :
        price_parent = item.find("span" , 'a-price')
        price = price_parent.find('span' , 'a-offscreen').text
    except AttributeError:
        return


    pic = item.find('img'  , {'class': 's-image'}).get('src')
    try:
        rating = item.i.text
        # review = item.find('span' ,{'class': 'a-size-base' , 'dir':'auto'} )
    except AttributeError:
        rating = ''
        # review = ''
    url  = "http://www.amazon.com" + atag.get("href")
    # driver.get(url)
    # soup2 = bs4.BeautifulSoup(driver.page_source , 'html.parser')
    # pic = soup2.find('img' , {'class' : 'a-dynamic-image a-stretch-horizontal'}).get("src")
    # result = {description : description ,price = price , pic , rating , review ,url}
    result ={}
    result['description'] = description
    result['price'] = price
    result['pic'] = pic
    result['rating'] = rating
    # result['review'] = review
    return result

# data = extractor(results[0])
# print(data)
def main_work(name , num):
    records = []

    url = get_url(name)
    
    for page in range(1,num):

        driver.get(url.format(page))
        soup = bs4.BeautifulSoup(driver.page_source , 'html.parser')
        
        results  = soup.find_all('div' , {'data-component-type' : 's-search-result'})
        # for i in range(0 , 10) :
        for item in results:

            record = extractor(item)
            if record:
                records.append(record)
    # driver.close()
    # print(records.__len__)
    return records
# main_work("headphone")







