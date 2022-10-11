from time import time
from urllib.request import Request
import requests as req
from bs4 import BeautifulSoup
import json
import tqdm
import time

data = {
    "data":[]
}
id = 0
for page in range(1,18):
    url ="https://hh.ru/search/vacancy?area=113&search_field=name&search_field=company_name&search_field=description&text=Python-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&page={page}&hhtmFrom=vacancy_search_list"
    # url ="https://hh.ru/search/vacancy?area=113&search_field=name&search_field=company_name&search_field=description&only_with_salary=true&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&utm_medium=widgetvacancy&utm_campaign=hh.ru_logo&utm_source=dev.hh.ru&utm_term=%2Fadmin%2Fwidgets%2Fsearch&customDomain=1&page={page}&hhtmFrom=vacancy_search_list"
    resp = req.get(url, headers={'user-agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs={"data-qa":"serp-item__title"})
    
    for iter in tqdm.tqdm(tags):
        time.sleep(2)
        url_object = iter.attrs["href"]
        resp_object = req.get(url_object, headers={'user-agent': 'Mozilla/5.0'})
        soup_object = BeautifulSoup(resp_object.text, "lxml")

        tag_region = soup_object.find(attrs={"data-qa":"vacancy-serp__vacancy-address"})
        if tag_region is None:
                tag_region = "no data"
        else:
            tag_region = tag_region.text 

        tag_price = soup_object.find(attrs={"data-qa":"vacancy-salary"})
        if tag_price is None:
                tag_price = "no data"
        else:
            if tag_price.find(attrs={"data-qa":"vacancy-salary-compensation-type-net"}) is None:
                tag_price = tag_price.find(attrs={"data-qa":"vacancy-salary-compensation-type-gross"}).text
            else:    
                tag_price = tag_price.find(attrs={"data-qa":"vacancy-salary-compensation-type-net"}).text    

        tag_experience = soup_object.find(attrs={"data-qa":"vacancy-experience"})
        if tag_experience is None:
                tag_experience = "no data"
        else:
            tag_experience = tag_experience.text 
        
        id = id + 1
        data["data"].append({"id":id, "title":iter.text, "work experience":tag_experience, "salary":tag_price,"region":tag_region})
        with open("data.json", 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, ensure_ascii=False, indent='\t'))