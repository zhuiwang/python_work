data_dict = {}
name = []
while True:
    try:
        data = input().split(' ')
        if data == '':
            break
        file_name = data[0].split('\\')[-1]
        if len(file_name)>=16:
            file_name = file_name[-16:]
        else:
            pass
        v = file_name + ' ' + str(data[-1])
        if v not in data_dict.keys():
            name.append(v)
            data_dict[v] = 1
        else:
            data_dict[v] += 1
    except:
        break
for item in name[-8:]:
    print(item + ' ' + str(data_dict[item]) + ' ')
