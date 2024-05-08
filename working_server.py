from selenium import webdriver
import time,logging,mysql.connector
import path_locators
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def check_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="tenantapp"
    )

    return db


def open_tenant():
    try:
        driver.get("http://127.0.0.1:5000")
        time.sleep(2)
        logging.info("Open tenant successful")
    except Exception as e:
        logging.error("Error in open tenant:",e)


def click_tenant_button():

    open_tenant()
    driver.find_element(By.XPATH,path_locators.tenant_button["click"]).click()
    time.sleep(2)


def flight():

    driver.find_element(By.XPATH, path_locators.select_service["flight"]).click()
    time.sleep(1)


def train():

    driver.find_element(By.XPATH,path_locators.select_service["train"]).click()
    time.sleep(1)


def taxi():

    driver.find_element(By.XPATH,path_locators.select_service["taxi"]).click()
    time.sleep(1)


def hotel():

    driver.find_element(By.XPATH,path_locators.select_service["hotel"]).click()
    time.sleep(1)


def create_tenant():

    connection = check_database()
    cursor = connection.cursor()
    sql_query = "SELECT userId FROM tenant ORDER BY t_id DESC LIMIT 1"
    print(sql_query)
    cursor.execute(sql_query)
    resid = cursor.fetchone()[0]
    print(resid)

    r = resid.split("-")
    print(r)
    num = int(r[1]) + 1
    res = r[0] + "-" + str(num)
    print(res)

    driver.find_element(By.XPATH,path_locators.sign_up["tname"]).send_keys("siw")
    time.sleep(2)

    driver.find_element(By.XPATH,path_locators.sign_up["uname"]).send_keys(res)
    time.sleep(2)

    driver.find_element(By.XPATH,path_locators.sign_up["pwd"]).send_keys("7867")
    time.sleep(2)

    driver.find_element(By.XPATH,path_locators.sign_up["c_pwd"]).send_keys("7867")
    time.sleep(2)

    driver.find_element(By.XPATH,path_locators.sign_up["click_reg"]).click()
    time.sleep(2)


def t_create_login():

    connection = check_database()
    cursor = connection.cursor()
    sql_query = "SELECT userId FROM tenant ORDER BY t_id DESC LIMIT 1"
    print(sql_query)
    cursor.execute(sql_query)
    resid = cursor.fetchone()[0]

    driver.find_element(By.XPATH,path_locators.login["uname"]).send_keys(resid)
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.login["pwd"]).send_keys("7867")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.login["login_button"]).click()
    time.sleep(2)


def t_permanent_login():

    driver.find_element(By.XPATH, path_locators.login["uname"]).send_keys("siw12")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["pwd"]).send_keys("6767")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["login_button"]).click()
    time.sleep(2)


def t_logout():

    driver.find_element(By.XPATH,"/html/body/div/div[3]/a/button").click()
    time.sleep(1)


def t_click_sign_in():

    driver.find_element(By.XPATH,path_locators.sign_in_button["click"]).click()
    time.sleep(1)


