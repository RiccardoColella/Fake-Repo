$shell = New-Object -ComObject WScript.Shell

while ($true)
{
  $shell.SendKeys('+{F15}')
  Start-Sleep -seconds 59
}