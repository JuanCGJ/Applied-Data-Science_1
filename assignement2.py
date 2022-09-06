# PARTE A
# import pandas as pd
#
# def proportion_of_education():
#     df= pd.read_csv('NISPUF17.csv', index_col=0)
#     ed=df['EDUC1'];
#     NumMothers=len(ed)
#     # print('Num Mothers: ', NumMothers)
#     lessth=[]
#     eq=[]
#     higherth=[]
#     colleg=[]
#     for i in ed:
#         if   i == 1:
#             lessth.append(i)
#             portionless=len(lessth)/NumMothers
#         elif i == 2:
#             eq.append(i)
#             portioneq=len(eq)/NumMothers
#         elif i == 3:
#             higherth.append(i)
#             portionhigher=len(higherth)/NumMothers
#         else :
#             colleg.append(i)
#             portioncolleg=len(colleg)/NumMothers
#     proportion_of_education= {"less than high school":portionless,
#                               "high school":portioneq,
#                               "more than high school but not college":portionhigher,
#                               "college":portioncolleg}
#     print(proportion_of_education)
#     return proportion_of_education
# proportion_of_education()

#PARTE B
# import pandas as pd
# def average_influenza_doses():
#     df=pd.read_csv('NISPUF17.csv', index_col=0)
#     copia= df.drop(df[df['CBF_01']>2].index)       #aplico filtro 1. CBF=1 o 2.
#     columnas=copia[["CBF_01","P_NUMFLU"]].dropna() #aplico filtro2. P_NUMFLU sin datos Nan
#     fedyes=columnas[columnas['CBF_01']==1]         #valores de P_NUMFLU cuando CBF=1
#     promfedyes=fedyes['P_NUMFLU'].mean()           #promedio valores de P_NUMFLU cuando CBF=1
#     fedNo=columnas[columnas['CBF_01']==2]          #valores de P_NUMFLU cuando CBF=2
#     promfedNo=fedNo['P_NUMFLU'].mean()             #promedio valores de P_NUMFLU cuando CBF=2
#     average_influenza_doses=(promfedyes,promfedNo)
#     print(average_influenza_doses)
#     return average_influenza_doses
# average_influenza_doses()


# #PARTE C
# import pandas as pd
# df=pd.read_csv('NISPUF17.csv', index_col=0)
# def chickenpox_by_sex():
#     copy= df
#     columnas=copy[["HAD_CPOX","P_NUMVRC", "SEX"]]
#     print(columnas)
#     print('\n')
#     #------------------------------- male -------------------------------------
#     mask1=(columnas['SEX']==1) & (columnas['HAD_CPOX']==1) & (columnas['P_NUMVRC']>=1)
#     hvc=columnas.where(mask1).dropna()            #Dataframe de hombres con vacuna contagiados
#     print(hvc)
#     thc=len(hvc)                                  #total hombres contagiados con al menos una vacuna
#     print('Hombres contagiados con al menos una vacuna : ', thc)
#
#     mask2=(columnas['SEX']==1) & (columnas['HAD_CPOX']==2) & (columnas['P_NUMVRC']>=1)
#     hvnc=columnas.where(mask2).dropna()           #Dataframe de hombres con vacuna no contagiados
#     print('\n',hvnc)
#     thnc=len(hvnc)                                #total hombres no contagiados con al menos una vacuna
#     print('Hombres no contagiados con al menos una vacuna : ', thnc)
#
#     maleratio=thc/thnc                            #Hombres contagiados vs No contagiados, todos con vacuna
#     print('\nMale Ratio', maleratio)
#     #------------------------------- female -----------------------------------
#     mask3=(columnas['SEX']==2) & (columnas['HAD_CPOX']==1) & (columnas['P_NUMVRC']>=1)
#     mvc=columnas.where(mask3).dropna()            #Dataframe de mujeres con vacuna contagiadas
#     print('\n',mvc)
#     tmc=len(mvc)                                  #total mujeres contagiadass con al menos una vacuna
#     print('\nMujeres contagiadas con al menos una vacuna : ', tmc)
#
#     mask4=(columnas['SEX']==2) & (columnas['HAD_CPOX']==2) & (columnas['P_NUMVRC']>=1)
#     mvnc=columnas.where(mask4).dropna()           #Dataframe de mujeres con vacuna no contagiadas
#     print('\n',mvnc)
#     tmnc=len(mvnc)                                #total mujeres no contagiados con al menos una vacuna
#     print('\nMujeres no contagiadas con al menos una vacuna : ', tmnc)
#
#     femaleratio=tmc/tmnc                            #Hombres contagiados vs No contagiados, todos con vacuna
#     print('\nFemale Ratio', femaleratio)
#
#     chickenpox_by_sex={"male":maleratio, "female":femaleratio}
#     print('\n',chickenpox_by_sex)
#     return chickenpox_by_sex
# chickenpox_by_sex()


# # #PARTE D
# import scipy.stats as stats
# import pandas as pd
# df=pd.read_csv('NISPUF17.csv')
# def corr_chickenpox():
#     copy= df
#     columnas=copy[["HAD_CPOX","P_NUMVRC"]]
#     mask4=(columnas["HAD_CPOX"].lt(3))
#     res=columnas.where(mask4).dropna()
#     res.sort_index(inplace=True)
#     # print(res)
#     # print(res["HAD_CPOX"].unique())
#     # print(res["P_NUMVRC"].unique())
#
#     # here is some stub code to actually run the correlation
#     corr, pval=stats.pearsonr(res["HAD_CPOX"],res["P_NUMVRC"])  #se devuelven dos variables coor, pval
#     # print('Correlacion: ',corr)
#     # print('pval:         ', pval)
#     return corr
# corr_chickenpox()
