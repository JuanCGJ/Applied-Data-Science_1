# import numpy as np
# import re
# import pandas as pd
#
# def answer_one():
#     Energy= pd.read_excel("Energy Indicators.xls", sheet_name = "Energy")
#     Energy=Energy.drop(Energy.columns[[0, 1]], axis='columns')  #elimino columnas por su indice 0 y 1.
#     Energy=Energy.drop(range(0,17,1), axis=0)                   #eliino rango de filas 0 a 17 (header)
#     Energy=Energy.drop(range(244,282,1), axis=0)                #eliino rango de filas 244 a 282 (footer)
#     Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'] # Renombro columnas
#     listaener=[]
#     for k in Energy.columns:
#         str(k).strip()
#         listaener.append(k)
#     Energy.set_axis(listaener, axis=1, inplace=True)
#     Energy[Energy == '...'] = np.nan                            #relleno con NaN donde haya puntos (...)
#     Energy['Country'].replace('[\d*]','', regex=True, inplace=True)  #reemplazar con vacio '' donde cadena de numeros
#     Energy['Country'].replace('\(.*\)','', regex=True, inplace=True) #reemplazar con vacio '' donde cadena de numeros ()
#     Energy['Country']=Energy['Country'].str.rstrip()            #elimino espacios que sobran al fin de la cadena
#     Energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States',
#     'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
#     'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True) #reemplazo nombres
#     Energy['Energy Supply']=Energy['Energy Supply']*1000000     #paso de peta a giga joules
#     Energy=Energy.set_index('Country')
#     # print(Energy)
#     # print(len(Energy)) #227
#
#     GDP= pd.read_csv('world_bank.csv', header=None, skiprows=4) #elimino header y las 4 priemras filas
#     GDP[0]=GDP[0].str.strip()                                   #remuevo espacios de la columna 0
#     axislist=[]
#     for x in GDP.iloc[0]:                                       #creo lista con los nombres de las cabeceras
#         axislist.append(x)
#     for k in range (4,len(axislist),1):
#         axislist[k]=str(int(axislist[k]))
#     GDP.drop([0],axis=0,inplace=True)                           #elimino la fila 0
#     GDP.set_axis(axislist, axis=1, inplace=True)                #coloco lista como nuevo axis
#     GDP.rename(columns={'Country Name':'Country'}, inplace=True)#cambio nombre de cabecera
#     GDP['Country'].replace({"Korea, Rep." : "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
#     GDP=GDP.set_index('Country')
#     # print(GDP)
#     # print(len(GDP)) #264
#
#     ScimEn= pd.read_excel("scimagojr-3.xlsx", sheet_name = "Sheet1")
#     ScimEn=ScimEn.set_index('Country')
#     # print(ScimEn)
#     # print(len(ScimEn)) #191
#
#     mergedf=pd.merge(ScimEn, Energy, how='outer', left_index=True, right_index=True)  #uno GDP Y Energy dataframes en un solo dataf: mergedf
#     df=pd.merge(mergedf, GDP, how='outer', left_index=True, right_index=True)   #uno mergedf con Scim dataframe= todos dataframes en una sola= df
#     df=df.drop(df.columns[10:59], axis='columns') #elimino columnas que no necesito
#     df.sort_values(by=['Rank'], inplace=True)
#     df=df.iloc[0:15]
#     lista=[]
#     for x in df.columns:
#         str(x).strip()
#         lista.append(x)
#     df.set_axis(lista, axis=1, inplace=True)
#     answer_one=df                          #filtrada por los primeros 15 valores = (15 valores de rank)
#     #print(type(answer_one))
#     #print(answer_one.shape)
#     print(answer_one)
#     return(answer_one)
# answer_one()

