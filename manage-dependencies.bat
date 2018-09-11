@echo off
for /f "tokens=*" %%a in (dependencies) do (
   pip install --force-reinstall %%a
)
