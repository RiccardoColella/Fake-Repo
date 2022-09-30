Set-Location (get-item $PSScriptRoot ).parent.FullName
git pull

Set-Location $PSScriptRoot

$filePath = ".\uselessFile.txt"

$status = (git status)
if ($status -contains "nothing to commit, working tree clean"){
    Write-Output "No changes in the repo. Creating mock modification."
    Add-Content $filePath ("Line N. " + ([int]((Get-Item -Path $filePath | Get-Content -Tail 1) -replace '[^0-9]' , '') + 1))
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