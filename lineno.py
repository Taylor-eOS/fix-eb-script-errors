data_place = int(input("Enter value: "))
data = open('eb_campaign_script.txt', 'rb').read()
line_num = data[:data_place:].count(b'\n') + 1
print(line_num)
