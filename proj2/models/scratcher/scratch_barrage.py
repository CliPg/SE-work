from .video_scratcher  import search
from .barrage_extractor import barrage

import json
import random
import time
def scratch_barrage(output_file: str, keyword: str, num: int) -> int:
    """
    根据关键词抓取指定数量的视频弹幕并保存到文件

    Args:
        output_file (str): 输出 JSON 行文件路径
        keyword (str): 搜索关键词
        num (int): 想要获取的弹幕视频数量
    """
    search_instance = search(keyword, keep_open=False)
    count = 0
    for video_url in search_instance.query():
        print(f"正在解析 {video_url}")
        barrage_instance = barrage(video_url)
        if not barrage_instance.fetch():
            print("弹幕获取失败")
            continue

        count += 1
        barrage_data = barrage_instance.get()
        print(f"已获取 {len(barrage_data)} 条弹幕")

        # 追加写入
        with open(output_file, 'a', encoding='utf-8') as f:
            json.dump({
                "video_url": video_url,
                "barrages": barrage_data
            }, f, ensure_ascii=False)
            f.write("\n")  # 换行，保证每行一个 JSON 对象

        print(f"已完成 {count} 个视频的弹幕获取")

        if count >= num:
            print("已达到弹幕获取上限，程序结束")
            break

        time.sleep(random.uniform(6, 12))  # 模拟人类行为

    search_instance.stop()
    print("所有弹幕已保存")

    return count