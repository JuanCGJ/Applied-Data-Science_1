# def nhl_correlation():
#
#     import pandas as pd
#     import numpy as np
#     import scipy.stats as stats
#     import re
#     import pprint
#
#     cities=pd.read_html("wikipedia_data.html")[1]
#     cities=cities.iloc[:-1,[0,3,5,6,7,8]]                   #cargo las columnas que necesito
#     cities.replace('\[\w.*\]','', regex=True, inplace=True) # reemplazo [] por espacio ''
#     cities.replace('—',0, regex=True, inplace=True)         # reemplazo — por 0 = NaN
#     cities.replace('',0, regex=True, inplace=True)          # reemplazo '' por 0 = NaN
#     cities['NHL']=cities['NHL'].str.strip()                 # retiro espacios
#     cities['NFL']=cities['NFL'].str.strip()
#     cities['MLB']=cities['MLB'].str.strip()

#     copy_NHL=cities[['Metropolitan area','NHL','Population (2016 est.)[8]']].dropna()
#     copy_NHL.sort_values(by=['NHL'], inplace=True)
#     copy_NHL['Population (2016 est.)[8]']=copy_NHL['Population (2016 est.)[8]'].astype('int64')
#
#     population_by_region=copy_NHL['Population (2016 est.)[8]']
#
#
#
#     nhl_df=pd.read_csv("nhl.csv")
#     nhl_df=nhl_df.iloc[:35,[0,2,3,13,14]] #cargo las columnas que necesito
#     nhl_df=nhl_df.drop(nhl_df.index[[0, 9, 18, 26]], axis=0) #elimino filas que no necesito
#     nhl_df['team'].replace("\*",'',inplace=True,regex=True)  # reemplazo * por espacio"
#     nhl_df['team'].replace("[\D].*\s",'',inplace=True,regex=True)
#     nhl_df['team'].replace({'Knights' : 'Golden Knights', 'Jackets': 'Blue Jackets', 'Leafs': 'Maple Leafs', 'Wings': 'Red Wings' }, inplace=True)
#     nhl_df['team']=nhl_df['team'].str.strip()                #retiro espacios
#     nhl_df['W']=nhl_df['W'].astype('int64')                  #convierto columna str a int para poder dividir
#     nhl_df['L']=nhl_df['L'].astype('int64')                  #convierto columna str a int para poder dividir
#     nhl_df['W/L Ratio']=nhl_df['W']/(nhl_df['W']+nhl_df['L'])  #convierto columna str a int
#     nhl_df=nhl_df.drop(nhl_df.columns[[1, 2, 3, 4]], axis=1) #elimino columnas que no necesito
#     nhl_df['team'].replace({'Rangers' : 'RangersIslandersDevils'}, inplace=True)
#     nhl_df.iloc[15,1]=(nhl_df.iloc[15,1]+nhl_df.iloc[14,1]+nhl_df.iloc[12,1])/3     #RangersIslandersDevils promedio de los 3
#     nhl_df=nhl_df.drop(nhl_df.index[[14, 12]], axis=0)                              #elimino filas Islanders y Devils
#     nhl_df['team'].replace({'Kings' : 'KingsDucks'}, inplace=True)
#     nhl_df.iloc[24,1]=(nhl_df.iloc[24,1]+nhl_df.iloc[22,1])/2     #KingsDucks promedio de los 2
#     nhl_df=nhl_df.drop(nhl_df.index[[22]], axis=0)
#     nhl_df.sort_values(by=['team'], inplace=True)
#
#     win_loss_by_region = nhl_df['W/L Ratio']
#
#     corr, pval= stats.pearsonr(population_by_region, win_loss_by_region)
#
#
#     assert len(population_by_region) == len(win_loss_by_region), "Q1: Your lists must be the same length"
#     assert len(population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"
#
#     print(corr)
#     return corr
# nhl_correlation()


