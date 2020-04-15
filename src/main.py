from hack import *
import requests
import json
from Constantes import *


processo = "zsnesw.exe"

hackMario = hack(processo)


r = requests.get(URL, params = PARAMETROS, stream=True)
for raw in r.iter_lines():
    if raw:
        jsonDecodificado = raw.decode("utf-8")
        print(jsonDecodificado)
        tamanhoJson = len(jsonDecodificado)
        if tamanhoJson > 6:
            comentario = json.loads(jsonDecodificado[6:tamanhoJson])
            if comentario['message'] in listaComandos:
                print(comentario)
                statusInject = int(dicionarioComandos.get(comentario['message']))
                print (statusInject)
                hackMario.injetarStatusMario(statusInject)



