# -*- coding: utf-8 -*-
from com.ziclix.python.sql import zxJDBC

import random
import os

file_db = os.getenv("DIR_DB") # Чтобы установить путь к бд укажите его в файле run в переменной DIR_DB
jdbc_url = "jdbc:ucanaccess://"+file_db
username = ""
password = ""
driver_class = "net.ucanaccess.jdbc.UcanloadDriver"
nameTable = "homework"

listLog = []

def saveList(list):
    file_log = os.getenv("DIR_FILE_LOG")  # Чтобы установить путь к бд укажите его в файле run в переменной DIR_DB
    f = open(file_log, "a")
    f.write("\n" + "\n".join(str(x) for x in list))
    f.close()


def getRandNameFemale():
    name = [u'Светлана', u'Елена', u'Анастасия', u'Ольга', u'Инесса', u'Мария', u'София', u'Вера', u'Алла',
            u'Екатерина',
            u'Полина', u'Людмила']
    randomindexName = random.randint(0, len(name) - 1)
    return name[randomindexName]


def getRandNameMan():
    name = [u'Дмитрий', u'Андрей', u'Александр', u'Евгений', u'Данила', u'Егор', u'Виктор', u'Сергей', u'Роман',
            u'Кирилл',
            u'Иван']
    randomindexName = random.randint(0, len(name) - 1)
    return name[randomindexName]


def getRandFamilyName():
    list = [u'Рыжкин', u'Садыков', u'Иваньшин', u'Шустов', u'Белов', u'Беглов', u'Иванов', u'Волков', u'Абзалов',
            u'Хлестков', u'Муравьев', u'Лапкин']
    randomindexName = random.randint(0, len(list) - 1)
    return list[randomindexName]


def getRandOtchMan():
    name = [u'Дмитриевич', u'Андреевич', u'Александрович', u'Евгеньевич', u'Данилович', u'Викторович', u'Сергеевич',
            u'Иванович',
            u'Алексеевич']
    randomindexName = random.randint(0, len(name) - 1)
    return name[randomindexName]


def getRandOtchWomen():
    name = [u'Дмитриевна', u'Андреевна', u'Александровна', u'Евгеньевна', u'Викторовна', u'Сергеевна', u'Ивановна',
            u'Алексеевна']
    randomindexName = random.randint(0, len(name) - 1)
    return name[randomindexName]


def getRandSubject():
    name = [u'База данных', u'Программирование', u'ОПОИБ', u'Кодирование информации', u'Биология', u'Физика',
            u'Астрономия',
            u'Английский язык', u'ОБЖ', u'Операционные системы',
            u'Русский язык',
            u'Теория вероятности', u'Эксплуатация КС', u'Маркейтинг', u'БЖД']
    randomindexName = random.randint(0, len(name) - 1)
    return name[randomindexName]


def getRandDate():
    year = random.randrange(2017, 2021)
    month = random.randrange(1, 13)
    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)
    day = random.randrange(1, 29)
    if day < 10:
        day = "0" + str(day)
    else:
        day = str(day)
    return str(year) + "-" + month + "-" + day


def createTables(iTable):
    cnxn = zxJDBC.connect(jdbc_url, username, password, driver_class)
    crsr = cnxn.cursor()
    execTab = "CREATE TABLE " + nameTable + str(
        iTable + 1) + " (ID INT NOT NULL PRIMARY KEY, FIO CHAR(200) NOT NULL, nameSup CHAR(200) NOT NULL, DT DATE NOT NULL, mark BIT DEFAULT 0 NOT NULL)"
    listLog.append(execTab)
    print(str(iTable + 1) + ")Создана таблица запросом: " + execTab)
    crsr.execute(execTab)
    crsr.close()
    cnxn.commit()
    cnxn.close()


def createInstans(i):
    cnxn = zxJDBC.connect(jdbc_url, username, password, driver_class)
    crsr = cnxn.cursor()
    for iInsert in range(50):
        gender = random.randrange(2)
        mark = random.randrange(2)

        if gender == 1:  # мужик или не мужик вот в чем вопрос ¯\_(ツ)_/¯
            firstName = getRandNameMan()
            familyName = getRandFamilyName()
            otch = getRandOtchMan()
        else:
            firstName = getRandNameFemale()
            familyName = getRandFamilyName() + 'a'
            otch = getRandOtchWomen()

        fio = firstName + " " + familyName + " " + otch
        execIns = "INSERT INTO " + nameTable + str(i + 1) + " (ID, FIO, nameSup, DT, mark) VALUES (" + str(
            iInsert + 1) + ", '" + fio + "', '" + getRandSubject() + "', '" + getRandDate() + "', " + str(mark) + ")"
        listLog.append(execIns.encode("utf-8"))
        print(str(iInsert + 1) + ")Создан запрос запросом: ", execIns.encode("utf-8"))
        crsr.execute(execIns)

    crsr.close()
    cnxn.commit()
    cnxn.close()

# i = table1-10
# id primary key, Имя препода, наименование дисциплины, дата проведения занятия, оценка bool
i = int(os.getenv('i'))

createTables(i)
createInstans(i)
saveList(listLog)
