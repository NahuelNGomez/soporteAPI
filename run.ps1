echo "Se instalan dependecias ..."
pip install -r requirements.txt
echo "Se ejecuta la app ... (recordar cerrar la consola minimizada antes de volver a ejecutar)"
#Start-Process uvicorn app:app -NoNewWindow -Wait 
#Start-Job -Command {uvicorn app:app}
Start-Process powershell.exe -ArgumentList "-noexit", "-WindowStyle Minimized", -"command &{uvicorn app:app}"
sleep 10
echo "Se corren las pruebas de bdd:"
behave --color test\features
echo "Se abre FastApi"
#start chrome https://apisoporte.onrender.com/docs
