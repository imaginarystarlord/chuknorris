from urllib.request import urlopen
with open('ID.csv','r') as f:
    id = f.read()
    ids = [int(i) for i in id.split()[1::]]
list1 = [['ID','Joke']]
for id in ids:
    api_url = 'http://api.icndb.com/jokes/' + str(id)
    #print(api_url)
    url_result = urlopen(api_url)
    data = url_result.read()
    import json
    json_data = json.loads(data)
    list2 = [str(json_data['value']['id']),json_data['value']['joke']]
    list1.append(list2)
file = open('sample1.csv','w+')
for row in list1:
    file.write(row[0]+','+row[1]+'\n')
    
file.close()    





