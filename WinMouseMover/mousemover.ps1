clear

$shell = New-Object -ComObject WScript.Shell

while ($true)
{
  "Moving..."
  $shell.SendKeys('+{F15}')
  Start-Sleep -seconds 59
}