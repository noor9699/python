# import working_server as ws
# import test_suite as ts
# import logging
# import csv

logging.basicConfig(filename="neg_logcheck.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

dict = {}


def n_test1():
    try:
        ws.open_tenant()
        ws.click_tenant_button()
        ws.t_click_sign_in()
        ws.t_wrong_login_pwd()
        logger.info("n test 1 successful with 4 modules")
        dict["n_test1"] = "Success"

    except Exception as e:
        logger.error("Error in n test 1:", e)
        dict["n_test1"] = "Failed"
        pass


def n_test2():

    try:
        ws.open_tenant()
        ws.click_tenant_button()
        ws.t_click_sign_in()
        ws.t_wrong_login_uname()
        logger.info("n test 2 successful with 4 modules")
        dict["n_test2"] = "Success"

    except Exception as e:
        logger.error("Error in n test 2:", e)
        dict["n_test2"] = "Failed"
        pass


def n_test3():

    try:
        ws.open_tenant()
        ws.click_tenant_button()
        ws.same_create_t_uname()
        logger.info("n test 3 successful with 2 modules")
        dict["n_test3"] = "Success"

    except Exception as e:
        logger.error("Error in n test 3:", e)
        dict["n_test3"] = "Failed"
        pass


def n_test4():

    try:
        ws.open_tenant()
        ws.click_users()
        ws.t_click_sign_in()
        ws.user_login_w_pwd()
        logger.info("n test 4 successful with 4 modules")
        dict["n_test4"] = "Success"

    except Exception as e:
        logger.error("Error in n test 4:", e)
        dict["n_test4"] = "Failed"
        pass


def n_test5():

    try:
        ws.open_tenant()
        ws.click_users()
        ws.t_click_sign_in()
        ws.user_login_w_uname()
        logger.info("n test 5 successful with 4 modules")
        dict["n_test5"] = "Success"

    except Exception as e:
        logger.error("Error in n test 5:", e)
        dict["n_test5"] = "Failed"
        pass


def n_test6():

    try:
        ts.test_case19()
        logger.info("n test 6 successful with 5 modules")
        dict["n_test6"] = "Success"

    except Exception as e:
        logger.error("Error in n test 6:", e)
        dict["n_test6"] = "Failed"
        pass


def n_test7():

    try:
        ts.test_case18()
        logger.info("n test 7 successful with 5 modules")
        dict["n_test7"] = "Success"

    except Exception as e:
        logger.error("Error in n test 7:", e)
        dict["n_test7"] = "Failed"
        pass


def n_test8():

    try:
        ts.test_case20()
        logger.info("n test 8 successful with 5 modules")
        dict["n_test8"] = "Success"

    except Exception as e:
        logger.error("Error in n test 8:", e)
        dict["n_test8"] = "Failed"
        pass


def n_test9():

    try:
        ts.test_case26()
        logger.info("n test 9 successful with 5 modules")
        dict["n_test9"] = "Success"

    except Exception as e:
        logger.error("Error in n test 9:", e)
        dict["n_test9"] = "Failed"
        pass


def n_test10():

    try:
        ws.open_tenant()
        ws.click_users()
        ws.t_click_sign_in()
        ws.forget_pwd_wrng_uname()
        logger.info("n test 10 successful with 4 modules")
        dict["n_test10"] = "Success"

    except Exception as e:
        logger.error("Error in n test 10:", e)
        dict["n_test10"] = "Failed"
        pass


def run_fun():

    for i in range(1,11):
        print(i)
        str_test = "n_test"+ str(i)
        function = globals()[str_test]
        function()

        print(str_test)

    names = list(dict.keys())
    values = list(dict.values())

    with open('neg_Dict_n_test.csv', 'w') as output:
        writer = csv.writer(output)
        for key, value in dict.items():
            writer.writerow([key, value])


if __name__ == "__main__":

    run_fun()

