from itchat.content import *
import requests
import itchat
import function

answer_flag_6 = False
answer_flag_7 = False
answer_flag_8 = False
time_flag = False
weather_flag = False
AI_chat = False
music_flag = False
translation_flag = False

# 小豆机器人
Key = 'Your key'
Url = 'http://api.douqq.com/?key=' + Key + '&msg='


# 图灵机器人
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': 'your key',
        'info': msg
    }
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')


def initial():
    global answer_flag_6
    global answer_flag_7
    global answer_flag_8
    global time_weather_flag
    global biaoqingbao_flag
    global AI_chat
    global music_flag
    global translation_flag
    answer_flag_6 = False
    answer_flag_7 = False
    answer_flag_8 = False
    time_weather_flag = False
    biaoqingbao_flag = False
    AI_chat = False
    music_flag = False
    translation_flag = False


@itchat.msg_register([TEXT])
def text_reply(msg):
    global answer_key_6
    global answer_flag_6
    global answer_key_7
    global answer_flag_7
    global answer_key_8
    global answer_flag_8
    global time_weather_flag
    global biaoqingbao_flag
    global AI_chat
    global music_flag
    global translation_flag

    if msg.Text == '菜单':
        initial()
        msg.user.send("请选择以下数字进入对应的功能：\n1.组员介绍\n2.时间天气查询\n3.表情包制作\n4.智能聊天\n5.歌曲点播\n6.脑筋急转弯\n7.抽签\n8.翻译")

    elif msg.Text == '1' or msg.Text == '组员介绍':
        initial()
        msg.user.send("刘雨巷   陈铖\n唐启栋   周思远")

    elif msg.Text == '2' or msg.Text == '时间天气查询':
        initial()
        msg.user.send("请输入地点+时间或地点+天气")
        time_weather_flag = True

    elif msg.Text == '3' or msg.Text == '表情包制作':
        initial()
        msg.user.send("请输入表情包文字")
        biaoqingbao_flag = True

    elif msg.Text == '4' or msg.Text == "智能聊天":
        initial()
        msg.user.send("你好，我是机智 PiBot")
        AI_chat = True

    elif msg.Text == "5" or msg.Text == "歌曲点播":
        initial()
        msg.user.send("你好，请输入歌名和歌手")
        music_flag = True

    elif msg.Text == "6":
        initial()
        r = requests.get(Url + "脑筋急转弯")
        answer_flag_6 = True
        i = 0
        flag = False
        for content in r.text:
            if content == "：" and flag:
                break
            if content == "：":
                flag = True
            i += 1
        answer_key_6 = r.text[i+1:]
        return r.text.replace(answer_key_6, "求答案")

    elif msg.Text == "7":
        initial()
        r = requests.get(Url + "抽签")
        answer_flag_7 = True
        i = 0
        flag = False
        for content in r.text:
            if content == "：" and flag:
                break
            if content == "：":
                flag = True
            i += 1
        answer_key_7 = r.text[i + 1:]
        return r.text.replace(answer_key_7, "解签")

    elif msg.Text == "9":
        initial()
        r = requests.get(Url + "猜谜")
        # answer_flag_8 = True
        # i = 0
        # for content in r.text:
        #     if content == "：":
        #         break
        #     i += 1
        # answer_key_8 = r.text[i + 1:]
        # print(answer_key_8)
        return r.text
            #.replace(answer_key_8, "谜底")

    elif msg.Text == "8":
        initial()
        msg.user.send("你好，请输入需要翻译的内容")
        translation_flag = True

    else:
        if time_weather_flag:
            reply = get_response(msg.Text)
            msg.user.send(reply)
        if biaoqingbao_flag:
            function.make(msg.Text)
            msg.user.send("@img@%s" % "./static/biaoqingbao.jpg")
        if AI_chat:
            reply = get_response(msg.Text)
            msg.user.send(reply)
        if music_flag:
            msg.text += " 无"
            info = msg.text.split()
            url = function.get_musicurl(info[0], info[1])
            msg.user.send(url)
        if translation_flag:
            # reply = get_response("翻译 " + msg.Text)
            reply = requests.get(Url + "翻译" + msg.Text)
            msg.user.send(reply.text)

        if answer_flag_6:
            if msg.Text == "求答案":
                r = requests.get(Url + answer_key_6)
                return r.text.replace("继续玩，请回复：脑筋急转弯", "")
        if answer_flag_7:
            if msg.Text == "解签":
                r = requests.get(Url + answer_key_7)
                return r.text.replace("继续抽签，请回复：抽签", "")
        if answer_flag_8:
            if msg.Text == "谜底":
                print(answer_key_8)
                r = requests.get(Url + answer_key_8)
                print(r.text)
                return r.text.replace("继续猜谜语，请回复：猜谜", "")

    # msg.user.send("@img@%s" % "./static/example.gif")
    # msg.user.send('Nice to meet you!')
    # msg.user.send("@img@%s" % "./static/house.jpg")
    # itchat.send("by send", toUserName=msg.user['UserName'])
    # itchat.send_image("./static/house.jpg", toUserName=msg.user['UserName'])
    # msg.user.send_image("./static/house.jpg")
    # msg.user.send_file("./static/Sunny.mp3")
    # reply = get_response(msg['Text'])
    # default = 'I received: ' + msg['Text']
    # return reply or default


if __name__ == "__main__":
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run(debug=True)
