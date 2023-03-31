valid = ""
while 1:
    get = input()
    if get[0:2] == "TH" and len(get) == 5:
        try:
            int(get[2:])
            valid = get
            break
        except:
            continue
print(valid)