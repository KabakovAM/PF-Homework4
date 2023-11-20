import thr
import proc
import asy
import argparse

"""
python Homework4\Ex009\main.py -mt 'proc' --urls 'https://w.forfun.com/fetch/bc/bcad745997babea8eb3bd85b7144d1a9.jpeg' 'https://w.forfun.com/fetch/13/1330c90f7e960cebe0586865be3e0e4c.jpeg' 'https://klike.net/uploads/posts/2023-03/1679288970_3-71.jpg' 'https://ferret-pet.ru/wp-content/uploads/0/f/1/0f1123d90924be2c529e2e3a6d947ab8.jpeg' 'https://i.pinimg.com/originals/60/79/ab/6079abc6602dcf9023e419ec18964ac4.jpg' 'https://lady-dog.ru/wp-content/uploads/5/5/6/556b5c6fbc03d295870cc71a67a493cd.jpeg' 'https://sobakemozhno.ru/wp-content/uploads/2023/08/55c2802fe347ba9a51daf7c7c28af5a3.jpg' 'https://pichold.ru/wp-content/uploads/2018/11/rotveiler12.jpg' 'https://klike.net/uploads/posts/2023-03/1679288964_3-142.jpg' 'https://gagaru.club/uploads/posts/2023-02/1675877798_gagaru-club-p-milii-rotveiler-oboi-33.jpg'
"""

def download(mt, urls):
    if mt == 'thr':
        thr.main(urls)
    if mt == 'proc':
        proc.main(urls)
    if mt == 'Aasy':
        asy.run(urls)

if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('-mt', type=str, default=thr)
    parser.add_argument('--urls', nargs='+', default=[])
    args = parser.parse_args()
    download(args.mt, args.urls)