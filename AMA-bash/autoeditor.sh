#!/bin/bash


cd "$(dirname "$0")"
git pull

date  >> ./uselessFile.txt

git add *
git status
git commit -m "[AUTO] Periodical repo update bash"
git push origin master