# def nba_correlation():
#     import pandas as pd
#     import numpy as np
#     import scipy.stats as stats
#     import re
#
#     cities=pd.read_html("wikipedia_data.html")[1]
#     cities=cities.iloc[:-1,[0,3,5,6,7,8]]
#     cities.replace('\[\w.*\]','', regex=True, inplace=True) # reemplazo [] por espacio ''
#     cities.replace('—',0, regex=True, inplace=True)         # reemplazo — por 0 = NaN
#     cities.replace('',0, regex=True, inplace=True)          # reemplazo '' por 0 = NaN
#     cities['NBA']=cities['NBA'].str.strip()
#     copy_NBA=cities[['Metropolitan area','NBA','Population (2016 est.)[8]']].dropna()
#     copy_NBA.sort_values(by=['NBA'], inplace=True)
#
#     copy_NBA['Population (2016 est.)[8]']=copy_NBA['Population (2016 est.)[8]'].astype('int64')
#
#
#     population_by_region=copy_NBA['Population (2016 est.)[8]']
#
#     nba_df=pd.read_csv("nba.csv")
#     nba_df=nba_df.iloc[:30,[0,3]] #cargo las columnas que necesito
#     # nba_df['W/L%']=nba_df['W/L%'].astype('int64')
#     nba_df.rename(columns={"W/L%": "W/L Ratio"}, inplace=True)
#     nba_df['W/L Ratio']=nba_df['W/L Ratio'].astype('float64')
#     nba_df.replace('\(\d.*\)','', regex=True, inplace=True) # reemplazo () por espacio ''
#     nba_df.replace('\*','', regex=True, inplace=True) # reemplazo () por espacio ''
#     nba_df['team']=nba_df['team'].str.strip()
#     nba_df['team'].replace("[\D].*\s",'',inplace=True,regex=True)
#     nba_df['team'].replace({'Blazers' : 'Trail Blazers', 'Clippers': 'LakersClippers', 'Knicks': 'KnicksNets'}, inplace=True)
#     nba_df.iloc[24,1]=(nba_df.iloc[24,1]+nba_df.iloc[25,1])/2     #KingsDucks promedio de los 2
#     nba_df.iloc[10,1]=(nba_df.iloc[10,1]+nba_df.iloc[11,1])/2     #KingsDucks promedio de los 2
#     nba_df=nba_df.drop(nba_df.index[[11, 25]], axis=0)
#     nba_df.sort_values(by=['team'], inplace=True)
#
#     win_loss_by_region = nba_df['W/L Ratio']
#     corr, pval= stats.pearsonr(population_by_region, win_loss_by_region)
#     print(corr)
#     return corr
#
# nba_correlation()

