python C:\bat\python-scripts\goto-path.py %1% > temp.txt
set /p way=<temp.txt
del temp.txt
cd %way%
cls
