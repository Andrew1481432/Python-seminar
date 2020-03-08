#!/bin/bash
export CLASSPATH=.:/Users/andrew1481432/Documents/UCanAccess-5.0.0-bin/loader/ucanload.jar # путь к bin access для работы c access

DIR_DB="/Users/andrew1481432/Desktop/agafonov33.accdb" # путь к файлу бд
DIR_FILE_LOG="/Users/andrew1481432/Desktop/logSql.txt" # путь к лог файлу
export DIR_DB; export DIR_FILE_LOG

COUNT_TABLE=10

i=0
while [ $i -lt $COUNT_TABLE ]; do
    export i
    jython dbTest.py
    sleep 1
    i=$((i+1))
done