#비밀번호 만들기

#계속해서 오류난 이유 
# 1. site 변수 지정할 때 ""처리를 안함.
# 2. password 변수에 실수로 print를 잘못 적음.
# 3. 가장 중요한 것! 문자열끼리 +로 연결하려면, 숫자는 str 꼭 걸어줘야 함. 숫자로 이어서 적음.

# ! 헷갈렸던 것 - name 지정할 때 []의 끝부분을 -4로 해야 하는지 -5로 해야 하는지 헷갈림.
# ! 포함하지 않으므로 4개를 빼서 -4가 맞는 듯함.

site = "http://youtube.com"
name = site[7:-4]
password = name[:3] + str(len(name)) + str(name.count("e")) + "!" 

print("{}의 비밀번호 : {}" .format(site, password))


#나도코딩님 방식

url = "http://naver.com"
str_url = url.replace("http://" , "")
str_url = str_url[:str_url.index(".")]

Password = str_url[:3] + str(len(str_url)) + str(str_url.count("e")) + "!"

print("{1}의 비밀번호는 {0}입니다." .format(Password, url))