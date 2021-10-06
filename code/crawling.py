from selenium import webdriver
from time import sleep
URL = 'https://komsa.or.kr/prog/psnShip/kor/sub03_0204/list.do'
import pickle
driver = webdriver.Chrome('/Users/hanboyoung/Documents/2021/1.Datascience/4.Projects/데이터/chromedriver')
driver.get(url=URL)
sleep(3)

#목록마다 들어가서 정보 받아오기
#전체 페이지 이동하기
def start():
    datas=[]
    for a in range(0,3):
        print(a)
        for j in range(3,14):
            l = '//*[@id="txt"]/div[2]/div/div/ul/li['+str(j)+']/a'
            if j !=3:
                driver.find_element_by_xpath(l).click()
            
            for i in range(1,7):
                loc = '#txt > div.ui-images__list > ul > li:nth-child('+str(i)+') '
                try:
                    driver.find_element_by_css_selector(loc).click()
                except:
                    with open('data.pickle','wb') as f:
                        pickle.dump(datas,f)
                        driver.close()
                        return
                sleep(2)

                #정보 받아오기
                ##선명, 톤수, 사이즈
                title = driver.find_element_by_css_selector('#txt > div.photo_wrap.typeB > div > div.info_box > strong').text
                tons = driver.find_element_by_css_selector('#txt > div.photo_wrap.typeB > div > div.info_box > ul > li:nth-child(1)').text
                size = driver.find_element_by_css_selector('#txt > div.photo_wrap.typeB > div > div.info_box > ul > li:nth-child(2)').text

                info = [title, tons, size]
                ##선형, 선종, 속력, 기관, 항해구역, 여객정원, 항로명, 선사
                for k in range(1,9):
                    loc_='#txt > div.ui.ui-object.type1 > div > div:nth-child('+str(k)+') > div'
                    info.append(driver.find_element_by_css_selector(loc_).text)
                datas.append(info)
                #끝나면 다음 i로 들어가기
                driver.back()
start()
