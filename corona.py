import time
import xlsxwriter
from datetime import datetime
import requests
import urllib.request
from bs4 import BeautifulSoup

m=0
#--------------------------------------------
def save_data_to_excel(file_name,data_entries,n):
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet('Statistics Covid-19')
    col=0
    for col_entry in (data_entries[0]):
            worksheet.write(0, col, col_entry)
            col+=1
    row = 2
    for row_id in range(1,len(data_entries)):
        col=0
        for col_entry in (data_entries[row_id]):
            worksheet.write(row, col, col_entry)
            col+=1
        row += 1

    # Write a total using a formula.
    worksheet.merge_range('A2:B2','World Wide')
    last_rank=str(n+1)
    col_id=ord('C')

    for i in range(2,11):
        j=chr(col_id)
        col_id+=1
        worksheet.write(1, i, '=SUM('+j+'3:'+j+last_rank+')')
    worksheet.write(1, 11, url)
    workbook.close()    
#--------------------------------------------
def get_data_entries(request_response):
    soup=BeautifulSoup(response.text,"html.parser")
    
    title=soup.find('title')
    print(title.text)
    print("Source: "+url)
    
    general_info=soup.findAll("div",{"class":"card-content"})
    
    links=general_info[14].findAll("a")
    infected=general_info[14].findAll("td")
    tabh=general_info[14].findAll("th")
    
    j=0
    stat=[["RANK"]]
    for i in range(len(tabh)):
        stat[j].append(tabh[i].text)
    stat[j].append("MORE DETAILS")
    m=len(links)
    while j<m:
        i=j*10
        j=j+1
        stat.append([j, 
            infected[i+0].text.replace('\n',''),
            int(infected[i+1].text.replace(',','')),
            int(infected[i+2].text.replace(',','')),
            int(infected[i+3].text.replace(',','')),
            int(infected[i+4].text.replace(',','')),
            int(infected[i+5].text.replace(',','')),
            int(infected[i+6].text.replace(',','')),
            int(infected[i+7].text.replace(',','')),
            int(infected[i+8].text.replace(',','')),
            int(infected[i+9].text.replace(',','')),
            links[j-1]["href"]])
    return stat
def corona():
    url="https://corona.help/"
    response=requests.get(url)
    if response.ok:
        stat=get_data_entries(response)
        data=[]
        for c in stat[1:]:
          ks=stat[0]
          d={}
          for i in range(len(ks)):
            d[ks[i]]=c[i]
          data.append(d)
        print(data[0])
        return data
    return []