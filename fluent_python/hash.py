import json

a =
{
  "id": 1,
  "name": "上海相亲群",
  "image": "http://img4.imgtn.bdimg.com/it/u=1114585158,1026985006&fm=27&gp=0.jpg",
  "bg_image": "http://bpic.588ku.com/back_pic/05/11/08/37598fd214cc4a8.jpg!/fh/300/quality/90/unsharp/true/compress/true",
  "descr": "相亲",
  "notice": "哈哈哈哈",
  "price": 499,
  "amount": 8,
  "joined": 0,
  "status": 1,
  "owner": {
    "owner_nickname": "都是",
    "owner_id": 4
  },
  "create_time": "2018-09-07"
}
print(json.loads(a))
