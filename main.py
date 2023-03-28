from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
import time

# 예약 사이트 URL
url = "https://yeyak.seoul.go.kr/web/search/selectPageListDetailSearchImg.do?code=T100&dCode=T108"

# 브라우저 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") # 창 최대화
options.add_argument("--disable-notifications") # 브라우저 알림 제거

# 크롬 드라이버 실행
driver = webdriver.Chrome(options=options)
driver.get(url)

# 로그인 정보 입력
username = driver.find_element_by_name("me2me2kr") # 로그인 아이디 입력란
password = driver.find_element_by_name("889488ss!!") # 로그인 비밀번호 입력란
username.send_keys("your_username")
password.send_keys("your_password")

# 로그인 버튼 클릭
login_button = driver.find_element_by_xpath("//button[contains(text(), '로그인')]")
login_button.click()

# 예약 페이지로 이동
driver.get("https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S230316105228647450&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value=")

# 예약 일자 선택
reservation_date = driver.find_element_by_name("date") # 예약 일자 선택란
reservation_date.send_keys("yyyy-mm-dd") # 원하는 날짜 입력

# 인원 수 선택
num_people = driver.find_element_by_name("people") # 예약 인원 선택란
num_people.send_keys("2") # 예약할 인원 수 입력

# 예약 버튼 클릭
reservation_button = driver.find_element_by_xpath("//button[contains(text(), '예약하기')]")
reservation_button.click()

# 예약 확인 페이지에서 예약 완료 버튼 클릭
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '예약완료')]"))
    )
    element.click()
except:
    print("예약에 실패하였습니다.")

# 브라우저 종료
driver.quit()