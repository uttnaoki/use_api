# coding:utf-8
import requests
import json

def get_resas(key, url):
    x = json.loads(requests.get('https://opendata.resas-portal.go.jp/' + url, headers = {"X-API-KEY":key}).text)

    # return(x['result'])
    return (x)
    # return(x['message'],x['result'])

api_key = 'key'
forIndustry = 'api/v1/industry/power/forIndustry' #産業特化係数
empnum = 'api/v1/municipality/employee/perYear' #従業者数（事業所単位）

cityCodeSet = [
    "33202", # 倉敷市
    "33205", # 笠岡市
    "33207", # 井原市
    "33208", # 総社市
    "33209", # 高梁市
    "33210", # 新見市
    "33216", # 浅口市
    "33423", # 早島町
    "33445", # 里庄町
    "33461", # 矢掛町
]

sum_value = {
    "33202": 0, # 倉敷市
    "33205": 0, # 笠岡市
    "33207": 0, # 井原市
    "33208": 0, # 総社市
    "33209": 0, # 高梁市
    "33210": 0, # 新見市
    "33216": 0, # 浅口市
    "33423": 0, # 早島町
    "33445": 0, # 里庄町
    "33461": 0 # 矢掛町
}

simcCodeSet = [
    "09", # 食料品製造業
    "10", # 飲料・たばこ・飼料製造業
    "11", # 繊維工業
    "12", # 木材・木製品製造業（家具を除く）
    "13", # 家具・装備品製造業
    "14", # パルプ・紙・紙加工品製造業
    "15", # 印刷・同関連業
    "16", # 化学工業
    "17", # 石油製品・石炭製品製造業
    "18", # プラスチック製品製造業（別掲を除く）
    "19", # ゴム製品製造業
    "20", # なめし革・同製品・毛皮製造業
    "21", # 窯業・土石製品製造業
    "22", # 鉄鋼業
    "23", # 非鉄金属製造業
    "24", # 金属製品製造業
    "25", # はん用機械器具製造業
    "26", # 生産用機械器具製造業
    "27", # 業務用機械器具製造業
    "28", # 電子部品・デバイス・電子回路製造業
    "29", # 電気機械器具製造業
    "30", # 情報通信機械器具製造業
    "31", # 輸送用機械器具製造業
    "32", # その他の製造業
]

sicName = []
# value_unpan = []
# value_seizo = []
# value_yuso = []
# value_hanbai = []
# value_gyomu = []
# value_service = []
# value_okayama = []

# value_tmp = []
value2012 = []
value2014 = []
param = "?prefCode=33&sicCode=D"
f = open('data', 'w')
f.write('分類,value')
f.write('\n')
for cityCode in cityCodeSet:
    url = empnum + param + '&cityCode=' + cityCode + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"建設",')
f.write(str(value_okayama))
f.write('\n')

# value_tmp = []
value2012 = []
value2014 = []
param = "?prefCode=33&sicCode=E"
for cityCode in cityCodeSet:
    url = empnum + param + '&cityCode=' + cityCode + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"製造",')
f.write(str(value_okayama))
f.write('\n')

# value_tmp = []
value2012 = []
value2014 = []
param = "?prefCode=33&sicCode=H"
for cityCode in cityCodeSet:
    url = empnum + param + '&cityCode=' + cityCode + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"輸送関連",')
f.write(str(value_okayama))
f.write('\n')

# value_tmp = []
value2012 = []
value2014 = []
param = "?prefCode=33&sicCode=I"
for cityCode in cityCodeSet:
    url = empnum + param + '&cityCode=' + cityCode + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"販売関連",')
f.write(str(value_okayama))
f.write('\n')

value2012 = []
value2014 = []
param = "?prefCode=33&sicCode=K"
for cityCode in cityCodeSet:
    url = empnum + param + '&cityCode=' + cityCode + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"業務管理・事務関連",')
f.write(str(value_okayama))
f.write('\n')

value2012 = []
value2014 = []
param = "?prefCode=33&sicCode=M"
for cityCode in cityCodeSet:
    url = empnum + param + '&cityCode=' + cityCode + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
param = "?prefCode=33&sicCode=Q"
for cityCode in cityCodeSet:
    url = empnum + param + '&cityCode=' + cityCode + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
param = "?prefCode=33&sicCode=R"
for cityCode in cityCodeSet:
    url = empnum + param + '&cityCode=' + cityCode + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"サービス業",')
f.write(str(value_okayama))
f.write('\n')

value2012 = []
value2014 = []
param = "?cityCode=-&sicCode=D"
for i in range(1,48):
    print(str(i))
    url = empnum + param + '&prefCode=' + str(i) + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    print(resultjson)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"運搬",')
f.write(str(value_okayama))
f.write('\n')

value2012 = []
value2014 = []
param = "?cityCode=-&sicCode=E"
for i in range(1,48):
    print(str(i))
    url = empnum + param + '&prefCode=' + str(i) + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    print(resultjson)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"製造",')
f.write(str(value_okayama))
f.write('\n')

value2012 = []
value2014 = []
param = "?cityCode=-&sicCode=H"
for i in range(1,48):
    print(str(i))
    url = empnum + param + '&prefCode=' + str(i) + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    print(resultjson)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"輸送関連",')
f.write(str(value_okayama))
f.write('\n')

value2012 = []
value2014 = []
param = "?cityCode=-&sicCode=I"
for i in range(1,48):
    print(str(i))
    url = empnum + param + '&prefCode=' + str(i) + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    print(resultjson)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"販売関連",')
f.write(str(value_okayama))
f.write('\n')

value2012 = []
value2014 = []
param = "?cityCode=-&sicCode=K"
for i in range(1,48):
    print(str(i))
    url = empnum + param + '&prefCode=' + str(i) + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    print(resultjson)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"業務管理・事務関連",')
f.write(str(value_okayama))
f.write('\n')

value2012 = []
value2014 = []
param = "?cityCode=-&sicCode=M"
for i in range(1,48):
    print(str(i))
    url = empnum + param + '&prefCode=' + str(i) + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    print(resultjson)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
param = "?cityCode=-&sicCode=Q"
for i in range(1,48):
    print(str(i))
    url = empnum + param + '&prefCode=' + str(i) + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    print(resultjson)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
param = "?cityCode=-&sicCode=R"
for i in range(1,48):
    print(str(i))
    url = empnum + param + '&prefCode=' + str(i) + '&simcCode=-'
    resultjson = get_resas(api_key, url)
    print(resultjson)
    value2012.append(resultjson['result']['data'][1]['value'])
    value2014.append(resultjson['result']['data'][2]['value'])
a = 0
b = 0
for tmp in value2012:
    a += tmp
for tmp in value2014:
    b += tmp
value_okayama = (b-a)/a
value_okayama *= 100
f.write('"サービス業",')
f.write(str(value_okayama))
f.write('\n')






f.close()

# for cityCode in cityCodeSet:
#     for simcCode in simcCodeSet:
#         url = empnum + param + '&cityCode=' + cityCode + '&simcCode' + simcCode
#         print(url)
#         resultjson = get_resas(api_key, url)
#         edata = resultjson['data']
#         rlen = len(resultjson['data'])
#         sum_value[resultjson['cityCode']] += resultjson['data'][rlen-1]['value']
#         print(resultjson['cityName'])
#         print(resultjson['data'][rlen-1]['value']) # rlen-1 で最新データのみを指定
#         print(resultjson['data'][rlen-1]['year']) # rlen-1 で最新データのみを指定
#         json.dump(resultjson, f, ensure_ascii=False)
#         f.write(',\n')
#         print(sum_value)
