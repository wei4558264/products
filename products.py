import os # operating system 
products = []

if os.path.isfile('products.csv'):
	print('太好了!檔案存在呢!')
	with open('products.csv','r',encoding='utf-8-sig') as f:
		for line in f:
			if '水果,價錢' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)
else:
	print("糟糕...要重新輸入檔案")

#使用者輸入資料
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入價錢:')
	price = int(price)
	products.append([name, price])
print(products)

#列出水果價錢
for p in products:
	print(p[0], '的價錢是:', p[1], '元')

#寫入檔案
with open('products.csv', 'w',encoding='utf-8') as f:
	f.write('水果,價錢\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')