# def mlb_correlation():
#     import pandas as pd
#     import numpy as np
#     import scipy.stats as stats
#     import re
#
#     cities=pd.read_html("wikipedia_data.html")[1]
#     cities=cities.iloc[:-1,[0,3,5,6,7,8]]
#     cities.replace('\[\w.*\]','', regex=True, inplace=True) # reemplazo [] por espacio ''
#     cities.replace('—',0, regex=True, inplace=True)         # reemplazo — por 0 = NaN
#     cities.replace('',0, regex=True, inplace=True)          # reemplazo '' por 0 = NaN
#     cities['MLB']=cities['MLB'].str.strip()
#     copy_MLB=cities[['Metropolitan area','MLB','Population (2016 est.)[8]']].dropna()
#     copy_MLB.sort_values(by=['MLB'], inplace=True)  #len=26
#     copy_MLB['Population (2016 est.)[8]']=copy_MLB['Population (2016 est.)[8]'].astype('int64')
#
#     print(copy_MLB)
#     population_by_region=copy_MLB['Population (2016 est.)[8]']
#
#
#     mlb_df=pd.read_csv("mlb.csv")
#     mlb_df=mlb_df.iloc[:30,[0,1,2]] #cargo las columnas que necesito
#
#     mlb_df['W']=mlb_df['W'].astype('int64')                  #convierto columna str a int para poder dividir
#     mlb_df['L']=mlb_df['L'].astype('int64')                  #convierto columna str a int para poder dividir
#     mlb_df['W/L Ratio']=mlb_df['W']/(mlb_df['W']+mlb_df['L'])  #convierto columna str a int
#
#
#     mlb_df['team'].replace("[\D].*\s",'',inplace=True,regex=True)
#     mlb_df['team']=mlb_df['team'].str.strip()
#     mlb_df.iloc[0,0]='Red Sox'
#     mlb_df.iloc[8,0]='White Sox'
#     mlb_df['team'].replace({'Yankees' : 'YankeesMets', 'Dodgers': 'DodgersAngels', 'Giants': 'GiantsAthletics', 'Cubs': 'CubsWhite Sox', 'Jays': 'Blue Jays'}, inplace=True)
#     mlb_df.iloc[1,3]=(mlb_df.iloc[1,3] + mlb_df.iloc[18,3])/2
#     mlb_df.iloc[25,3]=(mlb_df.iloc[25,3] + mlb_df.iloc[13,3])/2
#     mlb_df.iloc[28,3]=(mlb_df.iloc[28,3] + mlb_df.iloc[11,3])/2
#     mlb_df.iloc[21,3]=(mlb_df.iloc[21,3] + mlb_df.iloc[8,3])/2
#     mlb_df=mlb_df.drop(mlb_df.index[[18,13,11,8]], axis=0)
#     mlb_df.sort_values(by=['team'], inplace=True)
#
#     print(mlb_df)
#     win_loss_by_region = mlb_df['W/L Ratio']
#
#     corr, pval= stats.pearsonr(population_by_region, win_loss_by_region)
#     print(corr)
#     return corr
#
# mlb_correlation()

# def nfl_correlation():
#     import pandas as pd
#     import numpy as np
#     import scipy.stats as stats
#     import re
#
#     cities=pd.read_html("wikipedia_data.html")[1]
#     cities=cities.iloc[:-1,[0,3,5,6,7,8]]
#     cities.replace('\[\w.*\]','', regex=True, inplace=True) # reemplazo [] por espacio ''
#     cities.replace('—',0, regex=True, inplace=True)         # reemplazo — por 0 = NaN
#     cities.replace('',0, regex=True, inplace=True)          # reemplazo '' por 0 = NaN
#     cities['NFL']=cities['NFL'].str.strip()
#     copy_NFL=cities[['Metropolitan area','NFL','Population (2016 est.)[8]']].dropna()
#     copy_NFL.sort_values(by=['NFL'], inplace=True)  #len=26
#     copy_NFL['Population (2016 est.)[8]']=copy_NFL['Population (2016 est.)[8]'].astype('int64')
#
#     print(copy_NFL) #len=29
#
#     population_by_region=copy_NFL['Population (2016 est.)[8]']
#
#
#     nfl_df=pd.read_csv("nfl.csv")
#     nfl_df=nfl_df.iloc[:40,[1,2,11,13,14]] #cargo las columnas que necesito
#     nfl_df=nfl_df.drop(nfl_df.index[[0,5,10,15,20,25,30,35]], axis=0)
#     nfl_df['W']=nfl_df['W'].astype('int64')                  #convierto columna str a int para poder dividir
#     nfl_df['L']=nfl_df['L'].astype('int64')                  #convierto columna str a int para poder dividir
#     nfl_df['W/L Ratio']=nfl_df['W']/(nfl_df['W']+ nfl_df['L'])  #convierto columna str a int
#     nfl_df.replace('\*','', regex=True, inplace=True)
#     nfl_df.replace('\+','', regex=True, inplace=True)
#     nfl_df['team'].replace("[\D].*\s",'',inplace=True,regex=True)
#     nfl_df['team']=nfl_df['team'].str.strip()
#     nfl_df['team'].replace({'Giants' : 'GiantsJets', 'Rams': 'RamsChargers', '49ers': '49ersRaiders'}, inplace=True)
#     nfl_df.loc[24,('W/L Ratio')]=(nfl_df.loc[24,('W/L Ratio')] + nfl_df.loc[4,('W/L Ratio')])/2
#     nfl_df.loc[36,('W/L Ratio')]=(nfl_df.loc[36,('W/L Ratio')] + nfl_df.loc[17,('W/L Ratio')])/2
#     nfl_df.loc[38,('W/L Ratio')]=(nfl_df.loc[38,('W/L Ratio')] + nfl_df.loc[19,('W/L Ratio')])/2
#     nfl_df=nfl_df.drop([4,17,19],axis=0)
#     nfl_df.sort_values(by=['team'], inplace=True)
#
#     win_loss_by_region = nfl_df['W/L Ratio']
#
#     print(nfl_df)
#
#     corr, pval= stats.pearsonr(population_by_region, win_loss_by_region)
#     print(corr)
#     return corr
#
# nfl_correlation()