# PARTE B
# import numpy as np
# import re
# import pandas as pd
# def answer_two():
#     Energy= pd.read_excel("Energy Indicators.xls", sheet_name = "Energy")
#     Energy=Energy.drop(Energy.columns[[0, 1]], axis='columns')  #elimino columnas por su indice 0 y 1.
#     Energy=Energy.drop(range(0,17,1), axis=0)                   #eliino rango de filas 0 a 17 (header)
#     Energy=Energy.drop(range(244,282,1), axis=0)                #eliino rango de filas 244 a 282 (footer)
#     Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'] # Renombro columnas
#     listaener=[]
#     for k in Energy.columns:
#         str(k).strip()
#         listaener.append(k)
#     Energy.set_axis(listaener, axis=1, inplace=True)
#     Energy[Energy == '...'] = np.nan                            #relleno con NaN donde haya puntos (...)
#     Energy['Country'].replace('[\d*]','', regex=True, inplace=True)  #reemplazar con vacio '' donde cadena de numeros
#     Energy['Country'].replace('\(.*\)','', regex=True, inplace=True) #reemplazar con vacio '' donde cadena de numeros ()
#     Energy['Country']=Energy['Country'].str.rstrip()            #elimino espacios que sobran al fin de la cadena
#     Energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States',
#     'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
#     'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True) #reemplazo nombres
#     Energy['Energy Supply']=Energy['Energy Supply']*1000000     #paso de peta a giga joules
#     Energy=Energy.set_index('Country')
#     # for x in Energy.index:
#     #     print(x)
#     # print(Energy)
#     # print(len(Energy)) #227
#
#     GDP= pd.read_csv('world_bank.csv', header=None, skiprows=4) #elimino header y las 4 priemras filas
#     GDP[0]=GDP[0].str.strip()                                   #remuevo espacios de la columna 0
#     axislist=[]
#     for x in GDP.iloc[0]:                                       #creo lista con los nombres de las cabeceras
#         axislist.append(x)
#     for k in range (4,len(axislist),1):
#         axislist[k]=str(int(axislist[k]))
#     GDP.drop([0],axis=0,inplace=True)                           #elimino la fila 0
#     GDP.set_axis(axislist, axis=1, inplace=True)                #coloco lista como nuevo axis
#     GDP.rename(columns={'Country Name':'Country'}, inplace=True)#cambio nombre de cabecera
#     GDP['Country'].replace({"Korea, Rep." : "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
#     GDP=GDP.set_index('Country')
#
#     # print(GDP)
#     # print(len(GDP)) #264
#
#     ScimEn= pd.read_excel("scimagojr-3.xlsx", sheet_name = "Sheet1")
#     ScimEn['Country']=ScimEn['Country'].str.rstrip()
#     ScimEn=ScimEn.set_index('Country')
#     print(ScimEn)
#     # print(len(ScimEn)) #191
#
#     mergedf=pd.merge(ScimEn, Energy, how='outer', left_index=True, right_index=True)  #uno GDP Y Energy dataframes en un solo dataf: mergedf
#     df=pd.merge(mergedf, GDP, how='outer', left_index=True, right_index=True)   #uno mergedf con Scim dataframe= todos dataframes en una sola= df
#
#     outervalues=len(df) #318
#     print('Outervalues length: ', outervalues)
#     # print(df)
#
#     mergedf1=pd.merge(ScimEn, Energy, on="Country")  #uno GDP Y Energy dataframes en un solo dataf: mergedf
#     df1=pd.merge(mergedf1, GDP, on="Country")   #uno mergedf con Scim dataframe= todos dataframe
#     innervalues=len(df1) #162
#     print('innervalues length: ',innervalues)
#
#     answer_two=outervalues-innervalues #156
#     print('lost Values: ', answer_two)
#     return(answer_two)
# answer_two()

