#import shutil

input_file = 'eb_campaign_script.txt'
#shutil.copy(input_file, input_file + '.bak')
data = open(input_file, 'rb').read()
fixed = data.decode('windows-1252')
open(input_file, 'w', encoding='utf-8').write(fixed)
