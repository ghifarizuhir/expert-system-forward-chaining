kamusPenyakit = {
    'penyakit':['Demam Berdarah',
               'Malaria',
               'Chikungunya',
               'Kaki Gajah',
               'Demam Penyakit Kuning',
               'Flu biasa',
               'Tidak Terdefinisi'], #isi list "Tidak Terdefinisi" harus ditempatkan paling bawah
    'aturan':[[1,2,3],
              [1,2],
              [1,3],
              [2,4],
              [2],
              [1]],
    'gejala':['Tidak ada', #isi list "Tidak ada" harus ditempatkan paling atas
              'Demam mendadak tinggi (38-40 C)',
              'Demam tiba-tiba turun',
              'Kebocoran pembuluh darah',
              'Sakit kepala berat']
}

penyakit = kamusPenyakit.get('penyakit')
aturan = kamusPenyakit.get('aturan')
gejala = kamusPenyakit.get('gejala')


def gejalaOut(indexGejala):
    for i in range(len(indexGejala)): 
        print (i, end = "       ") 
        print (indexGejala[i]) 
    print()

def hasilDiagnosis(namaPenyakit):
    i=0
    while i < len(penyakit)-1:
        if namaPenyakit == aturan[i]:
            print(penyakit[i])
            break
        else:
            i += 1

    if i == len(aturan):
        print(penyakit[i])

def diagnosisIn(listDiagnosis):
    i = 1
    while i <= (len(max(aturan, key=len))) :
        masukan = input("Masukkan kode gejala :")
        try:
            masukan = int(masukan)
            if masukan > 0 and masukan <= len(gejala)-1:
                listDiagnosis.append(masukan)
                i += 1
            elif masukan == 0:
                i += 1
            else:
                print("Masukan anda salah, ulangi lagi")
        except ValueError:
            print("Masukan anda salah, ulangi lagi")
    listDiagnosis = sorted(listDiagnosis)
    return listDiagnosis

def removeValList(x):
  return list(dict.fromkeys(x))

def utama():
    print('Sistem Pakar diagnosis Penyakit Umum pada Manusia\n\nSilahkan masukkan '+ str(len(max(aturan, key=len))) +' gejala yang anda alami :\nKode    Gejala')
    
    user_in = []

    gejalaOut(gejala)
    user_in = diagnosisIn(user_in)
    user_in = removeValList(user_in)
    print('''Berdasarkan gejala anda\ndiagnosa penyakit anda :''')
    hasilDiagnosis(user_in)

ulang = True
while ulang == True:
    utama()
    vabMasukUlang = True
    while vabMasukUlang == True:
        masukUlang = input("ingin ulang ? [y/n]")
        if masukUlang == 'y' or masukUlang == 'Y':
            ulang = True
            break
        elif masukUlang == 'n' or masukUlang == 'N':
            print("Terima kasih")
            ulang = False
            break
        else:
            print("Masukan salah!")
            vabMasukUlang = True