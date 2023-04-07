# 1
wget https://wouterboomsma.github.io/ppds2021/data/british-english
wget https://wouterboomsma.github.io/ppds2021/data/british-english-subset

# 2
#diff british-english british-english-subset | grep "<" | cut -b 3 | uniq | sed -r 's/[0-9]//g' | sed '/^$/d'
diff british-english british-english-subset | grep "<" | cut -b 3 | uniq | sed -r 's/[0-9]//g'

# 3
grep '^[^XYZ]' british-english > british-english-subset2