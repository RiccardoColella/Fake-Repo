$shell = New-Object -ComObject WScript.Shell

"Working..."
"Press CTRL + C to stop"

while ($true)
{
  $shell.SendKeys('^')
  $shell.SendKeys('^')
  Start-Sleep -seconds 55
}