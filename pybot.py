from pybot_eto import eto_command
from pybot_random import choice_command, dice_command
from pybot_datetime import today_command, now_command
def len_command(command):
    text = command.split()
    length = len(text)
    responce = '文字列ノ個数ハ {} 個デス'.format(length)
    return responce

def heisei_command(command):
    heisei, year_str = command.split()
    if year_str.isdigit():
        year = int(year_str)
        if year >= 1989:
            heisei_year = year - 1988
            responce = '西暦{}年ハ、平成{}年デス'.format(year, heisei_year)
        else:
            responce = '西暦{}年ハ、平成デハアリマセン'.format(year)
    else:
        responce = '数値ヲ指定シテクダサイ'
    return responce

command_file = open('pybot.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    responce = word_list[1]
    bot_dict[key] = responce

while True:
    command = input('pybot> ')
    responce = ""
    try:
        for key in bot_dict:
            if key in command:
                responce = bot_dict[key]
                break

        if '平成' in command:
            responce = heisei_command(command)
        if '長さ' in command:
            responce = len_command(command)
        if '干支' in command:
            responce = eto_command(command)
        if '選ぶ' in command:
            responce = choice_command(command)
        if 'さいころ' in command:
            responce = dice_command(command)
        if '今日' in command:
            responce = today_command()
        if '現在' in command:
            responce = now_command()

        if not responce:
            responce = '何ヲ言ッテルカ、ワカラナイ'
        print(responce)

        if 'さようなら' in command:
            break
    except Exception as e:
        print('予期セヌ エラーガ 発生シマシタ')
        print('* 種類:', type(e))
        print('* 内容:', e)
