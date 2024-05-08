tenant_button = {"click":"//*[@id='otherPage']"}
users_button = {"click":"/html/body/nav/a"}

sign_up = {
    "tname":"/html/body/div[1]/div/div/form[1]/div[1]/input",
    "uname":"/html/body/div[1]/div/div/form[1]/div[2]/input",
    "pwd":"/html/body/div[1]/div/div/form[1]/div[3]/input",
    "c_pwd":"/html/body/div[1]/div/div/form[1]/div[4]/input",
    "click_reg":"/html/body/div[1]/div/div/form[1]/div[6]/div/button"
}

select_service = {
    "flight":"/html/body/div[1]/div/div/form[1]/div[5]/div/input[1]",
    "train":"/html/body/div[1]/div/div/form[1]/div[5]/div/input[2]",
    "taxi":"/html/body/div[1]/div/div/form[1]/div[5]/div/input[3]",
    "hotel":"/html/body/div[1]/div/div/form[1]/div[5]/div/input[4]"
}

sign_in_button = {"click":"//*[@id='otherPage']"}
sign_up_button = {"click":"//*[@id='otherPage']"}

login = {"uname":"/html/body/div[1]/div/div/form[1]/div[1]/input",
         "pwd":"/html/body/div[1]/div/div/form[1]/div[2]/input",
         "login_button":"/html/body/div[1]/div/div/form[1]/div[4]/div/button"}

users_sign_up = {
    "email":"/html/body/div[1]/div/div/form[1]/div[1]/input",
    "pwd":"/html/body/div[1]/div/div/form[1]/div[2]/input",
    "c_pwd":"/html/body/div[1]/div/div/form[1]/div[3]/input",
    "click_reg":"/html/body/div[1]/div/div/form[1]/div[5]/div/button"
}

t_book_flight = {
    "click":"/html/body/div/div[1]/a/button",
    "add_flight":"//*[@id='navbarNavDropdown']/ul/li[2]/a",
    "flight_name":"//*[@id='flightForm']/div/input[1]",
    "travel_from":"//*[@id='flightForm']/div/input[2]",
    "travel_to":"//*[@id='flightForm']/div/input[3]",
    "avl_seats":"//*[@id='flightForm']/div/input[4]",
    "submit":"//*[@id='flightForm']/a/button",
    "logout":"//*[@id='navbarNavDropdown']/ul/li[2]/a"
}

t_book_train = {
    "click":"/html/body/div/div[1]/a[4]/button",
    "add_train":"//*[@id='navbarNavDropdown']/ul/li[2]/a",
    "train_name":"/html/body/div/form/div/input[1]",
    "travel_from":"/html/body/div/form/div/input[2]",
    "travel_to":"/html/body/div/form/div/input[3]",
    "price":"/html/body/div/form/div/input[4]",
    "avl_seats":"/html/body/div/form/div/input[5]",
    "submit":"/html/body/div/form/div/button",
    "logout":"//*[@id='navbarNavDropdown']/ul/li[3]/a"
}

t_book_hotel = {
    "click":"/html/body/div/div[1]/a[2]/button",
    "add_hotel":"//*[@id='navbarNavDropdown']/ul/li[2]/a",
    "hotel_name":"/html/body/div/form/div/input[1]",
    "city":"/html/body/div/form/div/input[2]",
    "avl_room":"/html/body/div/form/div/input[3]",
    "price":"/html/body/div/form/div/input[4]",
    "submit":"/html/body/div/form/button",
    "logout":"//a[@href='http://127.0.0.1:5000/dropsessiontenantlogin']"
}

t_book_taxi = {
    "click":"/html/body/div/div[1]/a[3]/button",
    "add_taxi":"//*[@id='navbarNavDropdown']/ul/li[2]/a",
    "taxi_number":"/html/body/div/form/div/input[1]",
    "city":"/html/body/div/form/div/input[2]",
    "rate":"/html/body/div/form/div/input[3]",
    "submit":"/html/body/div/form/button",
    "logout":"//*[@id='navbarNavDropdown']/ul/li[3]/a"
}

