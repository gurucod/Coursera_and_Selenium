import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
#element.send_keys(file_path)
print(os.path.abspath(__file__))                            #Путь к исполняемому файлу
print(os.path.abspath(os.path.dirname(__file__)))          #Путь до директории где все лежит
print(file_path)                                #содержит полный путь к файлу