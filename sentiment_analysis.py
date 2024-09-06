from knusl import KnuSL  # 기존의 KnuSL 클래스를 불러옵니다.
from konlpy.tag import Okt  # 한국어 형태소 분석을 위해 Konlpy 사용

class SentimentAnalyzer:
    def __init__(self):
        self.ksl = KnuSL()  # KnuSL 감정 사전을 초기화
        self.okt = Okt()  # 형태소 분석기를 초기화

    def analyze_sentence(self, sentence):
        # 문장을 형태소 분석하여 명사와 동사 등의 주요 단어를 추출합니다.
        words = self.okt.nouns(sentence) + self.okt.morphs(sentence)
        
        score = 0  # 전체 문장의 감성 점수 초기화
        word_count = 0  # 감성 점수가 매겨진 단어의 수
        
        for word in words:
            if len(word) > 1:  # 단일 문자는 무시합니다.
                root, polarity = self.ksl.data_list(word)
                if root != 'None':
                    score += int(polarity)  # 극성을 점수로 변환하여 합산
                    word_count += 1
        
        # 평균 점수 계산 (단어 수가 0인 경우 점수는 0으로 설정)
        avg_score = score / word_count if word_count > 0 else 0
        return avg_score
