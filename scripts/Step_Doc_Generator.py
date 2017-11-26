
'''
Author : Babu Sekaran
Description : This script collects all the steps added in your python step files 
inside the pointed directory.
Note : BDD step implementation of lettuce, Behave, Squish

'''

from os import listdir,walk
from os.path import join, isfile,isdir, extsep
import sys
import json
import re
from re import match
import codecs



class BDD_step_collector(object):

	def __init__(self,dir):
		self.step_dir = dir
		self.step_file_pattern = '.*steps.*\.py'
		self.step_pattern = re.compile(r'(@(.*)(\(["\'].*))["\']\)')
		self.step_files = []
		self.steps = []

	def find_steps(self):
		for path in listdir(self.step_dir+'.'):
			abs_path = join(self.step_dir,path)
			for directory, sub_directories, files in walk(abs_path):
				for file_name in files:
					if match(self.step_file_pattern, file_name):
						self.step_files.append((file_name,join(directory,file_name)))
						sf_path = join(directory,file_name)
						with codecs.open(sf_path, encoding="utf-8") as current_step_file:
							line_number = 0
							for line in current_step_file:
								match_inst = match(self.step_pattern, line)
								if match_inst:
									if match_inst: self.steps.append((line_number,file_name,match_inst.group()))
								line_number +=1


def main():
	steps_dir = "D:\steps"
	if isdir(steps_dir) : pass
	else : raise LookupError("Add a valid step dirctory to proceed") 
	a = BDD_step_collector(steps_dir)
	a.find_steps()
	step_json = []
	for index , file , step in a.steps:
		#sj = {}
		#sj["step_file"] = str(file)
		#sj["step_index"] = str(index)
		#sj["step_def"] = str(step)
		sl = []
		sl.append(file)
		sl.append(index)
		sl.append(step)
		step_json.append(sl)
		#print sj
	
	with open("step-file.json",'w') as json_outfile:
		json.dump(step_json, json_outfile)


if __name__ == '__main__':
	main()

