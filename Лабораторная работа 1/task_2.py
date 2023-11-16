# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
strings = 50
symbols = 25
kb = 1024
bty = 4
disk_vol = 1.44
volume = symbols * strings * pages * bty/kb
cnt = int((disk_vol * kb // volume))
print("Количество книг, помещающихся на дискету:", cnt)
