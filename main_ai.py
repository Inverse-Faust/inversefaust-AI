# main_ai.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from sentiment_analysis import SentimentAnalyzer
from prompt_main import analyze_activities, analyze_diary

# FastAPI 앱 초기화
app = FastAPI()

# 감성 분석기 초기화
analyzer = SentimentAnalyzer()

# 활동 데이터 모델 정의
class Activity(BaseModel):
    activity: str
    duration: float  # 활동 시간 (시간 단위)

# 활동 요청 데이터 모델 정의
class ActivitiesRequest(BaseModel):
    userId: str
    activities: List[Activity] = Field(..., description="활동 목록")
    
# 일기 요청 데이터 모델 정의
class DiaryRequest(BaseModel):
    userId: str
    diary: str

# 엔드포인트 활동부분
@app.post("/api/v1/ai")
async def analyze_activities_endpoint(entry: ActivitiesRequest):
    try:
        # 활동 및 일기 분석 결과 가져오기
        activities_data = [activity.dict() for activity in entry.activities]
        activity_advice = analyze_activities(entry.userId, activities_data)

        # 응답 반환
        return {
            "userId": entry.userId,
            "white_score": activity_advice["사용자"]["흰 늑대 총 점수"],
            "black_score": activity_advice["사용자"]["검은 늑대 총 점수"]
        }
    except ValueError as e:
        # JSON decoding 에러 처리
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        # 기타 예외 처리
        raise HTTPException(status_code=500, detail=str(e))

#엔드포인트 첨언부분
@app.post("/api/v2/ai/")
async def analyze_diary_endpoint(entry: DiaryRequest):
    try:
        # 감정 분석 수행
        sentiment_score = analyzer.analyze_sentence(entry.diary)

        # 감정 점수를 통해 감정 분류
        sentiment = "긍정" if sentiment_score > 0 else "부정" if sentiment_score < 0 else "중립"

        # 활동 및 일기 분석 결과 가져오기
        diary_advice = analyze_diary(entry.userId, entry.diary)

        # 응답 반환
        return {
            "userId": entry.userId,
            "diary_sentiment": sentiment,
            "diary_score": sentiment_score,
            "diary_advice": diary_advice["advice"]
        }
    except ValueError as e:
        # JSON decoding 에러 처리
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        # 기타 예외 처리
        raise HTTPException(status_code=500, detail=str(e))
    
#엔드포인트 초기버전(잠시 대기)
"""
@app.post("/api/advice/ai/")
async def analyze_journal(entry: JournalRequest):
    try:
        # 감정 분석 수행
        sentiment_score = analyzer.analyze_sentence(entry.diary)

        # 감정 점수를 통해 감정 분류
        sentiment = "긍정" if sentiment_score > 0 else "부정" if sentiment_score < 0 else "중립"

        # 활동 및 일기 분석 결과 가져오기
        activities_data = [activity.dict() for activity in entry.activities]
        activity_advice = analyze_activities(entry.userId, activities_data)
        diary_advice = analyze_diary(entry.userId, activities_data, entry.diary)

        # 응답 반환
        return {
            "userId": entry.userId,
            "white_score": activity_advice["사용자"]["흰 늑대 총 점수"],
            "black_score": activity_advice["사용자"]["검은 늑대 총 점수"],
            "diary_sentiment": sentiment,
            "diary_score": sentiment_score,
            "diary_advice": diary_advice["advice"]
        }
    except ValueError as e:
        # JSON decoding 에러 처리
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        # 기타 예외 처리
        raise HTTPException(status_code=500, detail=str(e))
    
"""
# 서버 실행 명령: `uvicorn main_ai:app --reload`
