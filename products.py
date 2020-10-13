product = []
while True:
	name = input('請輸入你購買商品的名稱:')
	if name == 'q':
		break
	price = input('請輸入你購買商品的價格:')
	#p = [] 二維度清單
	#p.append(name)
	#p.append(price)
	#-p = [name, price]
	product.append([name, price])
print(product)

