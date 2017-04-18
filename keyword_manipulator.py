import os
import re
files = [f for f in os.listdir('/home/erowz/KeywordCollections') if '.' in f and f.split('.')[1] == 'csv']
#files = ['AR.csv']
print('cleaing old manipulated keyword collections. . . . .\n\n')
os.system('rm -rf ./Manipulated_*')

for item in files:
	fl = open('./Manipulated_'+item,'w' )
	with open('/home/erowz/KeywordCollections/'+item) as f:
		next(f)
		for line in f:
			tmp1 = re.findall(r'\"(.*?)\"',line)
			if len(tmp1)==1:
				line = line.replace('"'+tmp1[0]+'",',',')
				line = line.strip()
				tmp = line.split(',')
				tmp[5] = tmp1[0]
			elif len(tmp1)==2:
				line = line.replace('"'+tmp1[0]+'",',',')
				line = line.replace('"'+tmp1[1]+'",',',')
				tmp = line.split(',')
				tmp[1] == tmp[0]
				tmp[5] == tmp[1]
			else:
				
				line = line.strip()
				tmp = line.split(',')
			tmp.remove(tmp[0])
			tmp.insert(1,'/'+tmp[0].replace(' ','-'))
			
			if tmp[2] != 'true':
				tmp[2] = ''
			tmp[3] = tmp[3].split('T')[0]
			if tmp[3] == '0001-01-01':
				tmp[3] = ''
			if tmp[6] != 'true': 
				tmp[6] = ''
			if tmp[8] != '': 
				tmp[8] = '/'+tmp[8].replace(' ','-')
			if tmp[8] == '': 
				tmp.insert(9,'false')
			else: 
				tmp.insert(9,'true')
			if tmp[10] != 'true': 
				tmp[10] = ''
			fl.write('|'.join(tmp)+'\n')
		print(item+' processed')

