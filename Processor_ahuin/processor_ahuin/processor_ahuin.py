import json
import pandas as pd

def process_json_to_csv(json_file_path, csv_file_path='extracted_data.csv'):
    """
    从指定的JSON文件读取数据，提取特定字段，并将结果保存到CSV文件中。

    参数:
    - json_file_path: JSON文件的路径。
    - csv_file_path: 保存结果的CSV文件的路径（默认为'extracted_data.csv'）。
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 确定数据是可迭代的且不是简单的字符串或整数等
        if isinstance(data, dict):
            # 假设我们的目标数据在字典的某个键下，这里尝试找到它
            for key in data.keys():
                if isinstance(data[key], list):  # 确保这个键对应的是个列表
                    data = data[key]
                    break

        # 检查是否成功找到了列表数据
        if not isinstance(data, list):
            raise ValueError("未找到期望的列表数据结构。")

        extracted_data = [{
            'screen_name': item['screen_name'],
            'followers_count': item.get('followers_count', 0),
            'created_at': item.get('created_at', '')
        } for item in data if isinstance(item, dict)]

        df = pd.DataFrame(extracted_data)
        df.to_csv(csv_file_path, index=False, encoding='utf-8')
        print(f'数据已保存到 {csv_file_path}')

    except Exception as e:
        print(f"处理数据时发生错误：{e}")

# 可选：如果你希望直接运行此脚本进行测试或单独操作
if __name__ == "__main__":
    # 这里可以修改为你的测试JSON文件路径和输出CSV文件路径
    process_json_to_csv('path_to_your_json_file.json')
