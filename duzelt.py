path = r"rezervasyonlar\templates\rezervasyonlar\rezervasyon_listesi.html"

f = open(path, "r", encoding="utf-8")
lines = f.readlines()
f.close()

# "odeme_ekle" gecen satiri bul (Odeme Yap linki)
idx_link = None
for i, line in enumerate(lines):
    if "odemeler:odeme_ekle" in line and "url" in line:
        idx_link = i
        break

if idx_link is None:
    print("HATA: odeme_ekle linki bulunamadi.")
else:
    print("Link satiri bulundu:", idx_link + 1)
    # Bu satirdan geriye dogru en yakin {% if satirini bul
    idx_if = None
    for i in range(idx_link, -1, -1):
        if "{% if" in lines[i]:
            idx_if = i
            break

    if idx_if is None:
        print("HATA: ilgili if satiri bulunamadi.")
    else:
        print("If satiri bulundu:", idx_if + 1)
        print("Eski hali:", lines[idx_if].strip())
        eski_sayisi = lines[idx_if].count("== 'onaylandi'")
        lines[idx_if] = lines[idx_if].replace(
            "== 'onaylandi'",
            "!= 'beklemede' and rez.durum != 'iptal'"
        )
        print("Degistirilen adet:", eski_sayisi)
        print("Yeni hali:", lines[idx_if].strip())

        f = open(path, "w", encoding="utf-8")
        f.writelines(lines)
        f.close()
        print("Kaydedildi.")