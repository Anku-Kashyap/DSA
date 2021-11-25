
def wordBreak(wordList, word):
	if word == '':
		return True
	else:
		wordLen = len(word)
		return any([(word[:i] in wordList) and wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)])

               
n = 4
B = ["rvwng" ,"lben" ,"tztspyafeu" ,"ejac" ,"fexqdkkpf" ,"yjteqkvdbo" ,"ffbwkmzaw" ,"vvdiidtl" ,"c" ,"zhw"
]
A = "vvdiidtlrvwngfexqdkkpfyjteqkvdbocfexqdkkpfvvdiidtlejacyjteq"
print(wordBreak(B,A))