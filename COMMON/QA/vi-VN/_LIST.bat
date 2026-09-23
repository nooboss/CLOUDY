@echo off
(for %%f in (*) do (
    if /i not "%%~nxf"=="%~nx0" if /i not "%%~nxf"=="result.txt" echo %%f
)) > result.txt