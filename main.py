from fastapi import FastAPI, HTTPException
import pandas as pd



#Instancio mi aplicacion con la clase FastAPI
app = FastAPI(title='Proyecto Individual 1',
            description='Proyecto de Data Engineering con la finalidad de crear una api con FastAPI y containerizarla con Docker :)', version='2.0.0.0')

#Cargo mi dataset con el que se haran las consultas
df = pd.read_csv('./Datasets/combined_platforms.csv')
plataformas = ['amazon', 'netflix', 'hulu', 'disney']

#estas listas servirán para validar los argumentos en las queries
plataformas = ['amazon', 'hulu', 'disney', 'netflix']
tipos = ['min', 'season']

#diccionario de bienvenida
queries = {'get_max_duration':'/anio/plataforma/tipo',
            'get_count_platform':'/plataforma',
            'get_listedin':'/genero',
            'get_actor':'/plataforma/anio'}

@app.get('/')
def welcome():
    return f'Bienvenido, las queries admitidas son: {queries}'

#primera consigna
@app.get('/get_max_duration/{anio}/{plataforma}/{tipo}')
def get_max_duration(anio: int, plataforma: str, tipo: str):
    if (type(anio) == int and anio in range(1000, 2023)) and type(plataforma) == str and plataforma.lower() in plataformas and type(tipo) == str and tipo.lower() in tipos:
        if tipo.lower()=='min':
            return {'titulo': df.loc[df[(df['platform']==plataforma.lower())][df['type']=='Movie'][df['release_year']==anio]['duration_time'].idxmax()]['title']}
        elif tipo.lower() == 'season':
            return {'titulo': df.loc[df[(df['platform']==plataforma.lower())][df['type']=='TV Show'][df['release_year']==anio]['duration_time'].idxmax()]['title']}
    else:
        raise HTTPException(404, detail='LOS DATOS INGRESADOS NO SON VALIDOS')

#segunda consigna
@app.get('/get_count_platform/{plataforma}')
def get_count_platform(plataforma: str):
    if type(plataforma) == str and plataforma.lower() in plataformas:
        # esta query devuelve una serie por lo que se trasforma primero a un dataframe y luego a un diccionario
        consulta = df[df['platform'] == plataforma.lower()]['type'].value_counts().to_frame().to_dict()
        resultado = {}
        for i, j in consulta.items(): #iteramos sobre el nuevo diccionario para obtener los valores
            resultado.update(j)
    else:
        raise HTTPException(404, detail=f'La plataforma que puedes utilizar es: {plataformas}')

    return resultado

#tercera consigna
@app.get('/get_listedin/{genero}')
def get_listedin(genero:str):
    if type(genero)==str:
        return 'Lo siento, ya no me dio tiempo para esta query.'
    else:
        raise HTTPException(404, detail='Dato no valido.')


#cuarta consigna
@app.get('/get_actor/{platfom}/{year}')
def get_actor(platform:str, year:int):
    if (type(year) == int and year in range(1000, 2023)) and type(platform) == str and platform.lower() in plataformas:
        return 'Lo siento, ya no me dio tiempo para esta query.'
    else:
        raise HTTPException(404, detail='Dato no valido')