import os

location = "F:/User/Documents/CERTUS/Proyecto_Parcial/python/dataset"

# validad que la carpeta exista
if not os.path.exists(location):
    os.mkdir(location)
else:
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) #elimino todo los archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name))  #rmdir -> remove directory /#elimino todas mis carpetas

from kaggle.api.kaggle_api_extended import KaggleApi
##Para auntenticacion correcta no olvidar depositar archivo kaggle.json
## en la ruta C:\Windows\System32\config\systemprofile
api= KaggleApi()

api.authenticate()

#print(api.dataset_list(search='henryshan'))

api.dataset_download_file('henryshan/starbucks', 'starbucks.csv', path=location, quiet=False)