import pandas as pd
import numpy as np
import scipy.stats as stats
import re

mlb_df=pd.read_csv("mlb.csv")
nhl_df=pd.read_csv("nhl.csv")
nba_df=pd.read_csv("nba.csv")
nfl_df=pd.read_csv("nfl.csv")
cities=pd.read_html("wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def sports_team_performance():
    # YOUR CODE HERE
    ##INCOMPLETE !!
    #raise NotImplementedError()

    # Note: p_values is a full dataframe, so df.loc["NFL","NBA"] should be the same as df.loc["NBA","NFL"] and
    # df.loc["NFL","NFL"] should return np.nan
    sports = ['NFL', 'NBA', 'NHL', 'MLB']
    p_values = pd.DataFrame({k:np.nan for k in sports}, index=sports)

    #assert abs(p_values.loc["NBA", "NHL"] - 0.02) <= 1e-2, "The NBA-NHL p-value should be around 0.02"
    #assert abs(p_values.loc["MLB", "NFL"] - 0.80) <= 1e-2, "The MLB-NFL p-value should be around 0.80"
    #print(p_values)
    return p_values
sports_team_performance()

#examen
# import pandas as pd
# import numpy as np
# import re

# a = np.arange(8)
# b = a[4:6]
# b[:] = 40
# c = a[4] + a[6]
# print(c)

# s = 'ABCAC'
# print(bool(re.match('A', s)))

# def result():
#     s = 'ACAABAACAAABACDBADDDFSDDDFFSSSASDAFAAACBAAAFASD'
#
#     result = []
#     # compete the pattern below
#     pattern = "[A-Z](?=AAA)"
#     for item in re.finditer(pattern, s):
#       # identify the group number below.
#       result.append(item.group())
#     print(result)
#     return result
# result()

# s= pd.Series([4,7,-5,3],  index=['d', 'b', 'a', 'c'])
# print(s.iloc[0])
# print(s.index[0])
# print(s[0])
# print(s['d'])

# s1= pd.Series([20,15,18,31],  index=['Mango', 'Strawberry', 'Blueberry', 'Vanilla'])
# s2= pd.Series([20,30,15,20,20],  index=['Strawberry', 'Vanilla', 'Banana', 'Mango', 'Plain'])
# s3 = s1.add(s2)
# print(s3['Mango'] >=  s1.add(s2, fill_value = 0)['Mango'])

# Every time we call df.set_index(), the old index will be discarded.

# S = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
# print(S)
# print(S['b':'e'])

# df=pd.DataFrame([[5,6,20],[5,82,28],[71,31,92],[67,37,49]], index=['R1','R2','R3','R4'],columns=['a','b','c'])
# print(df)
#
# f = lambda x: x.max() + x.min()
# df_new = df.apply(f)
# print(df_new[1])

#  new_df.stack()

# df=pd.DataFrame([['item_1','A',10],['item_1','B',20],['item_1','C',np.nan],['item_2','A',5],['item_2','B',10],['item_2','C',15]], index=[0,1,2,3,4,5],columns=['Item','Store','Quantity sold'])
# print(df)
# print(df.groupby('Item').sum().iloc[0]['Quantity sold'])
