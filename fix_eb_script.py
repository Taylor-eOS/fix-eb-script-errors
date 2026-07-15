input_file = 'eb_campaign_script.txt'
data = open(input_file, 'rb').read()
fixed = data.decode('windows-1252')
open('eb_campaign_script_fixed.txt', 'w', encoding='utf-8').write(fixed)