# PARTE C
# import numpy as np
# import re
# import pandas as pd
# def answer_three():
#     Energy= pd.read_excel("Energy Indicators.xls", sheet_name = "Energy")
#     Energy=Energy.drop(Energy.columns[[0, 1]], axis='columns')  #elimino columnas por su indice 0 y 1.
#     Energy=Energy.drop(range(0,17,1), axis=0)                   #eliino rango de filas 0 a 17 (header)
#     Energy=Energy.drop(range(244,282,1), axis=0)                #eliino rango de filas 244 a 282 (footer)
#     Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'] # Renombro columnas
#     listaener=[]
#     for k in Energy.columns:
#         str(k).strip()
#         listaener.append(k)
#     Energy.set_axis(listaener, axis=1, inplace=True)
#     Energy[Energy == '...'] = np.nan                            #relleno con NaN donde haya puntos (...)
#     Energy['Country'].replace('[\d*]','', regex=True, inplace=True)  #reemplazar con vacio '' donde cadena de numeros
#     Energy['Country'].replace('\(.*\)','', regex=True, inplace=True) #reemplazar con vacio '' donde cadena de numeros ()
#     Energy['Country']=Energy['Country'].str.rstrip()            #elimino espacios que sobran al fin de la cadena
#     Energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States',
#     'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
#     'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True) #reemplazo nombres
#     Energy['Energy Supply']=Energy['Energy Supply']*1000000     #paso de peta a giga joules
#     Energy=Energy.set_index('Country')
#     # print(Energy)
#     # print(len(Energy)) #227
#
#     GDP= pd.read_csv('world_bank.csv', header=None, skiprows=4) #elimino header y las 4 priemras filas
#     GDP[0]=GDP[0].str.strip()                                   #remuevo espacios de la columna 0
#     axislist=[]
#     for x in GDP.iloc[0]:                                       #creo lista con los nombres de las cabeceras
#         axislist.append(x)
#     for k in range (4,len(axislist),1):
#         axislist[k]=str(int(axislist[k]))
#     GDP.drop([0],axis=0,inplace=True)                           #elimino la fila 0
#     GDP.set_axis(axislist, axis=1, inplace=True)                #coloco lista como nuevo axis
#     GDP.rename(columns={'Country Name':'Country'}, inplace=True)#cambio nombre de cabecera
#     GDP['Country'].replace({"Korea, Rep." : "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
#     GDP=GDP.set_index('Country')
#     # print(GDP)
#     # print(len(GDP)) #264
#
#     ScimEn= pd.read_excel("scimagojr-3.xlsx", sheet_name = "Sheet1")
#     ScimEn=ScimEn.set_index('Country')
#     # print(ScimEn)
#     # print(len(ScimEn)) #191
#
#     mergedf=pd.merge(ScimEn, Energy, how='outer', left_index=True, right_index=True)  #uno GDP Y Energy dataframes en un solo dataf: mergedf
#     df=pd.merge(mergedf, GDP, how='outer', left_index=True, right_index=True)   #uno mergedf con Scim dataframe= todos dataframes en una sola= df
#     df=df.drop(df.columns[10:59], axis='columns') #elimino columnas que no necesito
#     df.sort_values(by=['Rank'], inplace=True)
#     df=df.iloc[0:15]
#
#     lista=[]
#     for x in df.columns:                       #quita espacios de las columnas
#         str(x).strip()
#         lista.append(x)
#     df.set_axis(lista, axis=1, inplace=True)  #reestablece los nuevos nombres de columnas
#
#     df['avgGDP']=df.iloc[:,10:].mean(axis=1)
#     df=df['avgGDP'][0:15]
#     df.sort_values(ascending=False, inplace=True)
#
#     answer_three=df   #filtrada por los primeros 15 valores = (15 valores de rank)
#
#     print(answer_three)
#     print(type(answer_three))
#
#     return(answer_three)
# answer_three()

