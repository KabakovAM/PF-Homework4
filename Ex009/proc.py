import multiprocessing
import requests
import time

start = time.time()

def download(url):
    response = requests.get(url)
    filename = str(url.split('/')[-1:]).replace("['",'').replace("']",'')
    filepath = 'Homework4/Download/' + str(url.split('/')[-1:]).replace("['",'').replace("']",'')
    with open (filepath,'wb') as f:
        f.write(response.content)
    print(f'{time.time()-start:.2f} секунд - {filename}')

def main(urls):
    processes = []
    for i in range(len(urls)):
        p = multiprocessing.Process(target=download, args=(urls[i],))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print(f'{time.time()-start:.2f} секунд - общее время')