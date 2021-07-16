import os # operating system
products = [] 
#讀取資料
def read_in(datafile):	
	if os.path.isfile(datafile):
		print('太好了!檔案存在呢!')
		with open(datafile,'r',encoding='utf-8-sig') as f:
			for line in f:
				if '早餐,價錢' in line:
					continue
				name, price = line.strip().split(',')
				products.append([name,price])
		
		
	else:
		print("糟糕...要重新輸入檔案")
	return products

#使用者輸入資料
def input_data(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入價錢:')
		price = int(price)
		products.append([name, price])
	
	return products

#列出水果價錢
def print_data(products):
	for p in products:
		print(p[0], '的價錢是:', p[1], '元')

#寫入檔案
def write_in_data(datafile,products):
	with open(datafile, 'w',encoding='utf-8') as f:
		f.write('早餐,價錢\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')
#主檔案
oldfile = 'products.csv'
products = read_in(oldfile)
products = input_data(products)
print_data(products)
write_in_data(oldfile,products)

