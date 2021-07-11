#讀取檔案
products = []

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