import os
import re
import requests
import glob

def mkdir(file_path):
    file_path= file_path
    isExists = os.path.exists(file_path)
    if not isExists:
        os.makedirs(file_path)
        return file_path

def get_image(md_file):
    img_list= []
    with open(md_file,"r",encoding="utf-8") as f:
        for line in f.readlines():
            line = re.sub(r"png#.*","png",line)
            #line = line.split(']')[1]
            if ('](https://' in line and 'png' in line):
                line = line.split('(')[1].rstrip()
                img_list.append(line)
    return img_list

def img_download(img_list):
    for url in img_list:
        img_name = url.split('/')[-1]
        img_path = "./images/"
        #img_path = url.replace("https://cdn.nlark.com","").replace(img_name,"")
        img_name2 = img_path + img_name
        r = requests.get(url, stream=True,timeout=5) #增加超时，避免requests一直等待
        if r.status_code == 200:
            print(img_name)
            print(img_path)
            print(img_name2)
            mkdir(img_path)
            open(img_name2, 'wb').write(r.content)
            print(img_name2 + " download success!")
        else:
            print(img_name2 + "download failed!")

def new_md(md_file,new_file,domain):
    with open(md_file,"r",encoding="utf-8") as f:   
        for line in f.readlines():
            with open(new_file,"a",encoding="utf-8") as f:
                if ('](https://' in line and 'png' in line):
                    line = re.sub(r"png#.*","png)",line)
                    url = line.split('/')[-1].rstrip()
                    url = domain + url
                    line = re.sub(r"https?://[^\s/$.?#].[^\s]*\.(?:png|jpe?g|gif)",url,line)
                    line = line.split(')')[0]+')'
                    #line =line.replace("https://cdn.nlark.com",domain)
                    line =line.replace("image.png","")
                    f.write(line.rstrip())
                else:
                    f.write(line)


if __name__ == "__main__":
    mdfile_list = glob.glob("*.md")
    #for md_file in mdfile_list:     
    #    img_list = get_image(md_file)
    #    img_download(img_list)
    domain = input("please input the domain\r\n")
    for md_file in mdfile_list:     
        img_list = get_image(md_file)
        img_download(img_list)
        new_md(md_file,"test.md",domain)


    


