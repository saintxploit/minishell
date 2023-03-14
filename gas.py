import os

print("Welcome to Ftp & LazyConfig Tools Hunter")
print("Silakan Pilih Menu:")
print("1. Ftp Hunter")
print("2. Split Ftp")
print("3. Cek Ftp")
print("4. LazyConfig")
print("5. Clean Domain")
print("6. Sql Checker")
print("7. ExtractorDB")
print("8. RemoteSql Checker")
print("9. ExtracDB For CpCrack")
print("10. Cpcrack From DB")

def screen_clear():
    os.system('cls')
# Input pilihan pengguna

data = {
    '1':'ftphunter.py',
    '2':'ftpsplit.py',
    '3':'checkftp.py',
    '4':'lazyconfig.py',
    '5':'clean.py',
    '6':'sqlcek.py',
    '7':'extracdb.py',
    '8':'remote.py',
    '9':'extraccp.py',
    '10':'cpcarck.py'
}

SCRIPT_DIR = "Script"

pilihan = input("Masukan Pilih dengan Angka 1, 2, atau 3: ")
if data.get(pilihan):
    full_path = os.path.join(SCRIPT_DIR, data.get(pilihan))
    os.system(f'python3 {full_path}')
else:
    print('ga ada ')
