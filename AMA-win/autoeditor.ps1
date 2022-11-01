Set-Location (get-item $PSScriptRoot ).parent.FullName
git pull

Set-Location $PSScriptRoot

$filePath = ".\uselessFile.txt"

$status = (git status)
$date = Get-Date -Format "dddd yyyy/MM/dd HH:mm:ss K"
if ($status -contains "nothing to commit, working tree clean"){
    Write-Output "No changes in the repo. Creating mock modification."
    Add-Content $filePath $date
} else {
    Write-Output "Already some changes are present in the folder"
}
$logs = Join-Path "$PSScriptRoot" ".\logs.txt"
$status > $logs

Set-Location (get-item $PSScriptRoot ).parent.FullName

git add *
git status
git commit -m "[AUTO] Periodical repo update AMA-win" -S
git push origin master