#PARTE D
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# This function should return a single number.
# import numpy as np
# import re
# import pandas as pd
# def answer_four():
#     Energy= pd.read_excel("Energy Indicators.xls", sheet_name = "Energy")
#     Energy=Energy.drop(Energy.columns[[0, 1]], axis='columns')  #elimino columnas por su indice 0 y 1.
#     Energy=Energy.drop(range(0,17,1), axis=0)                   #eliino rango de filas 0 a 17 (header)
#     Energy=Energy.drop(range(244,282,1), axis=0)                #eliino rango de filas 244 a 282 (footer)
#     Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'] # Renombro columnas
#     listaener=[]
#     for k in Energy.columns:
#         str(k).strip()
#         listaener.append(k)
#     Energy.set_axis(listaener, axis=1, inplace=True)
#     Energy[Energy == '...'] = np.nan                            #relleno con NaN donde haya puntos (...)
#     Energy['Country'].replace('[\d*]','', regex=True, inplace=True)  #reemplazar con vacio '' donde cadena de numeros
#     Energy['Country'].replace('\(.*\)','', regex=True, inplace=True) #reemplazar con vacio '' donde cadena de numeros ()
#     Energy['Country']=Energy['Country'].str.rstrip()            #elimino espacios que sobran al fin de la cadena
#     Energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States',
#     'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
#     'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True) #reemplazo nombres
#     Energy['Energy Supply']=Energy['Energy Supply']*1000000     #paso de peta a giga joules
#     Energy=Energy.set_index('Country')
#     # print(Energy)
#     # print(len(Energy)) #227
#
#     GDP= pd.read_csv('world_bank.csv', header=None, skiprows=4) #elimino header y las 4 priemras filas
#     GDP[0]=GDP[0].str.strip()                                   #remuevo espacios de la columna 0
#     axislist=[]
#     for x in GDP.iloc[0]:                                       #creo lista con los nombres de las cabeceras
#         axislist.append(x)
#     for k in range (4,len(axislist),1):
#         axislist[k]=str(int(axislist[k]))
#     GDP.drop([0],axis=0,inplace=True)                           #elimino la fila 0
#     GDP.set_axis(axislist, axis=1, inplace=True)                #coloco lista como nuevo axis
#     GDP.rename(columns={'Country Name':'Country'}, inplace=True)#cambio nombre de cabecera
#     GDP['Country'].replace({"Korea, Rep." : "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
#     GDP=GDP.set_index('Country')
#     # print(GDP)
#     # print(len(GDP)) #264
#
#     ScimEn= pd.read_excel("scimagojr-3.xlsx", sheet_name = "Sheet1")
#     ScimEn=ScimEn.set_index('Country')
#     # print(ScimEn)
#     # print(len(ScimEn)) #191
#
#     mergedf=pd.merge(ScimEn, Energy, how='outer', left_index=True, right_index=True)  #uno GDP Y Energy dataframes en un solo dataf: mergedf
#     df=pd.merge(mergedf, GDP, how='outer', left_index=True, right_index=True)   #uno mergedf con Scim dataframe= todos dataframes en una sola= df
#     df=df.drop(df.columns[10:59], axis='columns') #elimino columnas que no necesito
#     df.sort_values(by=['Rank'], inplace=True)
#     df=df.iloc[0:15]
#
#     lista=[]
#     for x in df.columns:                       #quita espacios de las columnas
#         str(x).strip()
#         lista.append(x)
#     df.set_axis(lista, axis=1, inplace=True)  #reestablece los nuevos nombres de columnas
#     df['avgGDP']=df.iloc[:,10:].mean(axis=1)
#     #df.sort_values(ascending=False, inplace=True) descending average GDP Countries
#     # print(df)
#     answer_four=df.iloc[3,19] - df.iloc[3,10] ##6th largest average GDP:unitedkindome:2015 - 2006 =
#     print(answer_four)
#     print(type(answer_four))
#
#     return(answer_four)
# answer_four()

#PARTE E
# What is the mean energy supply per capita?
# This function should return a single number.

