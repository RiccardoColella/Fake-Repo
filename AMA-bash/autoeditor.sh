#!/bin/bash


cd "$(dirname "$0")"
git pull

echo "New Line\n" >> ./uselessFile.txt

git add *
git status
git commit -m "[AUTO] Periodical repo update AMAbash"
git push origin master
