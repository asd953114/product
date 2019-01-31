
products = []

while True:
    name = input("請輸入商品名稱: ")
    if name == "q":
    	break
    price = input("請輸入商品價格: ")	
    prince = int(price)
    products.append([name, price])



print(products)

for p in products:
	print(p[0], "的價格是", p[1])
#with 就是自動幫你close 因為在程式語言裡通常你打開檔案你就要關閉
#但大家很常忘記，所以python用了with幫你直接關閉
with open("products.csv", "w", encoding="utf-8") as f:  #w寫入模式 r讀取模式
	f.write("商品,價格\n")
	for p in products:
		f.write(p[0] + "," + str(p[1]) + "\n")