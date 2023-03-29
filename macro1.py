from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 웹드라이버 로드
driver = webdriver.Chrome()

# 사이트 접속
driver.get("https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S230314055802763586&code=T100&dCode=&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EA%B3%84%EB%82%A8&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value=")

# 예약 날짜 선택
reserve_date = "2022-04-08"
driver.find_element(By.ID, "dtmReserv").clear()  # 기존 예약 날짜 입력란 초기화
driver.find_element(By.ID, "dtmReserv").send_keys(reserve_date)

# 시간대 선택
reserve_time = "15:30~17:00"
Select(driver.find_element(By.ID, "reservTime")).select_by_visible_text(reserve_time)

# 인원 수 선택
person_num = "2"
Select(driver.find_element(By.ID, "personCnt")).select_by_visible_text(person_num)

# 예약 신청 클릭
driver.find_element(By.ID, "btnRsv").click()

# 로그인 정보 입력
# 로그인 정보 입력란이 나타날 때까지 대기
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "userNo")))

user_id = "your_id"
user_pw = "your_password"

driver.find_element(By.ID, "userNo").send_keys(user_id)
driver.find_element(By.ID, "userPw").send_keys(user_pw)
driver.find_element(By.ID, "btnLogin").click()

# 예약 완료 확인
# 예약 완료 메시지가 나타날 때까지 대기
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "layerPop")))

message = driver.find_element(By.ID, "layerPop").text
print(message)

# 브라우저 종료
driver.quit()
