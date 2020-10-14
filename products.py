#讀取檔案
product = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #繼續、跳過一次迴圈 只能寫在迴圈裡
		name, price = line.strip().split(',')#先strip去除空行 再以split切割 以','為切割的依據完成結果為清單
		product.append([name, price])
print(products)

#讓使用者輸入
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

#印出所有購買紀錄
for p in product:
	print(p[0], '的價格是', p[1])

#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'
# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')#添加欄位名稱
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')

#作業
data = [1,2,3,4,5,6]
with open('test.csv', 'w') as k:
	for d in data:
		k.write(str(d) + '\n')