# import numpy as np
# import re
# import pandas as pd
# def answer_five():
#     Energy= pd.read_excel("Energy Indicators.xls", sheet_name = "Energy")
#     Energy=Energy.drop(Energy.columns[[0, 1]], axis='columns')  #elimino columnas por su indice 0 y 1.
#     Energy=Energy.drop(range(0,17,1), axis=0)                   #eliino rango de filas 0 a 17 (header)
#     Energy=Energy.drop(range(244,282,1), axis=0)                #eliino rango de filas 244 a 282 (footer)
#     Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'] # Renombro columnas
#     listaener=[]
#     for k in Energy.columns:
#         str(k).strip()
#         listaener.append(k)
#     Energy.set_axis(listaener, axis=1, inplace=True)
#     Energy[Energy == '...'] = np.nan                            #relleno con NaN donde haya puntos (...)
#     Energy['Country'].replace('[\d*]','', regex=True, inplace=True)  #reemplazar con vacio '' donde cadena de numeros
#     Energy['Country'].replace('\(.*\)','', regex=True, inplace=True) #reemplazar con vacio '' donde cadena de numeros ()
#     Energy['Country']=Energy['Country'].str.rstrip()            #elimino espacios que sobran al fin de la cadena
#     Energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States',
#     'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
#     'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True) #reemplazo nombres
#     Energy['Energy Supply']=Energy['Energy Supply']*1000000     #paso de peta a giga joules
#     Energy=Energy.set_index('Country')
#     # print(Energy)
#     # print(len(Energy)) #227
#
#     GDP= pd.read_csv('world_bank.csv', header=None, skiprows=4) #elimino header y las 4 priemras filas
#     GDP[0]=GDP[0].str.strip()                                   #remuevo espacios de la columna 0
#     axislist=[]
#     for x in GDP.iloc[0]:                                       #creo lista con los nombres de las cabeceras
#         axislist.append(x)
#     for k in range (4,len(axislist),1):
#         axislist[k]=str(int(axislist[k]))
#     GDP.drop([0],axis=0,inplace=True)                           #elimino la fila 0
#     GDP.set_axis(axislist, axis=1, inplace=True)                #coloco lista como nuevo axis
#     GDP.rename(columns={'Country Name':'Country'}, inplace=True)#cambio nombre de cabecera
#     GDP['Country'].replace({"Korea, Rep." : "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
#     GDP=GDP.set_index('Country')
#     # print(GDP)
#     # print(len(GDP)) #264
#
#     ScimEn= pd.read_excel("scimagojr-3.xlsx", sheet_name = "Sheet1")
#     ScimEn=ScimEn.set_index('Country')
#     # print(ScimEn)
#     # print(len(ScimEn)) #191
#
#     mergedf=pd.merge(ScimEn, Energy, how='outer', left_index=True, right_index=True)  #uno GDP Y Energy dataframes en un solo dataf: mergedf
#     df=pd.merge(mergedf, GDP, how='outer', left_index=True, right_index=True)   #uno mergedf con Scim dataframe= todos dataframes en una sola= df
#     df=df.drop(df.columns[10:59], axis='columns') #elimino columnas que no necesito
#     df.sort_values(by=['Rank'], inplace=True)
#     df=df.iloc[0:15]
#
#     lista=[]
#     for x in df.columns:                       #quita espacios de las columnas
#         str(x).strip()
#         lista.append(x)
#     df.set_axis(lista, axis=1, inplace=True)  #reestablece los nuevos nombres de columnas
#     answer_five=df['Energy Supply per Capita'].mean() #157.6
#     print(answer_five)
#     print(type(answer_five))
#     return(answer_five)
# answer_five()

