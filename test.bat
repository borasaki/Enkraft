@ECHO OFF
SET "PScommand="POWERSHELL Add-Type -AssemblyName System.Windows.Forms; $FileBrowser = New-Object System.Windows.Forms.OpenFileDialog -Property @{ValidateNames = $false;FileName='';}; $FileBrowser.ShowDialog(); $File = $FileBrowser.Filename; Write-Output $File;""

FOR /F "Skip=1 usebackq tokens=*" %%Q in (`%PScommand%`) DO (
    ECHO %%Q
    del "config.txt"
    ECHO %%Q>> config.txt
)