import json
import os

# 감정 단어 사전 JSON 파일 경로 설정
input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'SentiWord_info.json')

class KnuSL:
    def __init__(self):
        # JSON 파일을 로드하여 감정 단어 데이터를 메모리에 저장
        with open(input_file_path, encoding='utf-8-sig', mode='r') as f:
            self.data = json.load(f)

    def data_list(self, wordname):
        # 단어가 감정 사전에 있는지 확인하고 결과를 반환
        result = ['None', 'None']
        for entry in self.data:
            if entry['word'] == wordname:
                result = [entry['word_root'], entry['polarity']]
                break
        
        return result  # 어근과 극성을 반환