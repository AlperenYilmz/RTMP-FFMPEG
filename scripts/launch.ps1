$host.ui.RawUI.WindowTitle = "RTMP System Launcher"

Start-Process cmd.exe -WorkingDirectory "..\overlay\" -ArgumentList "/k python ..\overlay\overlay.py" -NoNewWindow

Write-Host "debug line 1: Overlay script works fine "
$is_found = $false

while (!$is_found)
{
    Write-Host "debug line 2: directory search loop"
    if (Test-Path "..\overlay\overlay.png")
    {
        Write-Host "Overlay image found!"
        $is_found = $true
    }
    Start-Sleep -Seconds 2
}

Write-Host "debug line 3: image found"
Start-Process cmd.exe -ArgumentList "/k publish.bat" -NoNewWindow