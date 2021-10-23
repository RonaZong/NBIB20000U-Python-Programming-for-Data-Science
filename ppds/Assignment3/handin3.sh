# 1. Log in to the "ppds-diku" server and create a directory "handin3" in current directory
mkdir handin3

# 2. Create directory "test1" in directory "handin3"
cd handin3/
mkdir test1

# 3. Download file "m_scrambled.txt" to directory "test1"
cd test1
wget https://wouterboomsma.github.io/ppds2021/data/m_scrambled.txt

# 4. Copy "test1" directory as "test2"
cd ..
cp -r test1 test2

# 5. Use "find" command to output all files and directories under "handin3" directory
find -name "*"

# 6. Remove "test2" directory
rm -rf test2

# 7. Use "cat" command to check file
cat test1/m_scrambled.txt

# 8. Unscramble the image into "m.txt" in "test1" directory
cd test1
cat m_scrambled.txt | sort -n | tee m.txt

# 9. Download, unscramble and save in a single command
wget -O m_scrambled.txt https://wouterboomsma.github.io/ppds2021/data/m_scrambled.txt && sort -g m_scrambled.txt > m.txt

# 10. Delete "handin3" directory
cd ../..
rm -rf handin3/