## API и python скрипт робота
В API прописаны два get endpoint-а
### "/robot" и "/robot/working_info"


При вызове ***"/robot"*** можно передать параметр value - число с которого робот начнёт отсчёт, если его не указать вывод начнётся с 0. При повторном вызове выполнение скрипта робота завершится и данные о его работе запишутся в базу данных.


При вызове ***"/robot/working_info"*** пользователь получит все данные о работе скрипта робота.