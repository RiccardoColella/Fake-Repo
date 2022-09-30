#!/bin/bash

cd ${PWD}
git pull

echo "New Line\n" >> ./AMA-bash/uselessFile.txt

git add *
git status
git commit -m "[AUTO] Periodical repo update AMAbash"
git push origin master