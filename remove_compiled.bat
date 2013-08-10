cd src
for /r %%i in (*) do (if %%~xi==.pyc (del %%i) )


cd src
for /f "tokens=* delims=" %%i in ('dir /s /b /a:d *__pycache__*') do (
    rd /s /q "%%i"
)