# PARTE F
# What country has the maximum % Renewable and what is the percentage?
# This function should return a tuple with the name of the country and the percentage.
# import numpy as np
# import re
# import pandas as pd
# def answer_six():
#     Energy= pd.read_excel("Energy Indicators.xls", sheet_name = "Energy")
#     Energy=Energy.drop(Energy.columns[[0, 1]], axis='columns')  #elimino columnas por su indice 0 y 1.
#     Energy=Energy.drop(range(0,17,1), axis=0)                   #eliino rango de filas 0 a 17 (header)
#     Energy=Energy.drop(range(244,282,1), axis=0)                #eliino rango de filas 244 a 282 (footer)
#     Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'] # Renombro columnas
#     listaener=[]
#     for k in Energy.columns:
#         str(k).strip()
#         listaener.append(k)
#     Energy.set_axis(listaener, axis=1, inplace=True)
#     Energy[Energy == '...'] = np.nan                            #relleno con NaN donde haya puntos (...)
#     Energy['Country'].replace('[\d*]','', regex=True, inplace=True)  #reemplazar con vacio '' donde cadena de numeros
#     Energy['Country'].replace('\(.*\)','', regex=True, inplace=True) #reemplazar con vacio '' donde cadena de numeros ()
#     Energy['Country']=Energy['Country'].str.rstrip()            #elimino espacios que sobran al fin de la cadena
#     Energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States',
#     'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
#     'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True) #reemplazo nombres
#     Energy['Energy Supply']=Energy['Energy Supply']*1000000     #paso de peta a giga joules
#     Energy=Energy.set_index('Country')
#     # print(Energy)
#     # print(len(Energy)) #227
#
#     GDP= pd.read_csv('world_bank.csv', header=None, skiprows=4) #elimino header y las 4 priemras filas
#     GDP[0]=GDP[0].str.strip()                                   #remuevo espacios de la columna 0
#     axislist=[]
#     for x in GDP.iloc[0]:                                       #creo lista con los nombres de las cabeceras
#         axislist.append(x)
#     for k in range (4,len(axislist),1):
#         axislist[k]=str(int(axislist[k]))
#     GDP.drop([0],axis=0,inplace=True)                           #elimino la fila 0
#     GDP.set_axis(axislist, axis=1, inplace=True)                #coloco lista como nuevo axis
#     GDP.rename(columns={'Country Name':'Country'}, inplace=True)#cambio nombre de cabecera
#     GDP['Country'].replace({"Korea, Rep." : "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
#     GDP=GDP.set_index('Country')
#     # print(GDP)
#     # print(len(GDP)) #264
#
#     ScimEn= pd.read_excel("scimagojr-3.xlsx", sheet_name = "Sheet1")
#     ScimEn=ScimEn.set_index('Country')
#     # print(ScimEn)
#     # print(len(ScimEn)) #191
#
#     mergedf=pd.merge(ScimEn, Energy, how='outer', left_index=True, right_index=True)  #uno GDP Y Energy dataframes en un solo dataf: mergedf
#     df=pd.merge(mergedf, GDP, how='outer', left_index=True, right_index=True)   #uno mergedf con Scim dataframe= todos dataframes en una sola= df
#     df=df.drop(df.columns[10:59], axis='columns') #elimino columnas que no necesito
#     df.sort_values(by=['Rank'], inplace=True)
#     df=df.iloc[0:15]
#
#     lista=[]
#     for x in df.columns:                       #quita espacios de las columnas
#         str(x).strip()
#         lista.append(x)
#     df.set_axis(lista, axis=1, inplace=True)  #reestablece los nuevos nombres de columnas
#
#     # df=df['% Renewable']
#     # print(df)
#     index_max_valor=df.index[df['% Renewable']==df['% Renewable'].max()].tolist() #entrega lista con index que cumpple la condicion
#     index_max_valor=index_max_valor[0] #saco el valor de la lista
#     valor=df.loc['Brazil']['% Renewable'] #encuentro el valor de Brazil # 69.64803
#     answer_six=(index_max_valor, valor)  #armo tupla
#     print(answer_six)
#
#     return(answer_six)
# answer_six()

