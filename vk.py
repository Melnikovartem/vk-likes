# Сделал Артем Мельников
from urllib.request import urlopen
from json import loads
def Show_name(id):
        url_ = "https://api.vk.com/method/users.get?user_ids=" + id
        data = loads(urlopen(url_).read().decode('utf8'))
        return data['response'][0]['first_name'] + " " + data['response'][0]['last_name']
def bubble(li):
    n = 1 
    while n < len(li):
        for i in range(len(li)-n):
            if li[i][0] > li[i+1][0]:
                li[i],li[i+1] = li[i+1],li[i]
        n += 1
    li.reverse()
    return li
class User():
    def __init__(self, id):
        self.id = id
    def ShowLikes(self, post):
        url_ = "https://api.vk.com/method/likes.getList?type=post&owner_id=" + self.id + "&item_id=" + str(post)
        data = loads(urlopen(url_).read().decode('utf8'))
        return data['response']['users']
    def Wall(self):
        url_ = "https://api.vk.com/method/wall.get?filter=owner&owner_id=" + self.id
        data = loads(urlopen(url_).read().decode('utf8'))
        likes = {}
        own_likes = []
        for i in data['response'][1:]:
            like_ = self.ShowLikes(i["id"])
            for j in like_:
                p = str(j)
                if not(likes.get(p)):
                    likes[p]=0
                likes[p]+=1
                if own_likes.count(p) == 0:
                    own_likes.append(p)
        answer = []
        for i in own_likes:
            answer.append([likes[i], Show_name(i)])
        answer = bubble(answer)
        want = ''
        want = want + "Всего постов: " + str(data['response'][0]) + "\n"
        for i in answer:
            want = want + str(i[0]) + " это" + " "
            proc = round(i[0]/data['response'][0] *100)
            if proc >= 10:
                want = want + str(proc) + "% от всех постов"
            else:
                want = want + " " + str(proc) + "% от всех постов"
            want = want + " <-" + i[1] + "\n"
        return want

if __name__ == '__main__':
    friends = [
        ["Таня",   "350537453"],#1 Таня Газина
        ["Артем",  "154044544"],#2 Артем Мельников
        ["Света",  "81122639"],#3 Света Сельдекова
        ["Козьмин","2551535"], #id не тот #4 Евгений Козьмин
        ["Валера", "160121690"], #Traceback (most recent call last): #5 Валера Березовский
        ["Варя",   "155311228"],#6 Варя Макаревич
        ["Максим", "186801334"],#7 Максим Ященко
        ["Миша",   "108598243"],#8 Миша Исаев
        ["Леня",   "368620811"],#9 Леня Горский
        ["Семен",  "238403397"],#10 Семен Буянов
        ["Юра",    "184056688"],#11 Юра Зюзин
        ["Ортем",  "239377714"],#12 Артем Спесивцев
        ["МашаШ",  "161472358"]#13 Маша Шестопалова
        ]
    
    for i in friends:
        print(i[0])
        con = open("friends/" + i[0]+".txt","w")
        Us = User(i[1])
        try:
                con.write(Us.Wall())
        except:
                print(i[0] + " - ошибка")  
    print("Все готово")
