import os
import subprocess

files = [f for f in os.listdir('./') if f.split('_')[0] == 'Manipulated']
#print(files)
#files = ['Manipulated_bpfs-fr2.csv']
for f in files:
	if f == 'Manipulated_bpfs-fr2.csv':
		f = 'Manipulated_FR.csv'
	elif f == 'Manipulated_BR.csv':
		continue
	os.system('bq rm -f KeywordCollections.'+f.split('_')[1].split('.')[0]+'_Keywords')
	os.system('bq mk KeywordCollections.'+f.split('_')[1].split('.')[0]+'_Keywords  KeywordName:string,URL:string,IsKeywordDeleted:string,LastCrawlingDate:string,LastCategoryId:string,LastKeywordName:string,NoIndexNofollowMetaTag:string,TotalSearch:integer,i301:string,Has301:string,QualityFactor:string,AMS:integer')
	#os.system('rm -rf tmp/')
	#os.system('mkdir tmp/')
	#os.system('cd tmp/ && split -l 3500 ../'+f)
	#subfiles = [b for b in os.listdir('./tmp/') if b<>f]
	#print subfiles
	#for fl in subfiles:
	if f == 'Manipulated_FR.csv':
			s = subprocess.Popen(['bq','load','--max_bad_records=50','--field_delimiter=|','KeywordCollections.'+f.split('_')[1].split('.')[0]+'_Keywords', './Manipulated_bpfs-fr2.csv'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	else:
			s = subprocess.Popen(['bq','load','--max_bad_records=50','--field_delimiter=|','KeywordCollections.'+f.split('_')[1].split('.')[0]+'_Keywords', './'+f], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			stdout = s.stdout.readlines()
	print('stdout',stdout)
	if stdout == ['\n', '\n']:
	       	 		print '\nSuccessfully loaded into '+f.split('_')[1].split('.')[0]+'_Keywords\n',
				continue
	if stdout[2].split(' ')[0].lower() == 'warning':
        			print '\nSuccessfully loaded into '+f.split('_')[1].split('.')[0]+'_Keywords\n',
			        continue
	if stdout[2].split(' ')[0].lower() == 'bigquery' :
        			repeat = True
	  	      		print 'failed to load '+f+ ', repeating 10 times until first success. . .'
				continue
        			while repeat:
            				for i in range(10):
                				a = subprocess.Popen(['bq','load','--max_bad_records=10','--field_delimiter=|','KeywordCollections.'+f.split('_')[1].split('.')[0]+'_Keywords', './'+f], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		               			stdout = a.stdout.readlines()
        		      	  		if stdout == ['\n','\n']:
                		    			print('Successfully loaded')
                    					repeat = False
                    					break
	                			if stdout[2].split(' ')[0].lower() == 'warning':
        	            				print('Successfully loaded')
	                	    			repeat = False
        	            				break
	        	   	 	repeat = False

