from openai import OpenAI
import json

api_key = "my_key" 

client = OpenAI(
    api_key='my_key'

)

### 프롬프트 
# 사전 요약본
summary_data = """
### 도파민: 뇌의 다재다능한 신경전달물질

도파민은 신경계에서 중요한 역할을 하는 신경전달물질로, 다양한 인지 및 정서적 기능에 깊이 관여합니다. 두 개의 도파민 관련 문서를 종합하여 도파민의 전반적인 역할과 뇌에서의 기능, 그리고 인지 및 정서적 기능에 미치는 영향을 포괄적으로 요약하겠습니다.

#### 도파민의 역할

도파민은 주로 보상, 동기 부여, 감정 조절, 학습 및 기억과 같은 다양한 기능에 관여합니다. 도파민 시스템은 뇌의 여러 부위에 걸쳐 있으며, 각 부위에서 서로 다른 역할을 수행합니다. 도파민은 특히 보상 시스템에서 중요한 역할을 하며, 이는 우리가 특정 행동을 반복하도록 동기 부여하는 데 기여합니다.

#### 뇌에서의 도파민 기능

도파민은 뇌의 여러 부위에서 작용하며, 각 부위에서의 기능은 다음과 같습니다:

1. **기저핵 (Basal Ganglia)**: 기저핵은 운동 조절과 관련이 있으며, 도파민은 이 부위에서 운동 기능을 조절하는 데 중요한 역할을 합니다. 파킨슨병과 같은 운동 장애는 기저핵에서 도파민의 결핍으로 인해 발생합니다.

2. **전두엽 (Prefrontal Cortex)**: 전두엽은 고차원적인 인지 기능, 의사결정, 계획 및 사회적 행동을 조절합니다. 도파민은 전두엽에서 이러한 인지 기능을 조절하며, 도파민의 불균형은 ADHD와 같은 주의력 결핍 장애와 관련이 있습니다.

3. **중뇌 (Midbrain)**: 중뇌의 도파민 뉴런은 보상 시스템의 핵심 요소로, 보상과 동기 부여에 중요한 역할을 합니다. 중뇌에서 분비된 도파민은 쾌락과 보상을 경험하게 하며, 이는 중독과 관련이 있습니다.

4. **변연계 (Limbic System)**: 변연계는 감정 조절과 관련이 있으며, 도파민은 이 부위에서 감정의 조절과 스트레스 반응에 관여합니다. 도파민의 불균형은 우울증과 같은 정서적 장애와 관련이 있습니다.

#### 도파민의 인지 및 정서적 기능

도파민은 학습과 기억에도 중요한 역할을 합니다. 도파민은 새로운 정보를 학습하고 기억을 형성하는 과정에서 시냅스 가소성을 촉진합니다. 또한, 도파민은 감정 조절에 중요한 역할을 하며, 긍정적 감정과 부정적 감정을 모두 조절합니다. 도파민의 불균형은 우울증, 불안, 조울증 등 다양한 정서적 장애와 관련이 있습니다.

#### 도파민과 관련된 최신 연구

최근 연구에 따르면, 도파민은 단순히 보상과 동기 부여에만 관여하는 것이 아니라, 사회적 상호작용과 공감 능력에도 중요한 역할을 한다는 것이 밝혀졌습니다. 또한, 도파민 수용체의 유전적 변이가 개인의 성격 특성과 관련이 있을 수 있다는 연구 결과도 있습니다. 예를 들어, 도파민 D4 수용체 유전자의 변이는 모험심과 관련이 있는 것으로 나타났습니다.

#### 결론

도파민은 뇌의 여러 부위에서 다양한 기능을 수행하는 중요한 신경전달물질입니다. 도파민은 보상, 동기 부여, 감정 조절, 학습 및 기억에 중요한 역할을 하며, 도파민 시스템의 불균형은 다양한 신경정신과적 장애와 관련이 있습니다. 최신 연구는 도파민이 사회적 상호작용과 공감 능력에도 중요한 역할을 한다는 것을 시사하며, 도파민의 역할에 대한 이해는 계속해서 확장되고 있습니다.
"""

