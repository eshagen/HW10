def numbered_lines():

	with open ("small.txt", 'r') as f:
		line_num = 1
		data = f.readlines()
		with open ("new_file", 'w') as f2:	

			for line in data:
				f2.write(str(line_num) + "\t" + line + "\n")
				line_num += 1
			
		
		


##############################################################################
def main():
    numbered_lines()

if __name__ == '__main__':
    main()