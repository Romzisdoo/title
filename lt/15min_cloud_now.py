from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"15min_now.csv", encoding ="UTF-8")

comment_words = ''
stopwords = set(STOPWORDS)

for val in df.Tekstas:
	val = str(val)
	tokens = val.split()
	
	for i in range(len(tokens)):
		tokens[i] = tokens[i].lower()
	
	comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(width = 800, height = 800,
				background_color ='white',
				stopwords = stopwords,
				min_font_size = 10).generate(comment_words)
				
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("on")
plt.tight_layout(pad = 0)
plt.show()
