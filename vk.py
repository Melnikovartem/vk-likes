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
        print("Всего постов:", data['response'][0])
        for i in answer:
            print(i[0], "это", end = " ")
            proc = round(i[0]/data['response'][0] *100)
            if proc >= 10:
                print(str(proc) + "% от всех постов", end = " ")
            else:
                print(" " + str(proc) + "% от всех постов", end = " ")
            print("<-" , i[1])
            

if __name__ == '__main__':
    Us = User("154044544")
    Us.Wall()


