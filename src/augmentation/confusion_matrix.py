# 1-) TEST.TXT ICERISINDEKI DOSYA ISIMLERININ OLDUGU LISTE

test_ls = [] 
with open('/Users/ahmedsaidgulsen/Desktop/codes/robotaksi/test.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        list = line.rstrip().split('/')
        new_item = list[8].replace('.jpg','.txt')
        test_ls.append(new_item)
        # print(list[8])
# print(len(test_ls))
# print((test_ls))

# 2-) SADECE SAGADONULMEZ CLASS'INI ICEREN DOSYA ISIMLERI LISTESI

def generate_class_list(class_name_ls, class_number):
    class_name_ls = []
    b = 0
    for file_name in test_ls:
        with open(f'/Users/ahmedsaidgulsen/Downloads/dataset1/{file_name}', 'r') as file:
            a = 0
            for line in file.readlines():
                a += 1
            if a == 1: 
                if int(line[0]) == class_number:
                    b += 1
                    class_name_ls.append(file_name.replace('.txt','.jpg'))
                    # print(line.rstrip())
                    # print(file_name)
    # print(class_name_ls)
    # print(len(class_name_ls))
    # print(b)
    return class_name_ls
'''
2-) ve 3-) MADDELERINDE 6 DEFA FONKSIYONLARI CAGIRMAK YERINE FOR KULLANIP FONSKSIYONU ICINE ALABILIRDIK :D
'''
# only_sagadonulmez_ls = generate_class_list('only_sagadonulmez_ls', 4)
# only_soladonulmez_ls = generate_class_list('only_soladonulmez_ls', 5)
# only_sagmecburi_ls = generate_class_list('only_sagmecburi_ls', 8)
# only_solmecburi_ls = generate_class_list('only_solmecburi_ls', 9)
# only_ilerisag_ls = generate_class_list('only_ilerisag_ls', 6)
# only_ilerisol_ls = generate_class_list('only_ilerisol_ls', 7)


# 3-) OLUSTURDUGUMUZ LISTELERI DRIVEIM'DAKI KLASORLERE AKTARMAK
def transfer_2_drive(class_name_ls, directory_name):
    import shutil
    import os
    source_path = '/Users/ahmedsaidgulsen/Downloads/dataset1'
    destination_root = '/Users/ahmedsaidgulsen/Google Drive/My Drive/yolo/'
    for jpg_name in class_name_ls:
        source_file = os.path.join(source_path, jpg_name)
        destination_directory = os.path.join(destination_root, directory_name)
        destination_file = os.path.join(destination_directory, jpg_name)
        
        try:
            os.makedirs(destination_directory, exist_ok=True)  # Hedef dizini oluştur veya varsa devam et
            shutil.copy2(source_file, destination_file)
            print(f"{jpg_name} başariyla kopyalandi.")
        except Exception as e:
            print(f"{jpg_name} kopyalanamadi. Hata: {str(e)}")
# transfer_2_drive(only_sagadonulmez_ls, 'sagadonulmez')
# transfer_2_drive(only_soladonulmez_ls, 'soladonulmez')
# transfer_2_drive(only_sagmecburi_ls, 'sagmecburi')
# transfer_2_drive(only_solmecburi_ls, 'solmecburi')
# transfer_2_drive(only_ilerisag_ls, 'ilerisag')
# transfer_2_drive(only_ilerisol_ls, 'ilerisol')