def t_book_flight():

    driver.find_element(By.XPATH,path_locators.t_book_flight["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_flight["add_flight"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_flight["flight_name"]).send_keys("indigo")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_flight["travel_from"]).send_keys("dubai")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_flight["travel_to"]).send_keys("india")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_flight["avl_seats"]).send_keys("6")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_flight["submit"]).click()
    time.sleep(2)

    driver.find_element(By.XPATH,path_locators.t_book_flight["logout"]).click()
    time.sleep(1)


def t_book_train():

    driver.find_element(By.XPATH,path_locators.t_book_train["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_train["add_train"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_train["train_name"]).send_keys("rajdhani")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_train["travel_from"]).send_keys("kolkata")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_train["travel_to"]).send_keys("mumbai")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_train["price"]).send_keys("800")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_train["avl_seats"]).send_keys("80")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_train["submit"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_train["logout"]).click()
    time.sleep(1)


def t_book_hotel():

    driver.find_element(By.XPATH,path_locators.t_book_hotel["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_hotel["add_hotel"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_hotel["hotel_name"]).send_keys("redission")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_hotel["city"]).send_keys("jaipur")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_hotel["avl_room"]).send_keys("9")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_hotel["price"]).send_keys("750")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_hotel["submit"]).click()
    time.sleep(2)

    driver.find_element(By.XPATH,path_locators.t_book_hotel["logout"]).click()
    time.sleep(1)


def t_book_taxi():

    driver.find_element(By.XPATH,path_locators.t_book_taxi["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_taxi["add_taxi"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_taxi["taxi_number"]).send_keys("650")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_taxi["city"]).send_keys("banglore")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_taxi["rate"]).send_keys("908")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_taxi["submit"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_taxi["logout"]).click()
    time.sleep(1)


def t_click_u_flight():

    driver.find_element(By.XPATH,path_locators.tenant_user["u_flight"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.tenant_user["logout"]).click()
    time.sleep(1)


def t_click_u_hotel():

    driver.find_element(By.XPATH, path_locators.tenant_user["u_hotel"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.tenant_user["logout"]).click()
    time.sleep(1)


def t_click_u_taxi():

    driver.find_element(By.XPATH, path_locators.tenant_user["u_taxi"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.tenant_user["logout"]).click()
    time.sleep(1)


def t_click_u_train():

    driver.find_element(By.XPATH, path_locators.tenant_user["u_train"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.tenant_user["logout"]).click()
    time.sleep(1)


def click_users():

    open_tenant()
    driver.find_element(By.XPATH,path_locators.users_button["click"]).click()
    time.sleep(2)


def create_users():

    connection = check_database()
    cursor = connection.cursor()
    sql_query = "SELECT username FROM users ORDER BY user_id DESC LIMIT 1"
    print(sql_query)
    cursor.execute(sql_query)
    resid = cursor.fetchone()[0]
    print(resid)

    r = resid.split("-")
    print(r)
    num = int(r[1]) + 1
    res = r[0] + "-" + str(num)
    print(res)

    driver.find_element(By.XPATH,path_locators.users_sign_up["email"]).send_keys(res)
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.users_sign_up["pwd"]).send_keys("7860")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.users_sign_up["c_pwd"]).send_keys("7860")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.users_sign_up["click_reg"]).click()
    time.sleep(2)


def select_tenant():

    driver.find_element(By.XPATH,path_locators.select_tenant["click"]).click()
    time.sleep(3)

    driver.find_element(By.XPATH,path_locators.select_tenant["slct_othr"]).click()
    time.sleep(2)

    driver.find_element(By.XPATH, path_locators.select_tenant["click"]).click()
    time.sleep(3)


def user_create_login():

    connection = check_database()
    cursor = connection.cursor()
    sql_query = "SELECT username FROM users ORDER BY user_id DESC LIMIT 1"
    print(sql_query)
    cursor.execute(sql_query)
    resid = cursor.fetchone()[0]

    driver.find_element(By.XPATH, path_locators.login["uname"]).send_keys(resid)
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["pwd"]).send_keys("7860")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["login_button"]).click()
    time.sleep(2)


def user_permanent_login():

    driver.find_element(By.XPATH, path_locators.login["uname"]).send_keys("emo79")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["pwd"]).send_keys("7860")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["login_button"]).click()
    time.sleep(2)


def user_login_w_pwd():

    driver.find_element(By.XPATH, path_locators.login["uname"]).send_keys("emo798")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["pwd"]).send_keys("786")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["login_button"]).click()
    time.sleep(2)


def user_login_w_uname():

    driver.find_element(By.XPATH, path_locators.login["uname"]).send_keys("emo98")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["pwd"]).send_keys("7860")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["login_button"]).click()
    time.sleep(2)


def users_book_flight():

    driver.find_element(By.XPATH,path_locators.u_book_flight["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_flight["from"]).send_keys("indore")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_flight["to"]).send_keys("delhi")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_flight["submit"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_flight["book_now"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_flight["continue_btn"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_flight["logout"]).click()
    time.sleep(2)


def users_book_hotel():

    driver.find_element(By.XPATH,path_locators.u_book_hotel["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_hotel["city"]).send_keys("jaipur")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_hotel["submit"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_hotel["book_now"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_hotel["continue_btn"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_hotel["logout"]).click()
    time.sleep(1)


def users_book_taxi():

    driver.find_element(By.XPATH,path_locators.u_book_taxi["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_taxi["city"]).send_keys("indore")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_taxi["submit"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_taxi["book_now"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_taxi["continue_btn"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_taxi["logout"]).click()
    time.sleep(1)


def users_book_train():

    driver.find_element(By.XPATH, path_locators.u_book_train["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_train["from"]).send_keys("indore")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_train["to"]).send_keys("delhi")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_train["submit"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_train["book_now"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_train["continue_btn"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_train["logout"]).click()
    time.sleep(2)


def user_logout():

    driver.find_element(By.XPATH,"/html/body/div/div[1]/a/button").click()
    time.sleep(1)


def both_forget_pwd():

    driver.find_element(By.XPATH,path_locators.users_forget_pwd["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.users_forget_pwd["uname"]).send_keys("khan")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.users_forget_pwd["new_pwd"]).send_keys("6767")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.users_forget_pwd["retype_pwd"]).send_keys("6767")
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.users_forget_pwd["submit"]).click()
    time.sleep(1)


def dlt_flight_tkt():

    driver.find_element(By.XPATH,path_locators.dlt_flight_tkt["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.dlt_flight_tkt["dlt"]).click()
    time.sleep(1)


def dlt_train_tkt():

    driver.find_element(By.XPATH,path_locators.dlt_train_tkt["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.dlt_train_tkt["dlt"]).click()
    time.sleep(1)


def dlt_taxi():

    driver.find_element(By.XPATH,path_locators.dlt_taxi["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.dlt_taxi["dlt"]).click()
    time.sleep(1)


def dlt_hotel():

    driver.find_element(By.XPATH,path_locators.dlt_hotel["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.dlt_hotel["dlt"]).click()
    time.sleep(1)


def t_wrong_login_pwd():

    driver.find_element(By.XPATH, path_locators.login["uname"]).send_keys("siw12")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["pwd"]).send_keys("676")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["login_button"]).click()
    time.sleep(2)


def t_wrong_login_uname():

    driver.find_element(By.XPATH, path_locators.login["uname"]).send_keys("siw129")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["pwd"]).send_keys("6767")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.login["login_button"]).click()
    time.sleep(2)


def same_create_t_uname():

    driver.find_element(By.XPATH,path_locators.sign_up["tname"]).send_keys("khan")
    time.sleep(2)

    driver.find_element(By.XPATH,path_locators.sign_up["uname"]).send_keys("siw12")
    time.sleep(2)

    driver.find_element(By.XPATH,path_locators.sign_up["pwd"]).send_keys("7867")
    time.sleep(2)

    driver.find_element(By.XPATH,path_locators.sign_up["c_pwd"]).send_keys("7867")
    time.sleep(2)

    driver.find_element(By.XPATH,path_locators.sign_up["click_reg"]).click()
    time.sleep(2)


def click_sign_up_button():

    driver.find_element(By.XPATH,path_locators.sign_up_button["click"]).click()
    time.sleep(1)


def u_book_flight_with_meal():

    driver.find_element(By.XPATH,path_locators.user_book_flight_with_meal["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.user_book_flight_with_meal["from"]).send_keys("jaipur")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.user_book_flight_with_meal["to"]).send_keys("banglore")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.user_book_flight_with_meal["submit"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.user_book_flight_with_meal["book_now"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.user_book_flight_with_meal["click_yes"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.user_book_flight_with_meal["click_add"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.user_book_flight_with_meal["click_continue_btn"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.user_book_flight_with_meal["logout"]).click()
    time.sleep(1)


def chk_flyt_booking():

    driver.find_element(By.XPATH, path_locators.t_book_flight["click"]).click()
    time.sleep(1)


def create_u_bk_flyt_chk_tnt():

    open_tenant()
    click_users()
    select_tenant()
    create_users()
    user_create_login()
    u_book_flight_with_meal()
    open_tenant()
    click_tenant_button()
    t_click_sign_in()
    t_permanent_login()
    chk_flyt_booking()


def forget_pwd_wrng_uname():

    driver.find_element(By.XPATH, path_locators.users_forget_pwd["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.users_forget_pwd["uname"]).send_keys("dhjckdj")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.users_forget_pwd["new_pwd"]).send_keys("6767")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.users_forget_pwd["retype_pwd"]).send_keys("6767")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.users_forget_pwd["submit"]).click()
    time.sleep(1)


def forget_pwd_dfrnt_pwd():

    driver.find_element(By.XPATH, path_locators.users_forget_pwd["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.users_forget_pwd["uname"]).send_keys("dhjckdj")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.users_forget_pwd["new_pwd"]).send_keys("676")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.users_forget_pwd["retype_pwd"]).send_keys("6767")
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.users_forget_pwd["submit"]).click()
    time.sleep(1)


def fill_t_flight_form_without_data():

    driver.find_element(By.XPATH,path_locators.t_book_flight["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.t_book_flight["add_flight"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_flight["submit"]).click()
    time.sleep(2)


def fill_t_hotel_form_without_data():

    driver.find_element(By.XPATH, path_locators.t_book_hotel["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_hotel["add_hotel"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_hotel["submit"]).click()
    time.sleep(1)


def fill_t_taxi_form_without_data():

    driver.find_element(By.XPATH, path_locators.t_book_taxi["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_taxi["add_taxi"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_taxi["submit"]).click()
    time.sleep(1)


def fill_t_train_form_without_data():

    driver.find_element(By.XPATH, path_locators.t_book_train["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_train["add_train"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.t_book_train["submit"]).click()
    time.sleep(1)


def fill_user_flight_form_without_data():

    driver.find_element(By.XPATH,path_locators.u_book_flight["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_flight["submit"]).click()
    time.sleep(1)


def fill_user_hotel_form_without_data():

    driver.find_element(By.XPATH,path_locators.u_book_hotel["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH,path_locators.u_book_hotel["submit"]).click()
    time.sleep(1)


def fill_user_taxi_form_without_data():

    driver.find_element(By.XPATH,path_locators.u_book_taxi["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_taxi["submit"]).click()
    time.sleep(1)


def fill_user_train_form_without_data():

    driver.find_element(By.XPATH, path_locators.u_book_train["click"]).click()
    time.sleep(1)

    driver.find_element(By.XPATH, path_locators.u_book_train["submit"]).click()
    time.sleep(1)


def run():

    open_tenant()
    click_users()
    create_users()
    user_create_login()


if __name__ == "__main__":

    run()