users_forget_pwd = {
    "click":"/html/body/div[1]/div/div/form[1]/div[3]/a",
    "uname":"//*[@id='exampleInputEmail1']",
    "new_pwd":"//*[@id='exampleInputPassword1']",
    "retype_pwd":"//input[@name='passre']",
    "submit":"/html/body/form/button"
}

u_book_flight = {
    "click":"/html/body/div/div[1]/button[1]/a",
    "from":"//*[@id='flightForm']/div/input[1]",
    "to":"//*[@id='flightForm']/div/input[2]",
    "submit":"//*[@id='flightForm']/button",
    "book_now":"/html/body/table/tbody/tr[1]/td[6]/a/button",
    "continue_btn":"/html/body/div/button/a",
    "logout":"//*[@id='navbarNavDropdown']/ul/li[2]/a"
}

u_book_hotel = {
    "click":"/html/body/div/div[1]/button[2]/a",
    "city":"//*[@id='flightForm']/div/input",
    "submit":"//*[@id='flightForm']/button",
    "book_now":"/html/body/table/tbody/tr[1]/td[6]/a/button",
    "continue_btn":"/html/body/div/button/a",
    "logout":"//*[@id='navbarNavDropdown']/ul/li[2]/a"
}

u_book_taxi = {
    "click":"/html/body/div/div[1]/button[3]/a",
    "city":"//*[@id='flightForm']/div/input",
    "submit":"//*[@id='flightForm']/button",
    "book_now":"/html/body/table/tbody/tr[1]/td[5]/a/button",
    "continue_btn":"/html/body/div/button/a",
    "logout":"//*[@id='navbarNavDropdown']/ul/li[2]/a"
}

u_book_train = {
    "click":"/html/body/div/div[1]/button[4]",
    "from":"//*[@id='flightForm']/div/input[1]",
    "to":"//*[@id='flightForm']/div/input[2]",
    "submit":"//*[@id='flightForm']/button",
    "book_now":"/html/body/table/tbody/tr/td[7]/a/button",
    "continue_btn":"/html/body/div/button/a",
    "logout":"//*[@id='navbarNavDropdown']/ul/li[2]/a"
}

select_tenant = {
    "click":"/html/body/div[1]/div/div/form[1]/div[4]/div/select",
    "slct":"/html/body/div[1]/div/div/form[1]/div[4]/div/select/option[16]",
    "slct_othr":"/html/body/div[1]/div/div/form[1]/div[4]/div/select/option[1]"
}

tenant_user = {
    "u_flight":"/html/body/div/div[2]/a[1]/button",
    "u_hotel":"/html/body/div/div[2]/a[2]/button",
    "u_taxi":"/html/body/div/div[2]/a[3]/button",
    "u_train":"/html/body/div/div[2]/a[4]/button",
    "logout":"//*[@id='navbarNavDropdown']/ul/li[2]/a"
}

dlt_flight_tkt = {
    "click":"/html/body/div/div[1]/a/button",
    "dlt":"/html/body/table/tbody/tr[1]/td[6]/a"
}

dlt_train_tkt = {
    "click":"/html/body/div/div[1]/a[4]/button",
    "dlt_error":"/html/body/table/tbody/tr[1]/td[7]/a",
    "dlt":"/html/body/table/tbody/tr[3]/td[7]/a"
}

dlt_taxi = {
    "click":"/html/body/div/div[1]/a[3]/button",
    "dlt":"/html/body/table/tbody/tr[1]/td[5]/a"
}

dlt_hotel = {
    "click":"/html/body/div/div[1]/a[2]/button",
    "dlt":"/html/body/table/tbody/tr[1]/td[6]/a"
}

user_book_flight_with_meal ={
    "click":"/html/body/div/div[1]/button[1]/a",
    "from":"//*[@id='flightForm']/div/input[1]",
    "to":"//*[@id='flightForm']/div/input[2]",
    "submit":"//*[@id='flightForm']/button",
    "book_now":"/html/body/table/tbody/tr/td[6]/a/button",
    "click_yes":"/html/body/div/button[1]/a",
    "click_no":"/html/body/div/button[2]/a",
    "click_add":"//*[@id='add_btn']",
    "click_continue_btn":"//*[@id='cb']",
    "logout":"//*[@id='navbarNavDropdown']/ul/li[2]/a"
}


