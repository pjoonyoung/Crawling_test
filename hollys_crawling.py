from bs4 import BeautifulSoup
import urllib.request

result = [] # 작업결과를 저장할 빈 리스트 선언

for page in range(54,55):
    hollys_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' %page
    print(hollys_url)
    hollys_html = urllib.request.urlopen(hollys_url)
    soupHollys = BeautifulSoup(hollys_html, 'html.parser') # 호출 결과값을 파싱한 html을 저장
    tag_tbody = soupHollys.find('tbody')
    # print(tag_tbody)
    tag_tr = tag_tbody.find_all('tr')
    # print(tag_tr)
    for store in tag_tr: # 각 페이지당 10개의 대리점 정보가 store 저장되어 추출
        print(len(store))
        store_td = store.find_all('td') # 각 tr 내의 td 정보를 리스트로 추출하여 저장
        print(len(store_td))
        store_sido = store_td[0].string # 대리점의 시,도 추출
        store_name = store_td[1].string # 대리점의 이름 추출
        store_address = store_td[3].string # 대리점의 주소 추출
        store_phone = store_td[5].string # 대리점의 전화번호 추출

        result.append([store_name]+[store_sido]+[store_address]+[store_phone])

    # print(result)