#!/usr/bin/env python3
import cgi
import html
import keras
import pandas as pd


form = cgi.FieldStorage()
param1 = form.getfirst("TEXT_1", "IW")
param2 = form.getfirst("TEXT_2", "IF")
param3 = form.getfirst("TEXT_3", "VW")
param4 = form.getfirst("TEXT_4", "FP")
text1 = html.escape(param1)
text2 = html.escape(param2)
text3 = html.escape(param3)
text4 = html.escape(param4)


path_to_model = r'C:/bauman/git_bauman/ebw_model'

human_input = pd.DataFrame({'IW': [47],
                            'IF': [134],
                            'VW': [10],
                            'FP': [110]})


minmax = pd.read_csv(path_to_model + r'/minmax.csv')

human_input['IW'] = (human_input['IW'] - minmax.minIW) / (minmax.maxIW - minmax.minIW)
human_input['IF'] = (human_input['IF'] - minmax.minIF) / (minmax.maxIF - minmax.minIF)
human_input['VW'] = (human_input['VW'] - minmax.minVW) / (minmax.maxVW - minmax.minVW)
human_input['FP'] = (human_input['FP'] - minmax.minFP) / (minmax.maxFP - minmax.minFP)


model= keras.models.load_model(path_to_model)

mypredcit = model.predict(human_input)

predict = pd.DataFrame({'Depth': mypredcit[:,0]*(minmax.maxDepth-minmax.minDepth)+minmax.minDepth, 
                        'Width': mypredcit[:,1]*(minmax.maxWidth-minmax.minWidth)+minmax.minWidth})

# тестовые значение для ответа: 0.92	1.86
 
print(predict)

#print("Predicted Depth: ",predict.Depth)
#print("Predicted Width: ",predict.Width)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Chack data</title>
        </head>
        <body>""")

print("<h1>Calculation !</h1>")
print("<p>TEXT_1: {}</p>".format(param1))
print("<p>TEXT_1: {}</p>".format(param2))
print("<p>TEXT_1: {}</p>".format(param3))
print("<p>TEXT_1: {}</p>".format(param4))

print("""</body>
        </html>""")
