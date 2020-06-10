import sys
import fiz_l
import property

def marriage_func(person_1, person_2): # на вход подаются физ.лица (class Fiz_l)
    # общее правило
    # TODO isinstance перестал работать после разделения программы на несколько модулей
    # if not (isinstance(person_1, Fiz_l) and isinstance(person_2, Fiz_l)):
    #     raise TypeError("Аргументы должны быть из class Fiz_l")

    # проверка на соответствие обязательным требованиям каждого отдельного лица
    place_of_marriage = 'Saint-Petersburg' # здесь нужен input по субъекту РФ

    #проверка обоих лиц по отдельности
    person = person_1
    for i in range(2):
        # проверка на статус
        if person.status['live']['alive'] == False:
            raise ValueError(f"{person} умер(ла). С мертвецом в браки не вступают")
        if person.status['marriage']['married'] == True:
            law_link = 'абз. 2 ст. 15 Семейного кодекса РФ'
            raise ValueError(f"{person} состоит в браке. Второй брак недопустим\n Cсылка на норму: {law_link}")
        if person.status['capacity']['ogranicheniya'] == True:
            law_link = 'абз. 5 ст. 15 Семейного кодекса РФ'
            raise ValueError(f"{person} признан(а) недееспособным(ой). Брак с указанным лицом невозможен\n Cсылка на норму: {law_link}")
        temp = marriage_age_check(person, place_of_marriage) # проверка на брачный возраст
        if temp != True:
            marriage_age, law_link = temp[0], temp[1]
            raise ValueError(f"{person} не достиг(ла) брачного возраста - {marriage_age},\n Cсылка на норму: {law_link}")
        person = person_2

    #проверка лиц на совместную возможность пожениться
    # проверка на однополый брак
    if not (person_1.sex == 'male' and person_2.sex == 'female' or person_1.sex == 'female' and person_2.sex == 'male'):
        law_link = 'ч.1 ст. 12 Семейного кодекса РФ'
        raise ValueError(f"Брак между лицами одного пола недопустим\n"
              f"Ссылка на норму: {law_link}")

    # проверка на родстввенные связи
    # TODO

    # итог + изменение статуса
    print(f"Брак между {person_1} и {person_2} возможен")
    print('===============')
    while True:
        print(f"Заключить брак между {person_1} и {person_2}?")
        print("1 - ДА")
        print("2 - НЕТ")
        choose = input("Введите ответ (1 или 2): ")
        if choose == '1':
            print("Введите дату заключения брака: ")
            #TODO не раньше достижения младшим супругом  брачного возраста
            date = input()
            date_of_marriage = fiz_l.to_date(date)
            person_1.status['marriage']['married'] = True
            person_1.status['marriage']['married_to'] = person_2
            person_1.status['marriage']['date_of_marriage'] = date_of_marriage
            person_2.status['marriage']['married'] = True
            person_2.status['marriage']['married_to'] = person_1
            person_2.status['marriage']['date_of_marriage'] = date_of_marriage
            print(f"Брак между {person_1} и {person_2} заключен")
            break
        elif choose == '2':
            print('===============')
            print("Оставим их в покое")
            break
        else:
            print('===============')
            print("Incorrect answer. Try again.")
            print("===============")



def marriage_age_check(person, place_of_marriage):
    marriage_age = 18 # общий брачный возраст в РФ (ст. 13 СК РФ). Еще бы как-то метку на норму сделать, но торгда нужно новый объект создавать
    law_link = 'ч.1 ст. 13 Семейного кодекса РФ'
    # TODO
    # проверить брачный возраст нужного субъекта РФ и перезаписать, если необходимо, переменную marriage_age
    # если есть уважительные причины, признанные ЗАГСом - marriage_age = 16
    # если есть особые обстоятельства по reg_law - region_law_marriage_age
    if person.age >= marriage_age:
        return True
    else:
        return (marriage_age, law_link)

def region_law_marriage_age(region):
    # TODO list of region_marriage_ages
    ...


def marriage_property_check(date_of_marriage, date_of_ownership):
    '''
    Проверка на приобретение имущества в браке
    :param date_of_marriage:
    :param date_of_ownership:
    :return:
    '''
    # допустим, что никто пока не разводился
    if date_of_ownership >= date_of_marriage: #если имущество приобретено после заключения брака
        return True # имущество приобретено в браке
    else:
        return False # имущество приобретено не в браке