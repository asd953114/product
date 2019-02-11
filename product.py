#讀取檔案
import os # operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			if "商品,價格" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name,price])
		return products

#讓使用者輸入

def user_input(products):
	while True:
		name = input("請輸入商品名稱: ")
		if name == "q":
			break
		price = input("請輸入商品價格: ")	
		prince = int(price)
		products.append([name, price])
	print(products)
	return products

#印出檔案

def print_products(products):
	for p in products:
		print(p[0], "的價格是", p[1])

#with 就是自動幫你close 因為在程式語言裡通常你打開檔案你就要關閉
#但大家很常忘記，所以python用了with幫你直接關閉

def write_file(filename, products):
	with open(filename, "w", encoding="utf-8") as f:  #w寫入模式 r讀取模式
		f.write("商品,價格\n")
		for p in products:
			f.write(p[0] + "," + str(p[1]) + "\n")



def main():
	filename = "products.csv"
	if os.path.isfile(filename): #檢察檔案在不在
		print("yeah!找到檔案了!")
		products = read_file(filename)
	else:
		print("找不到檔案....")

	products = user_input(products)
	print_products(products)
	write_file("products.csv", products)



main()

# refactor 把直接的城市重構成漂亮的function










