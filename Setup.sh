echo Creating directory for Lasi Commands...
mkdir LasiFunctions
cd LasiFunctions
mkdir ActionFunctions
mkdir BooleanFunctions
mkdir ForActionFunctions
mkdir ForBooleanFunctions
cd ..
echo Done.

echo Creating directory for script outputs...
mkdir Output
echo Done.

echo Generating Lasi Commands...
python3 ./GenerateLasiCommands.py
echo Done.