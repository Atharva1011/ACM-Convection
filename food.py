from io import BytesIO
from tkinter import Image
import wolframalpha
import requests
from IPython import display
from PIL import Image

def nutrients(food): 
    food=food+"nutritional info"
    app_id="RLWKY9-EUT258WJ5X"
    client=wolframalpha.Client(app_id)
    res=client.query(food)
    url=res.pod[1].subpod.img.src
    # print(url)
    response=requests.get(url)
    img=Image.open(BytesIO(response.content))
    # print(res)
    ans=next(res.results).text
    # li = list(ans.split(" "))
    # print(li)
    # print(type(ans))
    # print(ans[40:])
    return url
    # Image(url)
    # print(img)
    # return Image(url)
    # next(ans)

# nutrients("cherry")