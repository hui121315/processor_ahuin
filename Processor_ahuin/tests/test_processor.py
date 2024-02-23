import unittest
import pandas as pd
import json
import os
from processor_ahuin import process_json_to_csv


class TestProcessJsonToCsv(unittest.TestCase):
    def setUp(self):
        """测试前的准备工作"""
        self.test_json_file = 'test_data.json'
        self.expected_csv_file = 'expected_output.csv'
        self.test_output_csv = 'test_output.csv'
        
        # 创建一个测试用的JSON文件
        test_data = [
            {"screen_name": "user1", "followers_count": 100, "created_at": "2020-01-01"},
            {"screen_name": "user2", "followers_count": 150, "created_at": "2020-01-02"}
        ]
        with open(self.test_json_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(test_data))
        
        # 预期的CSV输出，用于比较
        expected_data = [
            {"screen_name": "user1", "followers_count": 100, "created_at": "2020-01-01"},
            {"screen_name": "user2", "followers_count": 150, "created_at": "2020-01-02"}
        ]
        df = pd.DataFrame(expected_data)
        df.to_csv(self.expected_csv_file, index=False)

    def tearDown(self):
        """测试后清理生成的文件"""
        os.remove(self.test_json_file)
        os.remove(self.expected_csv_file)
        os.remove(self.test_output_csv)

    def test_process_json_to_csv(self):
        """测试process_json_to_csv函数是否正确执行"""
        process_json_to_csv(self.test_json_file, self.test_output_csv)
        
        # 比较生成的CSV文件和预期的CSV文件
        generated_df = pd.read_csv(self.test_output_csv)
        expected_df = pd.read_csv(self.expected_csv_file)
        
        pd.testing.assert_frame_equal(generated_df, expected_df)

if __name__ == '__main__':
    unittest.main()
