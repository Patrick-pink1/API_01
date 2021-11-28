# ---min24':00" , 30':00"------save in file:movie.txt-
# --use postman software to know how is th Json or use wig IDE
import requests

def func_write(list1):
    with open ("movie1.txt","a+") as file1: 
        print("----------->>>>>>>>>>>><<<<<<<<<<<<<<<<<<--------------------")
        print("file.tell(): ",file.tell())
        file1.write("----------->>>>>>>>>>>><<<<<<<<<<<<<<<<<<--------------------\n")
        for i in range(len(list1)):
            file1.write("{0:-<15d}{1}".format(i+1,list1[i]))
            file1.write("\n")
        print("Writing the list------DONE!------------")
# ---------------------------------------------------------------------------------------
try:
    response = requests.get("http://moviesapi.ir/api/v1/movies?page=1")
except Exception as error:
    print(error)
else:
    print("\n----->>>>>>>>>>-----------Connection DONE!------")
    print("--response: ",response)
    print("-----requests.status_code: ", response.status_code)
    print("---------response.json: ",response.json)
    mydict = response.json()
    all_pages = mydict['metadata']['page_count']
    pages= int(input("\n------WE HAVE %s pages.\nHowmany pages do you want to see? "%all_pages))
    with open ("movie1.txt","w+") as file:
        list_movie = []
        for page in range(pages):
            try:
                response = requests.get("http://moviesapi.ir/api/v1/movies?page={}".format(page+1))
            except Exception as error:
                print(error)
            else:
                print("\n----->>>>>>>>>>-----------Connection DONE!------")
                print("--response: ",response)
                print("-----requests.status_code: ", response.status_code)
                print("---------response.json: ",response.json)
                if response.status_code == 200:
                    mydict = response.json()
                    print("--------------------------------------")
                    for i in range (10):
                        str_title = "{0:-<10}{1}".format((i+1+page*10),mydict['data'][i]['title'])
                        print(str_title)
                        list_movie.append(mydict['data'][i]['title'])
                        file.write(str_title)
                        file.write("\n")
        print("\nlist_movie:\n",list_movie)
        func_write(list_movie)
        print("\n--------Writing DONE!!!---------")
        print("\nfile.tell(): ",file.tell())
        file.seek(0)
        print("file.tell()after file.seek(0): ",file.tell())
        print("\n------>>>>>>>>>>>>>-----file.read():----------------\n{}".format(file.read()))




