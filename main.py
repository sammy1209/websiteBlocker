from datetime import datetime
host_path = 'C:/Windows/System32/drivers/etc/hosts'
redirect = '127.0.0.1'
website_list=["www.facebook.com", "www.instagram.com", "facebook.com"]

start_date = datetime(2020,11,19)
end_date = datetime(2020,11,20)
today_date = datetime(datetime.now().year,datetime.now().month, datetime.now().day)


while True:
    if start_date <= today_date < end_date:
        with open(host_path,"r+") as file:
            content = file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
        print("all sites are blocked")
        break
    else:#end_date < today_date
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                #list comprehension
                if not any(site in line for site in website_list):
                    file.write(line)
            #to save the file after complition the task
            file.truncate()
        print("all sites are blocked")
        break
