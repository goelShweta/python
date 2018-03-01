import urllib.request

def download_img(url):
    '''
    downloading an image
    :param url:
    :return:
    '''
    #name="img_file"
    #fullname=name+".jpg"
    #urllib.request.urlretrieve(url,fullname)
    urllib.request.urlretrieve(url, "pic.jpg")

download_img("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtvqeQzj894KDazWPpn68h_CXx0H5yHZFxsHFHrDZE-sBj_YAY")
