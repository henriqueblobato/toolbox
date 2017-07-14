'''
Created on 13 de jul de 2017

@author: henrique

'''

from urllib.request import urlretrieve, urlopen

URL_LIST = ['http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03800933',
            '']

for url in URL_LIST:
    response = urlopen(url)
    if not response.code == 200:
        break
    
    # type, extension = (response.headers._headers[2][1]).split('/')
    
    _, only_url_img = response.headers._headers[1]
    if 'image' in only_url_img:
        try:
            name = url.split('/')[-1]
            handler = urlretrieve(url, name)
        except Exception as e:
            pass
    else:
        lines = response.readlines()
        
        for i, line in enumerate(lines):
            i = str(i)
            line = line.decode('ascii').rstrip()
            try:
                name = line.split('/')[-1]
                handler = urlretrieve(line, name)
                print('[%s]: %s saved' %(i, name))
            except Exception as e:
                print('[%s] %s' %(format(e), line))
                pass
