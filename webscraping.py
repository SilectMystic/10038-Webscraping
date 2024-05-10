from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = ("https://www.doordash.com/store/mcdonald's-southside-837652/?cursor=eyJzZWFyY2hfaXRlbV9jYXJvdXNlbF9jdXJzb3IiOnsicXVlcnkiOiJtYyBkb24iLCJpdGVtX2lkcyI6W10sInNlYXJjaF90ZXJtIjoibWMgZG9uIiwidmVydGljYWxfaWQiOi05OTksInZlcnRpY2FsX25hbWUiOiJhbGwifSwic3RvcmVfcHJpbWFyeV92ZXJ0aWNhbF9pZHMiOlsxLDE5Nl19&pickup=false")
# result = requests.get(url).text
driver = webdriver.Chrome()
driver.get(url)
page = BeautifulSoup(driver.page_source, 'lxml')
x = 0
while True:
    x += 1
    driver.execute_script('scrollBy(0,300)')
    div = page.find_all('div', attrs={'data-anchor-id':'MenuItem'})
    print(page)
    if x == 70:
        break
driver.quit()