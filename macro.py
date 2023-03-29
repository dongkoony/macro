from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess



# By. 모듈 테스트 로직

# By.selectPeriod = (By.CSS_SELECTOR, '#selectPeriod')
# By.selectRsvTime = (By.CSS_SELECTOR, '#selectRsvTime')
# By.userId = (By.CSS_SELECTOR, '#userId')
# By.userPwd = (By.CSS_SELECTOR, '#userPwd')

# 예약 사이트 URL
url = "https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S230314055802763586&code=T100&dCode=&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EA%B3%84%EB%82%A8&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value="

# 테스트 네이버 도메인
# url = "https://www.naver.com"


# 브라우저 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") # 창 최대화
options.add_argument("--disable-notifications") # 브라우저 알림 제거
options.add_argument("--remote-debugging-port=9222") # 디버깅 모드로 진입
options.add_argument("--disable-blink-features=AutomationControlled") # 자동화 소프트웨어 차단 기능 해제
options.add_argument("disable-infobars")
options.add_argument("enable-automation")
# options.AddAdditionalCapability("useAutomationExtension", false);
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.147 Safari/537.36")
options.add_argument("app-version=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.147 Safari/537.36")

# 크롬 드라이버 실행
driver = webdriver.Chrome(options=options)
driver.get(url)

# 예약 가능한 날짜 선택
date_select = Select(driver.find_element(By.selectPeriod)) # 예약 날짜 선택 셀렉트 박스
# date_select = Select(driver.find_element(By.XPATH, '//select[@id="selectPeriod"]')) # 예약 날짜 선택 셀렉트 박스
date_select.select_by_index(1) # 두번째(내일) 날짜 선택

# 예약 가능한 시간 선택
time_select = Select(driver.find_element(By.selectRsvTime)) # 예약 시간 선택 셀렉트 박스
time_select.select_by_index(1) # 두번째 시간(09:00~10:00) 선택

# 예약 버튼 클릭
reservation_button = driver.find_element_by_xpath("//a[@title='예약신청']")
reservation_button.click()

# 로그인 정보 입력
id_input = driver.find_element(By.userId)
pw_input = driver.find_element(By.userPwd)
id_input.send_keys("your_id") # 여기에 본인의 아이디를 입력하세요.
pw_input.send_keys("your_password") # 여기에 본인의 비밀번호를 입력하세요.

# 로그인 버튼 클릭
login_button = driver.find_element_by_xpath("//a[@title='로그인']")
login_button.click()

# 예약 진행
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='예약진행']"))
    )
    element.click()
except:
    print("예약에 실패하였습니다.")

# 예약 확인 페이지에서 예약 완료 버튼 클릭
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='예약완료']"))
    )
    element.click()
except:
    print("예약에 실패하였습니다.")

# 브라우저 닫기
driver.close()
