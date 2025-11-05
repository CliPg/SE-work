## Modules

- **scratcher**

    用于爬取指定关键词的视频的弹幕，结果保存于`dataset/barrage`。

- **vocab_generator**
    
    使用jieba对弹幕进行分词。

- **vocab_distiller**

    使用LLM/sentence_transformer筛选与ai技术应用相关的弹幕。


## Start

- **环境配置**

    ```
    pip install -r requirements
    ```

- **爬取弹幕**
    ```
    cd models
    python -m scratcher
    ```

- **对弹幕进行分词**
  ```
  cd models
  python -m vocab_generator
  ```

- **对弹幕进行蒸馏**
    提供用sentence_transformer和LLM自动筛选两种方式。
    ```
    python -m vocab_distiller [llm | sentence]
    ```
    如需使用LLM，需要在系统配置你的阿里云大模型的API_KEY或直接在vocab_distiller进行修改。

- **生成词云**
  ```
  python -m wordcloud_generator