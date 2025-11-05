## Modules

- **scratcher**

    用于爬取指定关键词的视频的弹幕，结果保存于`dataset/barrage`。


## Start

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