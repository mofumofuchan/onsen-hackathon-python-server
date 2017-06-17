import MeCab

class SentimentAnalyser(object)
    text = "こんにちは。とてもうれしいことが起こりました。本当にびっくりです。うれしい"
    nouns, verbs, adjs, advs = [], [], [], []
    nounswords, verbswords, adjswords, advswords = [], [], [], []
    nounspoint, verbspoint, adjspoint, advspoint = [], [], [], []
 
    def analyze(hinsi, words, point, score, number):
        for i in hinsi:
            cnt = 0
            for j in words:
                if i == j:
                    score += float(point[cnt])
                    number += 1
                cnt += 1
        return score, number

    def __call__(self, text):
        f = open('pn_ja.dic.txt', 'r')
        for line in f:
            line = line.rstrip()
            x = line.split(':')
            if abs(float(x[3]))>0:
                if x[2] == '名詞':
                    nounswords.append(x[0])
                    nounspoint.append(x[3])
                if x[2] == '動詞':
                    verbswords.append(x[0])
                    verbspoint.append(x[3])
                if x[2] == '形容詞':
                    adjswords.append(x[0])
                    adjspoint.append(x[3])
                if x[2] == '副詞':
                    advswords.append(x[0])
                    advspoint.append(x[3])
        f.close()
 
        tagger = MeCab.Tagger('-Ochasen')
        node = tagger.parseToNode(str(text))
        while node:
            if node.feature.split(",")[0] == '名詞':
                nouns.append(node.surface)
            if node.feature.split(",")[0] == '動詞':
                verbs.append(node.surface)
            if node.feature.split(",")[0] == '形容詞':
                adjs.append(node.surface)
            if node.feature.split(",")[0] == '副詞':
                advs.append(node.surface)
            node = node.next
 
        score = number = 0
        score, number = analyze(nouns,nounswords,nounspoint,score,number)
        score, number = analyze(verbs,verbswords,verbspoint,score,number)
        score, number = analyze(adjs,adjswords,adjspoint,score,number)
        score, number = analyze(advs,advswords,advspoint,score,number)
        if number > 0:
            print(score/number)
