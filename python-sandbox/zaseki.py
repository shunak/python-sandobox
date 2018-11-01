# 入力
# 1行目
# n = 座席数　m = グループ数
# 一回だけ出力
# これらのデータを変数zgに格納
zg = input().rstrip().split(' ')

count=0
# print(zg)

# zg[1]の回数＝iとなる
# zg[1]の回数分、値が二次元配列として格納されればよい

# 配列定義ab(グループの配列を生成)
ab = [[0 for i in range(2)] for j in range(int(zg[1]))]


# print(len(ab))　len(ab)==3
# とりあえず入力した値を表示するプログラムを作成

# 座席数の取得
zaseki = set([i+1 for i in range(int(zg[0]))])

print(zaseki)
m = max(zaseki)
# print(m)

for i in range(len(ab)):
	ab[i][0],ab[i][1] = map(int,input().split())
	
	c = [j if j <= m else j-m for j in range(ab[i][1],ab[i][0]+ab[i][1])]

	print(c)
	
	if(zaseki.issuperset(c)):
		for k in range(ab[i][1],ab[i][0]+ab[i][1]):
			if k > m:
				zaseki.remove(k-m)
				count+=1
			else:
				zaseki.remove(k)
				count+=1
	else:
		continue

print(count)



# for j in range(ab[i][1],ab[i][0]+ab[i][1]):
# 		zaseki.discard(j)
# 		count+=1
# 		print(zaseki)
# 		print(count)


# discardは捨てた回数までカウントしてしまうので、
# 
# 違うアルゴリズムを考える必要があるかも
# リストからリストを削除するアルゴリズムを考えればいけるはず




# print(ab)	

# 座るための条件を割り出すアルゴリズム

# 着席している場所を表示
# 例
# 6 3
# ３２　あ
# １６　い
# ２５　う

# 座席数を配列で格納
# 







# あが全員座った後、3人が2番目から座るときの着席番号3+2-1=4(着席番号の求め方ab[0][0]+ab[0][1]-1)





# 着席している番号を配列に格納c = 2,3,4
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










