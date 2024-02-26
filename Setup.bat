@echo Creating directory for Lasi Commands...
if not exist LasiFunctions mkdir LasiFunctions
cd LasiFunctions
if not exist ActionFunctions mkdir ActionFunctions
if not exist BooleanFunctions mkdir BooleanFunctions
if not exist ForActionFunctions mkdir ForActionFunctions
if not exist ForBooleanFunctions mkdir ForBooleanFunctions
cd ..
@echo Done.

echo Creating directory for script outputs...
if not exist Output mkdir Output
echo Done.

@echo Generating Lasi Commands...
python3 ./GenerateLasiCommands.py
@echo Done.