import requests
import datetime
TOK="q1e2rr3t3t3y737y"
USER="sakthik"
GRAP_ID="mytrip"
responce="https://pixe.la/v1/users"
user_pare={
    "token":TOK,
    "username":USER,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# abb=requests.post(url=responce,json=user_pare)
# print(abb.text)
endpoint_grap=f"{responce}/{USER}/graphs"
grap={
    "id":GRAP_ID,
    "name":"cycling",
    "unit":"Km",
    "type":"float",
    "color":"kuro"
}
headers={
    "X-USER-TOKEN":TOK
}
today=datetime.datetime.now()

# res=requests.post(url=endpoint_grap,json=grap,headers=headers)
# print(res.text)
pixel=f"{responce}/{USER}/graphs/{GRAP_ID}"
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"10.7",

}
ax=requests.post(url=pixel,json=pixel_data,headers=headers)
print(ax.text)
