#!/bin/bash

cd pwd
cd ..
git pull
cd pwd

echo "New Line\n" >> ./uselessFile.txt

cd ..
git add *
git status
git commit -m "[AUTO] Periodical repo update AMAbash"
git push origin master