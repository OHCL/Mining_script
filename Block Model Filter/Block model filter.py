import PySimpleGUI as sg

sg.theme("DarkBlue")
sg.set_options(font=("Courier New", 16))

fid = open("STS_GSI_COMP01_2.prn",'r')

textline = fid.readlines()

fid.close()

DATA = []
filterdata = []
setValues = set()

for LINE in textline:
    DATA.append([float(VALUE) for VALUE in LINE.split()])
    setValues.add(int([float(VALUE) for VALUE in LINE.split()][3]))

minValues = int(min(setValues))
maxValues = int(max(setValues))
print(minValues, maxValues)

layout = [
    [sg.Spin([i for i in range(minValues, maxValues)],     initial_value=minValues, size=(2, 1), enable_events=True, key='-MIN-'), sg.Text('Minimum value')],
    [sg.Spin([i for i in range(minValues+1, maxValues+1)], initial_value=maxValues, size=(2, 1), enable_events=True, key='-MAX-'), sg.Text('Maximum value')],
    [sg.Submit(), sg.Cancel()],
]

window = sg.Window('Title', layout, finalize=True)

value_min, value_max = minValues, maxValues

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-MAX-':
        value_max = values[event]
        window['-MIN-'].update(values=[i for i in range(minValues, value_max)])
    elif event == '-MIN-':
        value_min = values[event]
        window['-MAX-'].update(values=[i for i in range(value_min+1, maxValues+1)])
    print(event, values)

window.close()
print(min)

for DATALINE in DATA:
    #print(DATALINE[3])
    if value_min <= DATALINE[3] < value_max:
        strdataline = ' '.join(str(VALUE) for VALUE in DATALINE)
        filterdata.append(strdataline)

fid=open("GSI_FILTER.prn",'w')
fid.write('\n'.join(filterdata))
fid.close()