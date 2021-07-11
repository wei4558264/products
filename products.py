#讀取檔案
products = []
with open('products.csv','r',encoding='utf-8') as f:
	for line in f:
		if '水果,價錢' in line:
			continue
		name, price= line.strip().split(',')
		products.append([name, price])
print(products)

#使用者輸入資料
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入價錢:')
	products.append([name, price])
print(products)

#寫入檔案
with open('products.csv', 'w',encoding='utf-8') as f:
	f.write('水果,價錢\n')
	for p in products:
		f.write(p[0] + ',' +  p[1] + '\n')