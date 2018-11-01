# 座席数を配列で格納
a = [i+1 for i in range(5,10)]
# print(a)

count=0

print(a)
# あが全員座った後、3人が2番目から座るときの着席番号3+2-1=4(着席番号の求め方ab[0][0]+ab[0][1]-1)
# for i in range(2,2+3-1+1):
# 	a.remove(i)
# 	count+=1
# print(a)
# print(count)

# for i in range(6,6+1-1+1):
# 	a.remove(i)
# 	count+=1
# print(a)
# print(count)

# for i in range(5,5+2-1+1):
# 	a.remove(i)
# 	count+=1
# print(a)
# print(count)

# ↑このパターンが現れたら、二重ループ

# セットの全要素が指定したオブジェクトに含まれているかどうかを調べる

# リストからリストを削除するアルゴリズム
r = [j for j in range(2,2+3)]
k = [j for j in range(6,6+1)]
l = [j for j in range(5,6+1)]


print(r)
print(k)
print(l)



for i in range(len(ab)):
	ab[i][0],ab[i][1] = map(int,input().split())
	
	c = [j for j in range(ab[i][1],ab[i][0]+ab[i][1])]
	
	if(zaseki.issuperset(c)):
		
		zaseki.remove(c)

# 全セットに含まれるかを調べる
http://www.isl.ne.jp/pcsp/python/python17.html



	print(c)




# def dellist(items, indexes):
#     for index in indexes:
#     	del items[index]


# dellist(r,a)


# 着席している番号を配列に格納c = 2,3,4
# 座席番号リストから値を削除
# 削除できるなら

# 着席人数にカウント






# い　ひとりが6番目(ab[1][1])から座る1+6-1=6(ab[1][0]+ab[1][1]-1)
# 6番目に人が着席しているかどうかを確認
# 着席している→終了
# 着席していない→座る 着席人数にカウント
# 着席している番号を格納d = 6

# う　ふたりが5番目(ab[2][1])から座る2+5-1=6(ab[2][0]+ab[2][1]-1)
# 5番目の席に着席しているひとがいないかどうかを確認
# 着席していない→座る
# 座席番号を格納e=5,6
# この座席番号の中に座席番号配列に格納済みのデータがあったら、終了
# なければ着席人数にカウント
# 着席している→終了





# for i in range(len(ab)):
# 	ab[i][0] = input()
# 	ab[i][1] = input()
	
# 	print(ab[i][0])
# 	print(ab[i][1])







# i+1行目
# a_i(グループの人数)　b_i(着席開始座席番号)







# 出力
#最後のグループが座りにきたあと、無事に着席できている人数





