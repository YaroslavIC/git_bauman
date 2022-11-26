# coding: windows-1251
# код отвечающий за предсказание с использованием ИНС 
# код будет использован в консольном приложении

import keras
import pandas as pd

# путь до сохраненной модели
path_to_model = r'C:/bauman/git_bauman/ebw_model'

minmax = pd.read_csv(path_to_model + r'/minmax.csv')

print("Введите параметр IW (сварочный ток), значение между [",minmax.minIW,',',minmax.maxIW,']')
IW_human_input = input()
if IW_human_input=='':
    IW_human_input = (minmax.minIW+minmax.maxIW)/2
else:
    IW_human_input = float(IW_human_input)
    
print("Введите параметр IF (ток фокусировки эл. пучка), значение между [",minmax.minIF,',',minmax.maxIF,']')
IF_human_input = input()
if IF_human_input=='':
    IF_human_input = (minmax.minIF+minmax.maxIF)/2
else:
    IF_human_input = float(IF_human_input)


print("Введите параметр IF (ток фокусировки эл. пучка), значение между [",minmax.minVW,',',minmax.maxVW,']')
VW_human_input = input()
if VW_human_input=='':
    VW_human_input = (minmax.minVW+minmax.maxVW)/2
else:
    VW_human_input = float(VW_human_input)

print("Введите параметр IF (ток фокусировки эл. пучка), значение между [",minmax.minVW,',',minmax.maxVW,']')
FP_human_input = input()
if FP_human_input=='':
    FP_human_input = (minmax.minFP+minmax.maxFP)/2
else:
    FP_human_input = float(FP_human_input)

    
human_input = pd.DataFrame({'IW': [IW_human_input],
                            'IF': [IF_human_input],
                            'VW': [VW_human_input],
                            'FP': [FP_human_input]})

human_input['IW'] = (human_input['IW'] - minmax.minIW) / (minmax.maxIW - minmax.minIW)
human_input['IF'] = (human_input['IF'] - minmax.minIF) / (minmax.maxIF - minmax.minIF)
human_input['VW'] = (human_input['VW'] - minmax.minVW) / (minmax.maxVW - minmax.minVW)
human_input['FP'] = (human_input['FP'] - minmax.minFP) / (minmax.maxFP - minmax.minFP)

#human_input = pd.DataFrame({'IW': [0.5],
#                            'IF': [0.5],
#                            'VW': [0.5],
#                            'FP': [0.5]})


model= keras.models.load_model(path_to_model)

mypredcit = model.predict(human_input)

predict = pd.DataFrame({'Depth': mypredcit[:,0]*(minmax.maxDepth-minmax.minDepth)+minmax.minDepth, 
                        'Width': mypredcit[:,1]*(minmax.maxWidth-minmax.minWidth)+minmax.minWidth})

# тестовые значение для ответа: 0.92	1.86
 
print(predict)

#print("Predicted Depth: ",predict.Depth)
#print("Predicted Width: ",predict.Width)
