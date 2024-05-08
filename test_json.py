test_dict = {"test_case1":[2,"l","l"],"test_case2":[2,"l","l"],"test_case3":[3,"l","m"],"test_case4":[4,"m","m"],"test_case5":[4,"m","m"],"test_case6":[4,"m","m"],
             "test_case7":[4,"m","m"],"test_case8":[7,"h","m"],"test_case9":[4,"m","l"],"test_case10":[5,"m","l"],"test_case11":[4,"m","l"],"test_case12":[4,"m","l"],
             "test_case13":[3,"l","l"],
             "test_case14":[4,"m","l"],"test_case15":[5,"m","l"],"test_case16":[5,"h","h"],"test_case17":[5,"h","m"],"test_case18":[5,"h","m"],"test_case19":[5,"h","m"],
             "test_case20":[5,"h","h"],"test_case21":[5,"h","m"],"test_case22":[5,"h","m"],"test_case23":[5,"m","m"],"test_case24":[5,"m","m"],"test_case25":[5,"m","m"],"test_case26":[5,"h","m"],"test_case27":[5,"m","m"],

"test_case28":[5,"m","m"],"test_case29":[4,"m","l"],"test_case30":[5,"h","h"],"test_case31":[11,"h","h"],"test_case32":[4,"l","m"],"test_case33":[5,"m","m"],"test_case34":[5,"m","m"],"test_case35":[5,"m","m"],
             "test_case36":[5,"m","m"],"test_case37":[5,"m","m"],"test_case38":[5,"m","m"],"test_case39":[5,"m","m"],"test_case40":[5,"m","m"]}

neg_test_dict = {"n_test1":4,"n_test2":4,"n_test3":2,"n_test4":4,"n_test5":4,"n_test6":5,"n_test7":5,"n_test8":5,"n_test9":5,"n_test10":4}

module_dict = {"login_check":"low","Login_recheck":"Medium","Booking":"high"}

score = {}
list_score=[]
for keys in test_dict:
    print(keys)
    for i in range(0,2):
        if i == 0:
            list_score = []
            risk_score = 0.6
            depend_score = 0.4
        else:
            risk_score = 0.4
            depend_score = 0.6
        risk_l = test_dict[keys][1]
        depend_l = test_dict[keys][2]
        if risk_l == "l":
            risk_m = 1*risk_score
        elif risk_l == "m":
            risk_m = 2*risk_score
        else:
            risk_m = 3*risk_score
        if depend_l == "l":
            depend_m = 1*depend_score
        elif depend_l == "m":
            depend_m = 2*depend_score
        else:
            depend_m = 3*depend_score

        priority_score = risk_m+ depend_m

        list_score.append(priority_score)
    score[keys] = list_score

import csv
import matplotlib.pyplot as plt
names = list(score.keys())
values = list(score.values())

plt.bar(range(len(score)), values, tick_label=names)
plt.show()

with open('output1.csv', 'a') as output:
    writer = csv.writer(output)
    for key, value in score.items():
        writer.writerow([key, value[0],value[1]])






