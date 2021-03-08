#попытка парсера текстогового файла по ключивым словам

san_tex_ka = ('труб', "клип", "фильт", "хомут", "термо", "фум",  "отво", "пуск", 'аме','кран','сче', "тро", "прож", "муф", "бак","аэр", "шлан", "уго", "сиф", "сме", "унит", "изол", "пису", "реви", "перех", "ради")
elek_ri_ka = ('авт', "пуска", "пров", "расп", "патро", "управ", "кабе","шин", "нако", "вык", "датч", "ламп", "свет", "щит", "рубил", "вста", "выкл", "розе", "коро","гофр", "сче" )
plot_malj_worc = ("доск", "проф", "фасон", "шпиль", "подлж", "плинт", "нали", "сигн", "масти" "дюбел", "газ", "круг", "само", "двер", "цеме", "кле", "герм", "угол", "сили", "крас", "труб", "пила", "лез" )
plitochn_worc = ("плит", "зати", "кера", "кле", "крест")
#Сменили на маленкий шрифт и split сдулал лист
#san_tex_ka_new = ('PR-R  Тройник переходной 32-20-32	БУ	50,000	1 020,00').lower().split(
san_tex_ka_new = ('pr-r', 'тройник', 'переходной', '32-20-32')#, 'БУ', '50,000', '1 020,00')

print(san_tex_ka_new)
sbo_san_tex_ka = []
ves_txt = []
rasdel_1 = []

f = ('tool', 'storng')
print(f)

def pars_txt(rasdel):
    with open('C:/Users/Стас/Documents/andr/tutorial/new prog/tutorial modul/name__mane/parser one/TSSC_baza.txt', 'r') as rask_txt_file:
    #with open('C:/Users/Стас/Documents/andr/tutorial/new prog/tutorial modul/name__mane/parser one/, 'r')
        lens = rask_txt_file.readline()
        for s in rask_txt_file:#
            #ves_txt.append(s)
            for i in rasdel:#.split():
                #print(i)#
                if i in s.lower():#
                    rasdel_1.append(s)
                    print(s,end='')
                # elif i not in s.lower():
                #     #print(s,end='')
                    lens = rask_txt_file.readline()
# доделка убрать повтряющиеся из номеров и вывести не вошедшие
pars_txt(san_tex_ka_new)
print(rasdel_1)
print('________________________________________________________________________________________________')
# pars_txt(elek_ri_ka)
# print(rasdel_1)
# print("_________________________________________________________________________________________________")
# pars_txt(plot_malj_worc)
# print(rasdel_1)
# print("_________________________________________________________________________________________________")
# pars_txt(plitochn_worc)
# print(rasdel_1)
# print("_________________________________________________________________________________________________")



    # for s in rask_txt_file:
    #     ves_txt.append(s)
    #     for i in san_tex_ka:
    #         if i in s.lower():
    #             col_vo += 1
    #             print(s,end='')
    #             lens = rask_txt_file.readline()
# print()
# print(ves_txt)