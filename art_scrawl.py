#Version: 1.00 (Dec 15. 2018)
#Author: Diana Kim (diana.se.kim@gmail.com) 
import urllib.request
import re
import ssl
import pickle
#crawling all categories under "Art_movements" depth to five.

total_depth=5
base_path=['/wiki/Category:Art_movements"']
out_file="Art_movements.pkl"
categories=set()

def write_url(old_url,depth):
    url=old_url.split("+")[-1].strip()
    if depth>total_depth:
        return    
    print(depth,old_url) 
    if url in categories:
        return
    else:
        categories.add(url)
    with urllib.request.urlopen("https://en.wikipedia.org"+url[:-1]) as f1:
        html=f1.read().decode('utf-8')
        target_pgs='<li><a href="/wiki/(?!Category:)\S*'

       
        target_sub_category='CategoryTreeItem.+/wiki/Category:\S.*?</a>'
        depth+=1
        for item in re.findall(target_sub_category,html):
            if re.search('\/wiki/Category:\S*?"',item).groups==0:
                continue#return (nothing found)
            write_url(old_url+"+"+re.search('\/wiki/Category:\S*?"',item).group(0),depth)
        
    f1.close()
    return

### main categories ###
depth=0
write_url(base_path[0],depth)
with open(out_file,"wb") as f: # set save
    pickle.dump(categories,f)
f.close()