# 활동
prompt_activity = """
당신은 뇌 과학 전문가입니다. 사용자가 입력한 활동 목록에 대해 도파민 자극의 긍정적 또는 부정적 영향을 평가하고, 각 활동에 대한 근거와 점수를 제공하세요. 특히, 긍정적 도파민 자극을 유도하는 활동의 중요성을 강조하여 설명해 주세요. 최종적으로 **흰 늑대(긍정적 도파민 자극)**와 **검은 늑대(부정적 도파민 자극)** 점수를 계산한 후, **오직 JSON 형식**으로 결과를 반환하세요. 절대로 추가 설명을 하지 마세요. 오직 JSON 형식만 출력하세요.

다음은 도파민과 관련된 문서입니다. 이 문서들을 바탕으로 아래 내용을 수행하세요.

**문서** : {summary_data}

모든 작업은 한국어로 작성하세요.

### 작업 과정:
1. 각 활동이 도파민에 긍정적인지, 부정적인지 판단하십시오. 긍정적 도파민 자극은 장기적인 뇌 건강과 정서적 안정을 촉진하는 활동입니다. 활동이 **도파민의 신경 가소성을 향상**시키거나 **스트레스를 감소**시키는 경우, 긍정적 도파민 자극으로 분류하십시오.
2. 활동이 뇌의 장기적 건강과 도파민 시스템에 미치는 영향을 근거로 평가하십시오. 연구에 따라 도파민의 긍정적 자극과 관련된 활동에 대해 높은 점수를 부여하십시오.
3. 각 활동의 도파민 자극 정도에 따라 **흰 늑대 점수(긍정적 도파민 자극)**와 **검은 늑대 점수(부정적 도파민 자극)**로 나누어 점수를 부여하십시오. 긍정적 활동의 점수를 더 높게 부여할 수 있습니다.

사용자가 입력한 활동 목록:
{activities}

최종적으로, **오직 JSON 형식으로** 아래 형식에 맞추어 결과를 출력하십시오. 절대 다른 설명을 추가하지 마세요.
출력에 ''''''으로 감싸지 마세요.
예시는 다음과 같습니다.
{{
  "userId": "{userId}",
  "사용자": {{
    "흰 늑대 총 점수": 7,
    "검은 늑대 총 점수": 12,
    "활동 분석": [
      {{
        "활동": "유튜브 시청 2시간",
        "도파민 자극": "부정적",
        "흰 늑대 점수": 0,
        "검은 늑대 점수": 6,
        "근거": "유튜브 시청은 일시적으로 도파민을 자극하지만, 장기적으로 뇌의 보상 시스템에 부정적 영향을 줄 수 있습니다."
      }},
      {{
        "활동": "운동 1시간",
        "도파민 자극": "긍정적",
        "흰 늑대 점수": 3,
        "검은 늑대 점수": 0,
        "근거": "운동은 도파민 분비를 촉진하고 신경 가소성을 높여 뇌 건강과 정서적 안정을 유지하는 데 기여합니다."
      }},
      {{
        "활동": "독서 1시간",
        "도파민 자극": "긍정적",
        "흰 늑대 점수": 2,
        "검은 늑대 점수": 0,
        "근거": "독서는 인지 능력을 자극하고 도파민 시스템을 긍정적으로 자극하여 장기적인 뇌 건강에 이로울 수 있습니다."
      }},
      {{
        "활동": "비디오 게임 3시간",
        "도파민 자극": "부정적",
        "흰 늑대 점수": 0,
        "검은 늑대 점수": 6,
        "근거": "비디오 게임은 과도한 도파민 자극을 유도하여 중독성을 유발하고 장기적으로 부정적인 영향을 미칠 수 있습니다."
      }},
      {{
        "활동": "명상 30분",
        "도파민 자극": "긍정적",
        "흰 늑대 점수": 2,
        "검은 늑대 점수": 0,
        "근거": "명상은 스트레스를 줄이고 도파민 분비를 안정화시켜 정서적 안정을 도모합니다."
      }}
    ]
  }}
}}
"""

