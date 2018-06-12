"""
言語処理１００本ノック
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1
第一章　準備運動
"""


def knock00():
	string = "stressed"
	return string[:: -1]


def knock01():
	string = "パタトクカシーー"
	result = ''
	for i in range(0, 7, 2):
		result += string[i]
	return result


def knock02():
	string1 = "パトカー"
	string2 = "タクシー"
	result = ''
	for i in range(0, 4):
		result += string1[i]
		result += string2[i]
	return result


def knock03():
	string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
	string = string.replace('.', "")
	string = string.replace(',', "")
	str_list = string.split(' ')
	str_value = []
	for value in str_list:
		str_value.append(len(value))
	return str_value


def knock04():
	string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
	values = (1,5,6,7,8,9,15,16,19)
	word_list = string.split(' ')
	result = {}
	for (i, word) in enumerate(word_list, 1):
		if i in values:
			result.update({word[0:1]: i})
			print(str(i) + ' ' + word[0:1])
		else:
			result.update({word[0:2]: i})
			print(str(i) + ' ' + word[0:2])
		
	return result
