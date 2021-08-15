il=int(input('ili daxil edin'))
bir_illik_saniyeler=((365*24)*60)*60
saniyeler=il*bir_illik_saniyeler
dogush=saniyeler/8
olum=saniyeler/12
immiqrasiya=saniyeler/29
populasiya=dogush+immiqrasiya-olum
artim=dogush+immiqrasiya
print('artim: ', artim, '; azalim: ', olum, '; populasiya: ', populasiya)
