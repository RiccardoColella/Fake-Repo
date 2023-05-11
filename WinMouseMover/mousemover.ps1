$shell = New-Object -ComObject WScript.Shell

"Working..."
"Press CTRL + C to stop"

while ($true)
{
  $shell.SendKeys('+{F15}')
  Start-Sleep -seconds 59
}