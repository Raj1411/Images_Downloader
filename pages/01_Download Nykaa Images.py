
from opcode import opname
from time import time
from tkinter import E
from urllib import response
import streamlit as st
import requests as rq
from bs4 import BeautifulSoup as bs
import re
import shutil,os
import zipfile
from io import StringIO
from django.http import HttpResponse
from urllib.request import urlopen
from io import BytesIO
import base64
from PIL import Image
import time



# @st.cache
# def load_image(image_file):
#     img=Image.open(image_file)
#     return img




st.set_page_config(page_title="Nykaa Image Downloader", page_icon="https://cdn.worldvectorlogo.com/logos/nykaa-1.svg")
st.title("Nykaa Image Downloader")
st.markdown("---")
final_urls=[]


headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}


url_1=st.text_input("Enter the URL of the product you want to download: ")
total_images=st.text_input("Enter the number of images you want to download: ")

handle=zipfile.ZipFile('sample.zip','w')

if url_1=="":
    pass
else:
    ac=st.button("Generate Images")
    if ac:
        r=rq.get(url_1,headers=headers)
        soup=bs(r.text,'html.parser')
        # st.write(soup.prettify())

        # a_tags=soup.find_all('a',href=re.compile('//cdn.shopify.com/s/files/1'))
        a_tags=soup.find_all('img')
        # st.write(a_tags)




        for i in a_tags:
            aa=i.get('src')
            final_urls.append(aa)

        f_u=final_urls[0:int(total_images)]
        # st.write(f_u)

        
        
        for i in f_u:
            filename=i.split('/')[-1]
            f_1=filename.split('?')[0]
            
            response_1=urlopen(i)
            image=response_1.read()
            handle.writestr(f_1,image)


        handle.close()


        st.info("All Images has been Extracted from Website, Click on the below Download button to Download the Images")

        
        dwnld=st.download_button(data=open('sample.zip','rb'),file_name='sample.zip',label='Download')