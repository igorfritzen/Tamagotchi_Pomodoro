@echo off
REM Rode na raiz do projeto, com o venv ativo (pip install pyinstaller antes).
pyinstaller --noconfirm --clean --noconsole --onedir ^
  --name TamagotchiPomodoro ^
  --paths src ^
  --icon assets\icon.ico ^
  --add-data "assets;assets" ^
  run.py
echo.
echo Pronto: dist\TamagotchiPomodoro\TamagotchiPomodoro.exe
