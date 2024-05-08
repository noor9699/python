import working_server as ws
import logging
import csv
import matplotlib.pyplot as plt

logging.basicConfig(filename="logcheck.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

dict= {}


def test_case1():

    try:
        ws.open_tenant()
        ws.click_tenant_button()
        logger.info("test case 1 successful with 2 modules")
        dict["test_case1"] = "Success"

    except Exception as e:
        logger.error("Error in test case 1:", e)
        dict["test_case1"] = "Failed"
        pass


def test_case2():

    try:
        ws.open_tenant()
        ws.click_users()
        logger.info("test case 2 successful with 2 modules")
        dict["test_case2"] = "Success"

    except Exception as e:
        logger.error("Error in test case 2:", e)
        dict["test_case2"] = "Failed"
        pass


def test_case3():

    try:
        test_case1()
        ws.create_tenant()
        logger.info("test case 3 successful with 3 modules")
        dict["test_case3"] = "Success"

    except Exception as e:
        logger.error("Error in test case 3:",e)
        dict["test_case3"] = "Failed"
        pass


def test_case4():

    try:
        test_case1()
        ws.flight()
        ws.create_tenant()
        logger.info("test case 4 successful with 4 modules")
        dict["test_case4"] = "Success"

    except Exception as e:
        logger.error("Error in test case 4:",e)
        dict["test_case4"] = "Failed"
        pass


def test_case5():

    try:
        test_case1()
        ws.train()
        ws.create_tenant()
        logger.info("test case 5 successful with 4 modules")
        dict["test_case5"] = "Success"

    except Exception as e:
        logger.error("Error in test case 5:",e)
        dict["test_case5"] = "Failed"
        pass


def test_case6():

    try:
        test_case1()
        ws.taxi()
        ws.create_tenant()
        logger.info("test case 6 successful with 4 modules")
        dict["test_case6"] = "Success"

    except Exception as e:
        logger.error("Error in test case 6:", e)
        dict["test_case6"] = "Failed"
        pass


def test_case7():

    try:
        test_case1()
        ws.hotel()
        ws.create_tenant()
        logger.info("test case 7 successful with 4 modules")
        dict["test_case7"] = "Success"

    except Exception as e:
        logger.error("Error in test case 7:",e)
        dict["test_case7"] = "Failed"
        pass


def test_case8():

    try:
        test_case1()
        ws.flight()
        ws.hotel()
        ws.train()
        ws.taxi()
        ws.create_tenant()
        logger.info("test case 8 successful with 7 modules")
        dict["test_case8"] = "Success"

    except Exception as e:
        logger.error("Error in test case 8:",e)
        dict["test_case8"] = "Failed"
        pass


def test_case9():

    try:
        test_case3()
        ws.t_create_login()
        logger.info("test case 9 successful with 4 modules")
        dict["test_case9"] = "Success"

    except Exception as e:
        logger.error("Error in test case 9:", e)
        dict["test_case9"] = "Failed"
        pass


def test_case10():

    try:
        test_case9()
        ws.t_logout()
        logger.info("test case 10 successful with 5 modules")
        dict["test_case10"] = "Success"

    except Exception as e:
        logger.error("Error in test case 10:",e)
        dict["test_case10"] = "Failed"
        pass


def test_case11():

    try:
        test_case1()
        ws.t_click_sign_in()
        ws.t_permanent_login()
        logger.info("test case 11 successful with 4 modules")
        dict["test_case11"] = "Success"

    except Exception as e:
        logger.error("Error in test case 11:",e)
        dict["test_case11"] = "Failed"
        pass


def test_case12():

    try:
        test_case1()
        ws.t_click_sign_in()
        ws.both_forget_pwd()
        logger.info("test case 12 successful with 4 modules")
        dict["test_case12"] = "Success"

    except Exception as e:
        logger.error("Error in test case 12:",e)
        dict["test_case12"] = "Failed"
        pass


def test_case13():

    try:
        test_case2()
        ws.select_tenant()
        logger.info("test case 13 successful with 3 modules")
        dict["test_case13"] = "Success"

    except Exception as e:
        logger.error("Error in test case 13:",e)
        dict["test_case13"] = "Failed"
        pass


def test_case14():

    try:
        test_case13()
        ws.create_users()
        logger.info("test case 14 successful with 4 modules")
        dict["test_case14"] = "Success"

    except Exception as e:
        logger.error("Error in test case 14:",e)
        dict["test_case14"] = "Failed"
        pass


def test_case15():

    try:
        test_case14()
        ws.user_create_login()
        logger.info("test case 15 successful with 5 modules")
        dict["test_case15"] = "Success"

    except Exception as e:
        logger.error("Error in test case 15:",e)
        dict["test_case15"] = "Failed"
        pass


def test_case16():

    try:
        test_case2()
        ws.t_click_sign_in()
        ws.user_permanent_login()
        ws.users_book_flight()
        logger.info("test case 16 successful with 5 modules")
        dict["test_case16"] = "Success"

    except Exception as e:
        logger.error("Error in test case 16:", e)
        dict["test_case16"] = "Failed"
        pass


def test_case17():

    try:
        test_case2()
        ws.t_click_sign_in()
        ws.user_permanent_login()
        ws.users_book_taxi()
        logger.info("test case 17 successful with 5 modules")
        dict["test_case17"] = "Success"

    except Exception as e:
        logger.error("Error in test case 17:",e)
        dict["test_case17"] = "Failed"
        pass


def test_case18():

    try:
        test_case2()
        ws.t_click_sign_in()
        ws.user_permanent_login()
        ws.users_book_train()
        logger.info("test case 18 successful with 5 modules")
        dict["test_case18"] = "Success"

    except Exception as e:
        logger.error("Error in test case 18:",e)
        dict["test_case18"] = "Failed"
        pass


def test_case19():

    try:
        test_case2()
        ws.t_click_sign_in()
        ws.user_permanent_login()
        ws.users_book_hotel()
        logger.info("test case 19 successful with 5 modules")
        dict["test_case19"] = "Success"

    except Exception as e:
        logger.error("Error in test case 19:",e)
        dict["test_case19"] = "Failed"
        pass


def test_case20():

    try:
        test_case11()
        ws.t_click_u_flight()
        logger.info("test case 20 successful with 5 modules")
        dict["test_case20"] = "Success"

    except Exception as e:
        logger.error("Error in test case 20:",e)
        dict["test_case20"] = "Failed"
        pass


def test_case21():

    try:
        test_case11()
        ws.t_click_u_train()
        logger.info("test case 21 successful with 5 modules")
        dict["test_case21"] = "Success"

    except Exception as e:
        logger.error("Error in test case 21:",e)
        dict["test_case21"] = "Failed"
        pass


def test_case22():

    try:
        test_case11()
        ws.t_click_u_taxi()
        logger.info("test case 22 successful with 5 modules")
        dict["test_case22"] = "Success"

    except Exception as e:
        logger.error("Error in test case 22:",e)
        dict["test_case22"] = "Failed"
        pass


def test_case23():

    try:
        test_case11()
        ws.t_click_u_hotel()
        logger.info("test case 23 successful with 5 modules")
        dict["test_case23"] = "Success"

    except Exception as e:
        logger.error("Error in test case 23:",e)
        dict["test_case23"] = "Failed"
        pass


def test_case24():

    try:
        test_case2()
        ws.t_click_sign_in()
        ws.user_permanent_login()
        ws.user_logout()
        logger.info("test case 24 successful with 5 modules")
        dict["test_case24"] = "Success"

    except Exception as e:
        logger.error("Error in test case 24:",e)
        dict["test_case24"] = "Failed"
        pass


def test_case25():

    try:
        test_case11()
        ws.dlt_flight_tkt()
        logger.info("test case 25 successful with 5 modules")
        dict["test_case25"] = "Success"

    except Exception as e:
        logger.error("Error in test case 25:",e)
        dict["test_case25"] = "Failed"
        pass


def test_case26():

    try:
        test_case11()
        ws.dlt_train_tkt()
        logger.info("test case 26 successful with 5 modules")
        dict["test_case26"] = "Success"

    except Exception as e:
        logger.error("Error in test case 26:",e)
        dict["test_case26"] = "Failed"
        pass


def test_case27():

    try:
        test_case11()
        ws.dlt_hotel()
        logger.info("test case 27 successful with 5 modules")
        dict["test_case27"] = "Success"

    except Exception as e:
        logger.error("Error in test case 27:",e)
        dict["test_case27"] = "Failed"
        pass


def test_case28():

    try:
        test_case11()
        ws.dlt_taxi()
        logger.info("test case 28 successful with 5 modules")
        dict["test_case28"] = "Success"

    except Exception as e:
        logger.error("Error in test case 28:",e)
        dict["test_case28"] = "Failed"
        pass


def test_case29():

    try:
        test_case1()
        ws.t_click_sign_in()
        ws.click_sign_up_button()
        logger.info("test case 29 successful with 4 modules")
        dict["test_case29"] = "Success"

    except Exception as e:
        logger.error("Error in test case 29:",e)
        dict["test_case29"] = "Failed"
        pass


def test_case30():

    try:
        test_case2()
        ws.t_click_sign_in()
        ws.user_permanent_login()
        ws.u_book_flight_with_meal()
        logger.info("test case 30 successful with 5 modules")
        dict["test_case30"] = "Success"

    except Exception as e:
        logger.error("Error in test case 30:",e)
        dict["test_case30"] = "Failed"
        pass


def test_case31():

    try:
        ws.create_u_bk_flyt_chk_tnt()
        logger.info("test case 31 successful with 11 modules")
        dict["test_case31"] = "Success"

    except Exception as e:
        logger.error("Error in test case 31:",e)
        dict["test_case31"] = "Failed"
        pass


def test_case32():

    try:
        ws.open_tenant()
        ws.click_users()
        ws.t_click_sign_in()
        ws.forget_pwd_dfrnt_pwd()
        logger.info("test case 32 successful with 4 modules")
        dict["test_case32"] = "Success"

    except Exception as e:
        logger.error("Error in test case 32:", e)
        dict["test_case32"] = "Failed"
        pass


def test_case33():

    try:
        ws.open_tenant()
        ws.click_tenant_button()
        ws.t_click_sign_in()
        ws.t_permanent_login()
        ws.fill_t_flight_form_without_data()
        logger.info("test case 33 successful with 5 modules")
        dict["test_case33"] = "Success"

    except Exception as e:
        logger.error("Error in test case 33:",e)
        dict["test_case33"] = "Failed"
        pass


def test_case34():

    try:
        ws.open_tenant()
        ws.click_tenant_button()
        ws.t_click_sign_in()
        ws.t_permanent_login()
        ws.fill_t_hotel_form_without_data()
        logger.info("test case 34 successful with 5 modules")
        dict["test_case34"] = "Success"

    except Exception as e:
        logger.error("Error in test case 34:",e)
        dict["test_case34"] = "Failed"
        pass


def test_case35():

    try:
        ws.open_tenant()
        ws.click_tenant_button()
        ws.t_click_sign_in()
        ws.t_permanent_login()
        ws.fill_t_taxi_form_without_data()
        logger.info("test case 35 successful with 5 modules")
        dict["test_case35"] = "Success"

    except Exception as e:
        logger.error("Error in test case 35:",e)
        dict["test_case35"] = "Failed"
        pass


def test_case36():

    try:
        ws.open_tenant()
        ws.click_tenant_button()
        ws.t_click_sign_in()
        ws.t_permanent_login()
        ws.fill_t_train_form_without_data()
        logger.info("test case 36 successful with 5 modules")
        dict["test_case36"] = "Success"

    except Exception as e:
        logger.error("Error in test case 36:",e)
        dict["test_case36"] = "Failed"
        pass


def test_case37():

    try:
        ws.open_tenant()
        ws.click_users()
        ws.t_click_sign_in()
        ws.user_permanent_login()
        ws.fill_user_flight_form_without_data()
        logger.info("test case 37 successful with 5 modules")
        dict["test_case37"] = "Success"

    except Exception as e:
        logger.error("Error in test case 37:",e)
        dict["test_case37"] = "Failed"
        pass


def test_case38():

    try:
        ws.open_tenant()
        ws.click_users()
        ws.t_click_sign_in()
        ws.user_permanent_login()
        ws.fill_user_hotel_form_without_data()
        logger.info("test case 38 successful with 5 modules")
        dict["test_case38"] = "Success"

    except Exception as e:
        logger.error("Error in test case 38:",e)
        dict["test_case38"] = "Failed"
        pass


def test_case39():

    try:
        ws.open_tenant()
        ws.click_users()
        ws.t_click_sign_in()
        ws.user_permanent_login()
        ws.fill_user_taxi_form_without_data()
        logger.info("test case 39 successful with 5 modules")
        dict["test_case39"] = "Success"

    except Exception as e:
        logger.error("Error in test case 39:",e)
        dict["test_case39"] = "Failed"
        pass


def test_case40():

    try:
        ws.open_tenant()
        ws.click_users()
        ws.t_click_sign_in()
        ws.user_permanent_login()
        ws.fill_user_train_form_without_data()
        logger.info("test case 40 successful with 5 modules")
        dict["test_case40"] = "Success"

    except Exception as e:
        logger.error("Error in test case 40:",e)
        dict["test_case40"] = "Failed"
        pass


def run_fun():

    for i in range(1,41):
        print(i)
        str_test = "test_case" + str(i)
        function = globals()[str_test]
        function()

        print(str_test)

    names = list(dict.keys())
    values = list(dict.values())

    with open('Dict_test_suite.csv', 'w') as output:
        writer = csv.writer(output)
        for key, value in dict.items():
            writer.writerow([key, value])


if __name__ == "__main__":

    run_fun()
