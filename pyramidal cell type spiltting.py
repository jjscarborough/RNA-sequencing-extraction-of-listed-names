#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:43:21 2022

@author: joseph
"""

x=0
import pandas

import os

cilialist=[]
location="/Users/joseph/Desktop/GSE153164_RAW/test folder"
os.chdir(location)
data=[]
scgs=pandas.read_excel("/Users/joseph/Desktop/gene lists:papers for RNA seq differentation/MGI cilia gene list mouse.xlsx")
mousecelllist=pandas.read_excel("/Users/joseph/Desktop/gene lists:papers for RNA seq differentation/molecular logic of cellular division cell differentation lists.xlsx")
cilialist1=scgs["Symbol"].tolist()

Astrocyte1=mousecelllist["Astrocyte1" ].tolist()
Astrocyte2=mousecelllist["Astrocyte2"].tolist()
Eppendymocytes=mousecelllist["Eppendymocytes"].tolist()
SCPN=mousecelllist["SCPN"].tolist()
CThPN=mousecelllist["CThPN"].tolist()
layer6b=mousecelllist["layer6b"].tolist()
NearProj=mousecelllist["NearProj"].tolist()
CPN2 =mousecelllist["CPN L2&3"].tolist()
Stellate=mousecelllist["Stellate"].tolist()
CPN56_1=mousecelllist["CPN L5&6 01"].tolist()
CPN56_2=mousecelllist["CPN L5&6 02"].tolist()



resultsAstro1=[]
resultsAsto2=[]
resultsEppendymocytes=[]
resultsSCPN=[]
resultsCThPN=[]
resultslayer6b=[]
resultsNearproj=[]
resultsCPN2=[]
resultsStellate=[]
resultsCPN56_1=[]
resultsCPN56_2=[]


for root, dirs, files in os.walk(location):
    for file in files:
        if file.endswith(".csv"):
            df=pandas.read_csv(file)
            #print(df)
            data=[]
            resultsAstro1=[]
            resultsAstro2=[]
            resultsEppendymocytes=[]
            resultsSCPN=[]
            resultsCThPN=[]
            resultslayer6b=[]
            resultsNearproj=[]
            resultsCPN2=[]
            resultsStellate=[]
            resultsCPN56_1=[]
            resultsCPN56_2=[]
            resultsPY=[]
            resultsIN=[]
            countPy=[]
            countIN=[]
            countciliaPN=[]
            countciliaIN=[]
            ciliaID=[]
            cellID1=[]
            cellIDAstro1=["genes"]
            cellIDAstro2=["genes"]
            cellIDEppendymocytes=["genes"]
            cellIDSCPN=["genes"]
            cellIDCThPN=["genes"]
            cellIDlayer6b=["genes"]
            cellIDNearproj=["genes"]
            cellIDCPN2=["genes"]
            cellIDStellate=["genes"]
            cellIDCPN56_1=["genes"]
            cellIDCPN56_2=["genes"]
            Astro1cells=pandas.DataFrame()
            Astro2cells=pandas.DataFrame()
            Eppendymocytescells=pandas.DataFrame()
            SCPNcells=pandas.DataFrame()
            CThPNcells=pandas.DataFrame()
            layer6bcells=pandas.DataFrame()
            Nearprojcells=pandas.DataFrame()
            CPN2cells=pandas.DataFrame()
            Stellatecells=pandas.DataFrame()
            CPN56_1cells=pandas.DataFrame()
            CPN56_2cells=pandas.DataFrame()
            PNcells=pandas.DataFrame()
            INcells=pandas.DataFrame()
            finalcolumindexPN=1
            finalcolumindexIN=1
            finalcolumindexAstro1=1
            finalcolumindexAstro2=1
            finalcolumindexEppendymocytes=1
            finalcolumindexSCPN=1
            finalcolumindexCThPN=1
            finalcolumindexlayer6b=1
            finalcolumindexNearproj=1
            finalcolumindexCPN2=1
            finalcolumindexStellate=1
            finalcolumindexCPN56_1=1
            finalcolumindexCPN56_2=1
            u=0
            c=2
            totalrows=len(df)
            totalcolumns=len(df.columns)
            for number in range(totalcolumns-2):
                countPy=[]
                countIN=[]
                countAstro1=[]
                countAstro2=[]
                countEppendymocytes=[]
                countSCPN=[]
                countCThPN=[]
                countlayer6b=[]
                countNearproj=[]
                countCPN2=[]
                countStellate=[]
                countCPN56_1=[]
                countCPN56_2=[]
                countPy=[]
                countIN=[]
                ciliacountAstro1=[]
                ciliacountAstro2=[]
                ciliacountEppendymocytes=[]
                ciliacountSCPN=[]
                ciliacountCThPN=[]
                ciliacountlayer6b=[]
                ciliacountNearproj=[]
                ciliacountCPN2=[]
                ciliacountStellate=[]
                ciliacountCPN56_1=[]
                ciliacountCPN56_2=[]
                countPy=[]
                countIN=[]
                resultsAstro1=[]
                resultsAstro2=[]
                resultsEppendymocytes=[]
                resultsSCPN=[]
                resultsCThPN=[]
                resultslayer6b=[]
                resultsNearproj=[]
                resultsCPN2=[]
                resultsStellate=[]
                resultsCPN56_1=[]
                resultsCPN56_2=[]
                ciliaIDAstro1=[]
                ciliaIDAstro2=[]
                ciliaIDEppendymocytes=[]
                ciliaIDSCPN=[]
                ciliaIDCThPN=[]
                ciliaIDlayer6b=[]
                ciliaIDNearproj=[]
                ciliaIDCPN2=[]
                ciliaIDStellate=[]
                ciliaIDCPN56_1=[]
                ciliaIDCPN56_2=[] 
                countciliaPN=[]
                countciliaIN=[]
                ciliaIDIN=[]
                ciliaIDPN=[]
                resultsPY=[]
                countPy=[]
                resultsIN=[]
                countIN=[]
                numberAstro1genes=0
                numberAstro2genes=0
                numberEppendymocytes=0
                numberSCPN=0
                numberCThPN=0
                numberlayer6b=0
                numberNearproj=0
                numberCPN2=0
                numberStellate=0
                numberCPN56_1=0
                numberCPN56_2=0
               
                totalexpressionPN=0
                numberINgenes=0
                totalexpressionIN=0
                cellIDPN=['genes']
                cellIDIN=['genes']
                cellid=df.iloc[0,c]
                y=0
                u=0
                for number in range(totalrows):
                    count=df.iloc[u,c]
                    genename=df.iloc[u,1]
                    if count>=1:
               
                
                #print(count)
                   
                   
                        if genename in Astrocyte1:
                                        resultsAstro1.append(genename)
                                        countAstro1.append(count)
                        if genename in Astrocyte2:
                                        resultsAstro2.append(genename)
                                        countAstro2.append(count)
                        if genename in Eppendymocytes:
                                        resultsEppendymocytes.append(genename)
                                        countEppendymocytes.append(count)
                        if genename in SCPN:
                                        resultsSCPN.append(genename)
                                        countSCPN.append(count)
                        if genename in CThPN:
                                        resultsCThPN.append(genename)
                                        countCThPN.append(count)
                        if genename in layer6b:
                                        resultslayer6b.append(genename)
                                        countlayer6b.append(count)
                        if genename in NearProj:
                                        resultsNearproj.append(genename)
                                        countNearproj.append(count)
                        if genename in CPN2:
                                        resultsCPN2.append(genename)
                                        countCPN2.append(count)
                        if genename in Stellate:
                                        resultsStellate.append(genename)
                                        countStellate.append(count)
                        if genename in CPN56_1:
                                        resultsCPN56_1.append(genename)
                                        countCPN56_1.append(count)
                        if genename in CPN56_2:
                                        resultsCPN56_2.append(genename)
                                        countCPN56_2.append(count)
                        
                                        
                
                    u+=1
                
                numberPNgenes=len(resultsPY)
                totalexpressionPN=sum(countPy)
                numberINgenes=len(resultsIN)
                totalexpressionIN=sum(countIN)
                numberAstro1genes=len(resultsAstro1)
                numberAstro2genes=len(resultsAstro2)
                numberEppendymocytes=len(resultsEppendymocytes)
                numberSCPN=len(resultsSCPN)
                numberCThPN=len(resultsCThPN)
                numberlayer6b=len(resultslayer6b)
                numberNearproj=len(resultsNearproj)
                numberCPN2=len(resultsCPN2)
                numberStellate=len(resultsStellate)
                numberCPN56_1=len(resultsCPN56_1)
                numberCPN56_2=len(resultsCPN56_2)
                totalexpressionAstro1=sum(countAstro1)
                totalexpressionAstro2=sum(countAstro2)
                totalexpressionEppendymocytes=sum(countEppendymocytes)
                totalexpressionSCPN=sum(countSCPN)
                totalexpressionCThPN=sum(countCThPN)
                totalexpressionlayer6b=sum(countlayer6b)
                totalexpressionNearproj=sum(countNearproj)
                totalexpressionCPN2=sum(countCPN2)
                totalexpressionStellate=sum(countStellate)
                totalexpressionCPN56_1=sum(countCPN56_1)
                totalexpressionCPN56_2=sum(countCPN56_2)
                print("astro1", numberAstro1genes)
                print("astro2", numberAstro2genes)
                print("Eppend", numberEppendymocytes)
                print("SCPN", numberSCPN)
                print("CThPN", numberCThPN)
                print("layer6b", numberlayer6b)
                print("Nearproj", numberNearproj)
                print("CPN2", numberCPN2)
                print("stellate", numberStellate)
                print("CN56_1", numberCPN56_1)
                print("CPN56_2", numberCPN56_2)
                #print("PY", resultsPY)
                #print("IN", resultsIN)
                if numberAstro1genes>=numberAstro2genes and numberAstro1genes>=numberEppendymocytes and numberAstro1genes>=numberSCPN and numberAstro1genes>=numberCThPN and numberAstro1genes>=numberlayer6b and numberAstro1genes>=numberNearproj and numberAstro1genes>=numberCPN2 and numberAstro1genes>=numberStellate and numberAstro1genes>=numberCPN56_1 and numberAstro1genes>=numberCPN56_2:
                    cellIDAstro1.append(cellid)
                    y=0
                    for number in range(totalrows):
                        count1=df.iloc[y,c]
                        genename=df.iloc[y,1]
                        y+=1
                        if genename in cilialist1:
                            if count1>=0:
                                ciliacountAstro1.append(count1)
                                ciliaIDAstro1.append(genename)
                    Astro1cells[0]=ciliaIDAstro1
                    Astro1cells[finalcolumindexAstro1]=ciliacountAstro1
                    print(Astro1cells)
                if numberAstro2genes>=numberEppendymocytes and numberAstro2genes>=numberSCPN and numberAstro2genes>=numberCThPN and numberAstro2genes>=numberlayer6b and numberAstro2genes>=numberNearproj and numberAstro2genes>=numberCPN2 and numberAstro2genes>=numberStellate and numberAstro2genes>=numberCPN56_1 and numberAstro2genes>=numberCPN56_2 and numberAstro2genes>=numberAstro1genes:
                    cellIDAstro1.append(cellid)
                    y=0
                    for number in range(totalrows):
                        count1=df.iloc[y,c]
                        genename=df.iloc[y,1]
                        y+=1
                        if genename in cilialist1:
                            if count1>=0:
                                ciliacountAstro2.append(count1)
                                ciliaIDAstro2.append(genename)
                    Astro2cells[0]=ciliaIDAstro2
                    Astro2cells[finalcolumindexAstro2]=ciliacountAstro2
                if numberEppendymocytes>=numberSCPN and numberEppendymocytes>=numberCThPN and numberEppendymocytes>=numberlayer6b and numberEppendymocytes>=numberNearproj and numberEppendymocytes>=numberCPN2 and numberEppendymocytes>=numberStellate and numberEppendymocytes>=numberCPN56_1 and numberEppendymocytes>=numberCPN56_2 and numberEppendymocytes>=numberAstro1genes and numberEppendymocytes>=numberAstro2genes:
                    cellIDEppendymocytes.append(cellid)
                    y=0
                    for number in range(totalrows):
                        count1=df.iloc[y,c]
                        genename=df.iloc[y,1]
                        y+=1
                        if genename in cilialist1:
                            if count1>=0:
                                ciliacountEppendymocytes.append(count1)
                                ciliaIDEppendymocytes.append(genename)
                    Eppendymocytescells[0]=ciliaIDEppendymocytes
                    Eppendymocytescells[finalcolumindexEppendymocytes]=ciliacountEppendymocytes
                if numberSCPN>=numberCThPN and numberSCPN>=numberlayer6b and numberEppendymocytes>=numberNearproj and numberSCPN>=numberCPN2 and numberSCPN>=numberStellate and numberSCPN>=numberCPN56_1 and numberSCPN>=numberCPN56_2 and numberSCPN>=numberAstro1genes and numberSCPN>=numberAstro2genes and numberSCPN>=numberEppendymocytes:
                    cellIDSCPN.append(cellid)
                    y=0
                    for number in range(totalrows):
                        count1=df.iloc[y,c]
                        genename=df.iloc[y,1]
                        y+=1
                        if genename in cilialist1:
                            if count1>=0:
                                ciliacountSCPN.append(count1)
                                ciliaIDSCPN.append(genename)
                    SCPNcells[0]=ciliaIDSCPN
                    SCPNcells[finalcolumindexSCPN]=ciliacountSCPN
                if numberCThPN>=numberlayer6b and numberCThPN>=numberNearproj and numberCThPN>=numberCPN2 and numberCThPN>=numberStellate and numberCThPN>=numberCPN56_1 and numberCThPN>=numberCPN56_2 and numberCThPN>=numberAstro1genes and numberCThPN>=numberAstro2genes and numberCThPN>=numberEppendymocytes and numberCThPN>=numberSCPN:
                    cellIDCThPN.append(cellid)
                    y=0
                    for number in range(totalrows):
                        count1=df.iloc[y,c]
                        genename=df.iloc[y,1]
                        y+=1
                        if genename in cilialist1:
                            if count1>=0:
                                ciliacountCThPN.append(count1)
                                ciliaIDCThPN.append(genename)
                    CThPNcells[0]=ciliaIDCThPN
                    CThPNcells[finalcolumindexCThPN]=ciliacountCThPN
                if numberlayer6b>=numberNearproj and numberlayer6b>=numberCPN2 and numberlayer6b>=numberStellate and numberlayer6b>=numberCPN56_1 and numberlayer6b>=numberCPN56_2 and numberlayer6b>=numberAstro1genes and numberlayer6b>=numberAstro2genes and numberlayer6b>=numberEppendymocytes and numberlayer6b>=numberSCPN and numberlayer6b>=numberCThPN:
                    cellIDlayer6b.append(cellid)
                    y=0
                    for number in range(totalrows):
                        count1=df.iloc[y,c]
                        genename=df.iloc[y,1]
                        y+=1
                        if genename in cilialist1:
                            if count1>=0:
                                ciliacountlayer6b.append(count1)
                                ciliaIDlayer6b.append(genename)
                    layer6bcells[0]=ciliaIDlayer6b
                    layer6bcells[finalcolumindexlayer6b]=ciliacountlayer6b
               
                if numberNearproj>=numberCPN2 and numberNearproj>=numberStellate and numberNearproj>=numberCPN56_1 and numberNearproj>=numberCPN56_2 and numberNearproj>=numberAstro1genes and numberNearproj>=numberAstro2genes and numberNearproj>=numberEppendymocytes and numberNearproj>=numberSCPN and numberNearproj>=numberCThPN:
                    cellIDNearproj.append(cellid)
                    y=0
                    for number in range(totalrows):
                        count1=df.iloc[y,c]
                        genename=df.iloc[y,1]
                        y+=1
                        if genename in cilialist1:
                            if count1>=0:
                                ciliacountNearproj.append(count1)
                                ciliaIDNearproj.append(genename)
                    Nearprojcells[0]=ciliaIDNearproj
                    Nearprojcells[finalcolumindexNearproj]=ciliacountNearproj
                if numberCPN2>=numberStellate and numberCPN2>=numberCPN56_1 and numberCPN2>=numberCPN56_2 and numberCPN2>=numberAstro1genes and numberCPN2>=numberAstro2genes and numberCPN2>=numberEppendymocytes and numberCPN2>=numberSCPN and numberCPN2>=numberCThPN:
                    cellIDCPN2.append(cellid)
                    y=0
                    for number in range(totalrows):
                        count1=df.iloc[y,c]
                        genename=df.iloc[y,1]
                        y+=1
                        if genename in cilialist1:
                            if count1>=0:
                                ciliacountCPN2.append(count1)
                                ciliaIDCPN2.append(genename)
                    CPN2cells[0]=ciliaIDCPN2
                    CPN2cells[finalcolumindexCPN2]=ciliacountCPN2
                if numberStellate>=numberCPN56_1 and numberStellate>=numberCPN56_2 and numberStellate>=numberAstro1genes and numberStellate>=numberAstro2genes and numberStellate>=numberEppendymocytes and numberStellate>=numberSCPN and numberStellate>=numberCThPN and numberStellate>=numberlayer6b and numberStellate>=numberNearproj and numberStellate>=numberCPN2:
                    cellIDStellate.append(cellid)
                    y=0
                    for number in range(totalrows):
                        count1=df.iloc[y,c]
                        genename=df.iloc[y,1]
                        y+=1
                        if genename in cilialist1:
                            if count1>=0:
                                ciliacountStellate.append(count1)
                                ciliaIDStellate.append(genename)
                    Stellatecells[0]=ciliaIDStellate
                    Stellatecells[finalcolumindexStellate]=ciliacountStellate
                if numberCPN56_1>=numberCPN56_2 and numberCPN56_1>=numberAstro1genes and numberCPN56_1>=numberAstro2genes and numberCPN56_1>=numberEppendymocytes and numberCPN56_1>=numberSCPN and numberCPN56_1>=numberCThPN and numberCPN56_1>=numberlayer6b and numberCPN56_1>=numberNearproj and numberCPN56_1>=numberCPN2 and numberCPN56_1>=numberStellate:
                    cellIDCPN56_1.append(cellid)
                    y=0
                    for number in range(totalrows):
                        count1=df.iloc[y,c]
                        genename=df.iloc[y,1]
                        y+=1
                        if genename in cilialist1:
                            if count1>=0:
                                ciliacountCPN56_1.append(count1)
                                ciliaIDCPN56_1.append(genename)
                    print(len(ciliacountCPN56_1))
                    print(len(ciliaIDCPN56_1))
                    CPN56_1cells[0]=ciliaIDCPN56_1
                    CPN56_1cells[finalcolumindexCPN56_1]=ciliacountCPN56_1
                if numberCPN56_2>=numberAstro1genes and numberCPN56_2>=numberAstro2genes and numberCPN56_2>=numberEppendymocytes and numberCPN56_2>=numberSCPN and numberCPN56_2>=numberCThPN and numberCPN56_2>=numberlayer6b and numberCPN56_2>=numberNearproj and numberCPN56_2>=numberCPN2 and numberCPN56_2>=numberStellate and numberCPN56_2>=numberCPN56_1:
                    cellIDCPN56_2.append(cellid)
                    y=0
                    for number in range(totalrows):
                        count1=df.iloc[y,c]
                        genename=df.iloc[y,1]
                        y+=1
                        if genename in cilialist1:
                            if count1>=0:
                                ciliacountCPN56_2.append(count1)
                                ciliaIDCPN56_2.append(genename)
                    CPN56_2cells[0]=ciliaIDCPN56_2
                    CPN56_2cells[finalcolumindexCPN56_2]=ciliacountCPN56_2


                
               
                    
                    
                     
                                
                finalcolumindexAstro1+=1
                finalcolumindexAstro2+=1
                finalcolumindexEppendymocytes+=1
                finalcolumindexSCPN+=1
                finalcolumindexCThPN+=1
                finalcolumindexlayer6b+=1
                finalcolumindexNearproj+=1
                finalcolumindexCPN2+=1
                finalcolumindexStellate+=1
                finalcolumindexCPN56_1+=1
                finalcolumindexCPN56_2+=1                
                finalcolumindexPN+=1
                finalcolumindexIN+=1                
                c+=1
                
                
                
                
            
           
            Astro1cells.to_excel(file + 'astro1' +'.xlsx')
            Astro2cells.to_excel(file + 'astro2' +'.xlsx')
            Eppendymocytescells.to_excel(file + 'eppendymocytes' +'.xlsx')
            SCPNcells.to_excel(file + 'SCPN' +'.xlsx')
            CThPNcells.to_excel(file + 'CThPN' +'.xlsx')
            layer6bcells.to_excel(file + 'layer6b' +'.xlsx')
            Nearprojcells.to_excel(file +'nearproj' +'.xlsx')
            CPN2cells.to_excel(file + 'CPN2' +'.xlsx')
            Stellatecells.to_excel(file + 'Stellate' +'.xlsx')
            CPN56_1cells.to_excel(file + 'CPN56_1' +'.xlsx')
            CPN56_2cells.to_excel(file + 'CPN56_2' +'.xlsx')
            
            
            
#print(data)      
