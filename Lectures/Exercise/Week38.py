# 1
ssh ppds-diku # log in
pwd # Check which directory
cd .. #Go to parent directory
ls # List all files only own directory
cd # Go to home directory
cd ~
cd tnd179
ls -la # List all files (including hidden) - long format
ls -lt # List all files sorted by date - long format

# 2
mkdir temp # Create directory
cd temp # Make temp directory current directory
mv /usr/share/dict/british-english . # Attempt to move file, no permission
cp /usr/share/dict/british-english . # Copy file to current directory
rm british-english # Remove file
ln -s /usr/share/dict/british-english . # Make symlink
rm -rf temp # Remove directory

# 3
wc -l british-english # Count number of lines
head -n 123 british-english # Find first 123 lines of file
sort -r british-english # Sort in reverse order

# 4
mkdir dict_exercise
man cp # man-page for cp command
cp -r /usr/share/dict dict_exercise/ # Copy directory, recursively
grep -i "apple" british-english # Find "apple" & "Apple in file
grep -r "apple" /usr/share/dict/ # Find "apple" in directory
sed 's/black/white/g;s/Black/White/g' dict_exercise/dict/british-english # Replace "black" with "white"

# 5
wget https://people.binf.ku.dk/wb/data/m_scrambled.txt # Download file
zip m_scrambled.txt.zip m_scrambled.txt # Add m_scrambled.txt
cp m_scrambled.txt m_scrambled_gzip.txt # Copy for gzip later
gzip m_scrambled_gzip.txt # Turn into gzip
bzip2 -k m_scrambled.txt # -k keeps the original file
ls -l m_scrambled.txt* # Compare all m_scramble files

# 6
cat british-english | nl | head -n 1500 | tail -n 501
cat british-english | nl | head -n 1500 | tail -n 501 | grep -i 'a'
cat british-english | nl | head -n 1500 | tail -n 501 | grep -i 'a' | wc -m
cat british-english | nl | head -n 1500 | tail -n 501 | grep -i 'a' | wc -l
# Download a copy
# replace from uppercase to lowercase
# complete and squeeze repeated characters everything is not a letter, 'a-z', into a single one
# start a new line
# sorts alphabetically
# counts how many unique words there are
# sorts numerically
# All: sorts words by frequency
wget http://www.gutenberg.org/cache/epuc/10/pg10.txt
cat /usr/share/dict/american-english /usr/share/dict/british-english | sort | uniq -u | wc -m
cat pg10.txt | tr 'A-Z' 'a-z' | tr -cs 'a-z' '\n' | sort | uniq -c | sort -n

#7
nano hello.py
#!/usr/bin/env python
print("Hello, World!")
./hello.py
chmod u+x hello.py
./hello.py

#8
nano wait.py
import time
time.sleep(30) # Sleep for 30 seconds
print("Done waiting!")
python wait.py
^z
python wait.py &
ps ux
kill PID