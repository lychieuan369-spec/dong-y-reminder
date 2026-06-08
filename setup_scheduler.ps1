# setup_scheduler.ps1 — ASCII only, no special chars
$pythonExe      = "C:\Program Files\Python314\python.exe"
$workDir        = "D:\dong_y_reminder"
$reminderScript = "$workDir\reminder.py"
$gradeScript    = "$workDir\grade_quiz.py"

Write-Host "Python: $pythonExe"
Write-Host "Dir   : $workDir"

function Register-DongYTask {
    param([string]$TaskName, [string]$ScriptFile, [string]$TriggerTime)

    $action   = New-ScheduledTaskAction -Execute $pythonExe -Argument $ScriptFile -WorkingDirectory $workDir
    $trigger  = New-ScheduledTaskTrigger -Daily -At $TriggerTime
    $settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 5) -StartWhenAvailable -RunOnlyIfNetworkAvailable
    $principal= New-ScheduledTaskPrincipal -UserId "ADMIN" -RunLevel Highest -LogonType Interactive

    if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
        Write-Host "Removed old: $TaskName"
    }

    Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force | Out-Null
    Write-Host "Created: $TaskName at $TriggerTime"
}

Register-DongYTask -TaskName "DongY-Morning-Reminder" -ScriptFile $reminderScript -TriggerTime "07:00"
Register-DongYTask -TaskName "DongY-Evening-Reminder" -ScriptFile $reminderScript -TriggerTime "21:00"
Register-DongYTask -TaskName "DongY-Grade-Quiz"        -ScriptFile $gradeScript    -TriggerTime "21:30"

Write-Host "Done. Verify: Get-ScheduledTask -TaskName DongY-*"
