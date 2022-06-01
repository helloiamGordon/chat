#讀取檔案
def read_file(filename) :
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines

#convert
def convert(lines):
	Allen_word_count = 0
	Allen_image_count = 0
	Allen_sticker_count = 0
	Viki_word_count = 0
	Viki_image_count = 0
	Viki_sticker_count = 0
	for line in lines :
		m = line.split(' ')
		time = m[0]
		name = m[1]
		if name =='Allen':
			if m[2] == '圖片' :
				Allen_image_count += 1
			elif m[2] == '貼圖' :
				Allen_sticker_count += 1
			else:		
				for s in m[2:]:
					Allen_word_count += len(s)
		elif name =='Viki':
			if m[2] == '圖片' :
				Viki_image_count += 1
			elif m[2] == '貼圖' :
				Viki_sticker_count += 1
			else:	
				for s in m[2:]:
					Viki_word_count += len(s)	
	print('Allen有幾',Allen_word_count,'字')	
	print('Allen有幾', Allen_image_count,'張圖片')
	print('Allen有幾', Allen_sticker_count,'個貼圖')
	print('Viki有幾',Viki_word_count,'字')
	print('Viki有幾', Viki_image_count,'張圖片')
	print('Viki有幾', Viki_sticker_count,'個貼圖')




#寫入檔案
def write_file(filename, lines):
	with open(filename,'w') as f:
		for line in lines :
			f.write(line+'\n')



def main():	
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#print(lines)
	#write_file('output.txt', lines)
main()