#PARTE G
# Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value
# for this new column, and what country has the highest ratio? This function
# should return a tuple with the name of the country and the ratio.
import numpy as np
import re
import pandas as pd
def answer_seven():
    Energy= pd.read_excel("Energy Indicators.xls", sheet_name = "Energy")
    Energy=Energy.drop(Energy.columns[[0, 1]], axis='columns')  #elimino columnas por su indice 0 y 1.
    Energy=Energy.drop(range(0,17,1), axis=0)                   #eliino rango de filas 0 a 17 (header)
    Energy=Energy.drop(range(244,282,1), axis=0)                #eliino rango de filas 244 a 282 (footer)
    Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'] # Renombro columnas
    listaener=[]
    for k in Energy.columns:
        str(k).strip()
        listaener.append(k)
    Energy.set_axis(listaener, axis=1, inplace=True)
    Energy[Energy == '...'] = np.nan                            #relleno con NaN donde haya puntos (...)
    Energy['Country'].replace('[\d*]','', regex=True, inplace=True)  #reemplazar con vacio '' donde cadena de numeros
    Energy['Country'].replace('\(.*\)','', regex=True, inplace=True) #reemplazar con vacio '' donde cadena de numeros ()
    Energy['Country']=Energy['Country'].str.rstrip()            #elimino espacios que sobran al fin de la cadena
    Energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States',
    'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
    'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True) #reemplazo nombres
    Energy['Energy Supply']=Energy['Energy Supply']*1000000     #paso de peta a giga joules
    Energy=Energy.set_index('Country')
    # print(Energy)
    # print(len(Energy)) #227

    GDP= pd.read_csv('world_bank.csv', header=None, skiprows=4) #elimino header y las 4 priemras filas
    GDP[0]=GDP[0].str.strip()                                   #remuevo espacios de la columna 0
    axislist=[]
    for x in GDP.iloc[0]:                                       #creo lista con los nombres de las cabeceras
        axislist.append(x)
    for k in range (4,len(axislist),1):
        axislist[k]=str(int(axislist[k]))
    GDP.drop([0],axis=0,inplace=True)                           #elimino la fila 0
    GDP.set_axis(axislist, axis=1, inplace=True)                #coloco lista como nuevo axis
    GDP.rename(columns={'Country Name':'Country'}, inplace=True)#cambio nombre de cabecera
    GDP['Country'].replace({"Korea, Rep." : "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
    GDP=GDP.set_index('Country')
    # print(GDP)
    # print(len(GDP)) #264

    ScimEn= pd.read_excel("scimagojr-3.xlsx", sheet_name = "Sheet1")
    ScimEn=ScimEn.set_index('Country')
    # print(ScimEn)
    # print(len(ScimEn)) #191

    mergedf=pd.merge(ScimEn, Energy, how='outer', left_index=True, right_index=True)  #uno GDP Y Energy dataframes en un solo dataf: mergedf
    df=pd.merge(mergedf, GDP, how='outer', left_index=True, right_index=True)   #uno mergedf con Scim dataframe= todos dataframes en una sola= df
    df=df.drop(df.columns[10:59], axis='columns') #elimino columnas que no necesito
    df.sort_values(by=['Rank'], inplace=True)
    df=df.iloc[0:15]

    lista=[]
    for x in df.columns:                       #quita espacios de las columnas
        str(x).strip()
        lista.append(x)
    df.set_axis(lista, axis=1, inplace=True)  #reestablece los nuevos nombres de columnas

    print(df)
    print(df.columns)
    print(df['Self-citations'])
    sumselfcitations=df['Self-citations'].sum()
    print(sumselfcitations)
    df['Ratio_self-citations']=df['Self-citations']/sumselfcitations
    print(df)

    index_max_valor=df.index[df['Self-citations']==df['Self-citations'].max()].tolist() #entrega lista con index que cumpple la condicion
    index_max_valor=index_max_valor[0] #saco el valor de la lista
    valor=df.loc['China']['Ratio_self-citations'] #encuentro el valor de Brazil # 69.64803
    print(valor)
    answer_seven=(index_max_valor, valor)  #armo tupla
    print(answer_seven)
    # print(type(answer_seven))

    return(answer_seven)
answer_seven()
