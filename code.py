from bs4 import BeautifulSoup
import requests
choice={
        '1':'8MT-LQlP35c_',     #hindi
        '2':'LdbVc1Z5i9E_',     #english
        '3':'FnWfzTurhhg_',     #kannada
        '4':'W6DUe-fP3X8_'      #punjabi
      }

print('Enter your Choice 1-hindi,2-english,3-kannada,4-punjabi')
ch=input()
lang=choice[ch]

def get_song(lang):
    res=requests.get('https://www.jiosaavn.com/featured/weekly-top-/'+lang)
    soup =BeautifulSoup(res.text, 'lxml')
    data=soup.find('ol',{'class':'content-list'})
    all=data.find_all('div',{'class':'details'})
    return all

def print_all(all):
    for count,s in enumerate(all,1):
        song=s.find('p',{'class':'song-name'})
        print(count,song.text)

def saavn_main():
    all=get_song(lang)
    print_all(all)

saavn_main()
