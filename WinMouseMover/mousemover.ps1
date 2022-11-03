Add-Type -AssemblyName System.Windows.Forms

$backOrForth = $true

while ($true)
{
  $pos = [System.Windows.Forms.Cursor]::Position
  $delta = If ($backOrForth) {1} Else {-1}
  [System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point(($pos.X + $delta), ($pos.Y + $delta))
  $backOrForth = -Not $backOrForth
  Start-Sleep -Milliseconds 200
}