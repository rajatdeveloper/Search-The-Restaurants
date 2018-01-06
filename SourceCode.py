import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc="
loc = input("Enter Your Location")
s=input("want to filter [y/n]")
if s is 'y':
    x = int(input("1 for filter by Rating and 2 for filter by Most Reviewed "))
    if x is 1:
        filter = "&sortby=rating"
    else:
        filter = "&sortby=review_count"
else:
    filter = ""
page = "0"
url = base_url + loc +"&start="+page+filter
yelp_r = requests.get(url)
#request pagesource of given url

# yelp_r --- <response 200>

#print(yelp_r.status_code)

#print(yelp_r.text) --- give pagesource

yelp_soup = BeautifulSoup(yelp_r.text,'html.parser')

#print(yelp_soup.prettify()) --- make content easier to parse and read

name = yelp_soup.findAll('a',{'class':'biz-name js-analytics-click'})
#address = yelp_soup.findAll('address')
#phone = yelp_soup.findAll('span',{'class':'biz-phone'})
item = yelp_soup.findAll('span',{'class':'category-str-list'})
address = yelp_soup.findAll('div',{'class':'secondary-attributes'})

print("-----------------------------------------------------------------------------")
print("Required List of Top 10 Hotels is:->")
for k in range (len(name)):
    print("Restaurants Name: "+((name[k].text).strip()))
    print("Address:")
    print(" ".join((address[k].text).split()))
    #print((address[k].text).strip())
    #print("Phone No.")
    #print((phone[k].text).strip())
    print("Item Category:")
    print(" ".join((item[k].text).split()))
    print("-----------------------------------------------------------------------------")

#find html tag, specify using class,write text between tags