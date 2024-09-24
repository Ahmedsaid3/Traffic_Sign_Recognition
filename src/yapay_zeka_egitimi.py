from PIL import Image
import os

# 1-) DATASETIMI CLASS'LARA GORE INCELEME

# dataset1: txt filtreleme     
'''
dataset_path = '/Users/ahmedsaidgulsen/Downloads/dataset1'
for filename in os.listdir(dataset_path):
    if filename.endswith('.txt'):
        txt_file_path = os.path.join(dataset_path, filename)
        with open(txt_file_path, 'r') as txt_file:
            content = txt_file.read()
            list = content.split()
            if '16' in list[0]:
                print(list)
                print(f"Found '16' in file: {txt_file_path}")        
'''


# dataset1: class'lara gore gorselleri uretme
'''       
dataset_path = '/Users/ahmedsaidgulsen/Downloads/dataset1'
for filename in os.listdir(dataset_path):
    if filename.endswith('.txt'):
        txt_file_path = os.path.join(dataset_path, filename)
        with open(txt_file_path, 'r') as txt_file:
            content = txt_file.read()
            list = content.split()
            if '15' in list[0]:
                jpg_filename = filename.replace('.txt', '.jpg')  # .txt uzantisini .jpg ile değiştir
                jpg_file_path = os.path.join(dataset_path, jpg_filename)
                image = Image.open(jpg_file_path) # txt dosyasinda 'with open' ile acmistik, burada ise PIL kutuphanesini kullandik
                image.show()
'''

# 2-) DATASETIMDE HANGI CLASS ICIN KAC FOTO OLDUGUNU OGRENME

'''
ls = []
dataset_path = '/Users/ahmedsaidgulsen/Downloads/dataset1'
for filename in os.listdir(dataset_path):
    if filename.endswith('.txt'):
        txt_file_path = os.path.join(dataset_path, filename)
        with open(txt_file_path, 'r') as txt_file:
            lines = txt_file.readlines()
            for line in lines:
                list = line.split()
                if '13' in list[0]:
                    ls.append('a')      
print(len(ls))
'''

# 3-) HERHANGI BIR DOSYADA KAC FOTO OLDUGUNU BULMA

'''
ls = []
dosya_adi_txt_path = '/Users/ahmedsaidgulsen/Downloads/dosya_adi.txt'
with open (dosya_adi_txt_path,'r') as file:
    lines = file.readlines()
    for line in lines:
        ls.append('a')
print(len(ls))
'''

# 4-) TRAIN, VALID, TEST DOSYALARININ OLUSTURULMASI

# dataset_ls: datasetteki resimlerin isimlerinin yazili oldugu bir liste
'''
dataset_path = '/Users/ahmedsaidgulsen/Downloads/dataset1'
dataset_ls = [filename for filename in os.listdir(dataset_path) if filename.endswith('.jpg')]
print(len(dataset_ls))
'''

# train,valid,test edilecek fotolarin duzenlenmesi:
'''
ls = []
with open('/Users/ahmedsaidgulsen/Downloads/dosya_adi.txt', 'r') as file:
        for path in file.readlines():
            dosya_adi_ls = path.rstrip().split('/')
            # print(dosya_adi_ls[8])
            if dosya_adi_ls[8] in dataset_ls:
                ls.append(dosya_adi_ls[8])
print(len(ls))            
'''

# sonucta elde edilen listeden train,valid,test txt dosyalarinin olusturulmasi
'''
with open('dosya_adi.txt', 'w') as file:
    for jpg_file in ls:
        file.write(f'/content/darknet/build/darknet/x64/data/obj/{jpg_file}\n')
'''


# 5-) TRAIN, VALID VE TEST DOSYALARININ BIRBIRINDEN FARKLI DATASETLER OLDUGUNU INCELEME

# train listesinde valid ve test txt'lerinden foto olmadigini gosterme
'''
train_ls = [] 
with open('train.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        list = line.rstrip().split('/')
        train_ls.append(list[8])
# print(train_ls)

ls = []
with open('valid.txt', 'r') as file:
        for path in file.readlines():
            valid = path.rstrip().split('/')
            # print(valid[8])
            if valid[8] in train_ls:
                ls.append(valid[8])
print(len(ls)) 

ls = []
with open('test.txt', 'r') as file:
        for path in file.readlines():
            test = path.rstrip().split('/')
            # print(test[8])
            if test[8] in train_ls:
                ls.append(test[8])
print(len(ls)) 
'''

# valid listesinde test txt'sinden foto olmadigini gosterme
'''
valid_ls = [] 
with open('valid.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        list = line.rstrip().split('/')
        valid_ls.append(list[8])
# print(valid_ls)

ls = []
with open('test.txt', 'r') as file:
        for path in file.readlines():
            test = path.rstrip().split('/')
            # print(test[8])
            if test[8] in valid_ls:
                ls.append(test[8])
print(len(ls)) 
'''


# 6-) TOPLAM FOTO SAYILARI VE DAGILIMLARI
'''
dataset : 19291 tane jpg ve 19291 tane txt
download'daki train.txt : 13017, datasetle eslesen train.txt: 12929
download'daki valid.txt : 3894, datasetle eslesen valid.txt: 3868
download'daki test.txt : 1926, datasetle eslesen test.txt: 1908
toplam download'daki : 18837, datasetle eslesen toplam : 18705
'''
 
# 7-) colab'de test etmek icin foto isimlerinin yazili oldugu liste
'''
test_ls = [] 
with open('test.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        list = line.rstrip().split('/')
        test_ls.append(list[8])
        # print(list[8])
print(test_ls)
'''

# 8-) Txt dosyasindaki satir sayisini bulma
'''
# File path
file_path = "traincopy.txt"

# Open the file in read mode
with open(file_path, 'r') as file:
    # Count the number of lines
    num_lines = sum(1 for line in file)

print("Number of lines in the file:", num_lines)
'''


