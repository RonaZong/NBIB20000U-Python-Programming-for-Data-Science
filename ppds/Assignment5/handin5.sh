# 1
time python handin5_test1.py

# 2
time python handin5_test2.py

# 3
time python handin5_test3.py

# 4
diff -U $(wc -l < british-english) british-english american-english | sed -n 's/^-//p' | sed 1d | wc -l
diff british-english american-english | grep '<' | wc -l

# 5
time < $(diff -U $(wc -l < british-english) british-english american-english | sed -n 's/^-//p' | sed 1d)
