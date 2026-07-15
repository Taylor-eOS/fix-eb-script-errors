data = open('eb_campaign_script.txt', 'rb').read()
pos = 0
while True:
    try:
        data[pos:].decode('utf-8')
        break
    except UnicodeDecodeError as e:
        abs_pos = pos + e.start
        line_num = data[:abs_pos].count(b'\n') + 1
        context = data[max(0,abs_pos-20):abs_pos+20]
        print(line_num, context)
        pos = abs_pos + 1
