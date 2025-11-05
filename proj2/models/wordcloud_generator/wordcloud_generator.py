import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(input_file: str, output_file: str = "wordcloud.png"):
    # 读取词表 
    freq_dict = {}
    with open(input_file, "r", encoding="utf-8") as f:  # 改成你的文件名
        for line in f:
            data = json.loads(line.strip())
            word = data["word"]
            freq = data["frequency"]
            freq_dict[word] = freq

    # 生成词云 
    wordcloud = WordCloud(
        font_path="/System/Library/Fonts/STHeiti Medium.ttc",  # macOS 中文字体
        # Windows 可改为：font_path="C:/Windows/Fonts/simhei.ttf"
        background_color="white",
        width=1000,
        height=600,
        max_words=200,
        colormap="viridis"
    ).generate_from_frequencies(freq_dict)

    # 显示词云
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    # 保存为文件
    wordcloud.to_file(output_file)
    print("词云已保存为 wordcloud.png")