# 일기
prompt_diary = """
당신은 친절하고 전문적인 상담사 역할을 맡고 있습니다. 아래는 한 사용자의 오늘 하루 활동 기록과 일기입니다. 활동 기록과 일기를 분석하여, 사용자가 긍정적인 방향으로 나아갈 수 있도록 맞춤형 조언을 제공해 주세요. 조언은 항상 친절하고 긍정적이어야 하며, 실질적인 행동 계획과 응원의 말이 포함되어야 합니다. 조언은 다음을 포함해야 합니다:

- 사용자가 긍정적으로 느꼈던 부분에 대한 칭찬과 강화.

- 부정적이거나 개선할 수 있는 부분에 대한 현실적이고 실질적인 행동 계획.

- 내일 더 나은 하루를 보낼 수 있도록 실천 가능한 구체적인 제안.

- 마지막으로, 사용자에게 따뜻한 응원의 말로 마무리해 주세요.

- 조언은 2~3문장 이내로 간결하게 작성해 주세요.

사용자의 일기:
{{
    "userId": "{userId}",
    "diary": "{diary}"
}}

참고:

- 반드시 한국어로 작성해 주세요.

- 활동 기록과 일기를 바탕으로, 사용자에게 실질적으로 도움될 수 있는 맞춤형 조언을 제공해 주세요.

- 출력은 반드시 JSON 형식으로 작성되며, 다음과 같은 형식을 따라야 합니다.

- 출력에 ''''''으로 감싸지 마세요.

결과는 다음 형식으로 반환하세요:
{{
  "userId": "{userId}",
  "advice": "GPT가 제공하는 맞춤형 조언"
}}
"""

# GPT 응답 생성 함수
def get_completion(prompt, model='gpt-4o'):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content
  
# 점수 계산 함수
def calculate_weighted_scores_v2(w_score,b_score,weight=1.3):
    total_score = w_score + b_score

    if total_score == 0:
        raise ValueError("흰 늑대와 검은 늑대의 총 점수가 0입니다. 점수를 확인해 주세요.")

    white_scaled = (w_score / total_score) * 20
    black_scaled = (b_score / total_score) * 20

    # 가중치 계산
    weight_black = weight
    if black_scaled > white_scaled:
        black_final_score = black_scaled * weight_black
        white_final_score = white_scaled  
    else:
        black_final_score = black_scaled
        white_final_score = white_scaled
        
    return white_final_score,black_final_score
  

# 점수 계산 함수
def calculate_weighted_scores_v2(w_score,b_score,weight=1.3):
    total_score = w_score + b_score
    
    if total_score == 0:
        raise ValueError("흰 늑대와 검은 늑대의 총 점수가 0입니다. 점수를 확인해 주세요.")
    
    white_scaled = (w_score / total_score) * 20
    black_scaled = (b_score / total_score) * 20

    # 가중치 계산
    weight_black = weight
    if black_scaled > white_scaled:
        black_final_score = black_scaled * weight_black
        white_final_score = white_scaled  
    else:
        black_final_score = black_scaled
        white_final_score = white_scaled
    return white_final_score,black_final_score

# 활동 분석 함수
def analyze_activities(user_id, activities):
    activities_json = json.dumps(activities, ensure_ascii=False, indent=4)
    formatted_prompt_act = prompt_activity.format(
        userId=user_id,
        activities=activities_json,
        summary_data=summary_data
    )
    response_activity = get_completion(formatted_prompt_act)
    try:
        data = json.loads(response_activity)
        w_score = int(data["사용자"]["흰 늑대 총 점수"])
        b_score = int(data["사용자"]["검은 늑대 총 점수"])
        w_final,b_final=calculate_weighted_scores_v2(w_score,b_score,weight=1.3)
        data["사용자"]["흰 늑대 총 점수"]=int(w_final)
        data["사용자"]["검은 늑대 총 점수"]=int(b_final)
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON decoding error in analyze_activities: {e}")


# 일기 분석 함수
def analyze_diary(user_id, diary):
    formatted_prompt_diary = prompt_diary.format(
        userId=user_id,
        diary=diary
    )
    response_diary = get_completion(formatted_prompt_diary)
    try:
        return json.loads(response_diary)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON decoding error in analyze_diary: {e}")
