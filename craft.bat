@ECHO OFF

SET "PScommand="POWERSHELL Add-Type -AssemblyName System.Windows.Forms; $FileBrowser = New-Object System.Windows.Forms.OpenFileDialog -Property @{ValidateNames = $false;FileName='';}; $FileBrowser.ShowDialog(); $File = $FileBrowser.Filename; Write-Output $File;""

if exist config.txt (
for /f "delims=`" %%a in (config.txt) do (
  echo %%a
  Start "" "%%a"
  exit /b
)
) else (
FOR /F "Skip=1 usebackq tokens=*" %%Q in (`%PScommand%`) DO (
    ECHO %%Q
    del "config.txt"
    ECHO %%Q>> config.txt
)
for /f "delims=`" %%a in (config.txt) do (
  echo %%a
  Start "" "%%a"
  exit /b
)
)