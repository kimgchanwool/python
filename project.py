#append module
import os
import schedule
import time
#import winsound

#commit
def git_init():
    os.system('git init') #터미널에서 실행한다 해당내용을.
    print('git init')
    os.system('git add -A')
    print('git add -A')
    os.system('git commit -m "init"')
    print('git commit -m "init"')

    URL = input('write yout git-URL : ') #url을 인풋받기
    os.system(f'git remote add origin {URL}') #formating이용해서 url 과 연동.
    os.system('git branch -M main')
    os.system('git push -u -f origin main')
#    winsound.Beep(200, 100) #완료하면 사운드 발생

    return

def auto_commit():
    this_tm = time.localtime(time.time())#현재시각 받아오기

    os.system('git add -A')
    print('git add -A')
    os.system(f'git commit -m "{this_tm.tm_year}+{this_tm.tm_mon}+{this_tm.tm_mday}+{this_tm.tm_hours}+{this_tm.tm_min}"')
    print(f'git commit -m "{this_tm.tm_year}+{this_tm.tm_mon}+{this_tm.tm_mday}+    {this_tm.tm_hours}+{this_tm.tm_min}"')
    os.system('git push -f')
    print('git push -f')

#    winsound.Beep(200, 100)
    return
#schedule
schedule.every().day.at('18:10').do(auto_commit)
schedule.every().day.at('19:39').do(auto_commit)
#schedule에서 every().day를 사용
#12:00에 실행.
# .do 는 해당 함수를 실행


#Main
if __name__=='__main__':
    if 'Y' == input('you need Init? Y or N (default: N): '):
        git_init()
#    for i in range(4):
#        winsound.Beep(150,300)

    print('!!! runing !!!')

    while True:
        schedule.run_pending()
        time.sleep(1)
