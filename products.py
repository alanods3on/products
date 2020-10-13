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

for p in product:
	print(p[0], '的價格是', p[1])

#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')

data = [1,2,3,4,5,6]
with open('test.csv', 'w') as k:
	for d in data:
		k.write(str(d) + '\n')