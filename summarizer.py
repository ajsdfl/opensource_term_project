from transformers import pipeline

# 모델 입력의 최대 길이를 늘려 기사와 같은 긴 텍스트 처리를 용이하게 합니다.
# KoBART 모델의 일반적인 최대 입력 토큰 길이인 1024로 설정합니다.
MAX_INPUT_LENGTH = 1024

print("[Summarizer] 요약 모델 로딩 중...")

try:
    # 파이프라인 설정 시 max_length를 늘려 긴 텍스트 입력 지원
    summarizer_pipeline = pipeline(
        "summarization",
        model="digit82/kobart-summarization",
        max_length=MAX_INPUT_LENGTH  # 입력 토큰 최대 길이 설정 (인코더)
    )
except Exception as e:
    print(f"[Critical Error] 요약 모델 로드 실패: {e}")
    summarizer_pipeline = None


def summarize_text(text, num_sentences=3):
    """
    한글 텍스트(기사)를 입력받아 num_sentences줄 요약
    """

    if summarizer_pipeline is None:
        return "오류: 요약 모델이 로드되지 않았습니다."

    if not text or not isinstance(text, str):
        return "오류: 요약할 텍스트가 없습니다."

    try:
        result = summarizer_pipeline(
            text,
            max_new_tokens=150,  # 생성될 요약문의 최대 토큰 수
            min_length=30,       # 최소 길이 설정 (너무 짧은 요약 방지)
            do_sample=False
        )

        summary = result[0]["summary_text"]

        lines = summary.replace("다.", "다.\n").splitlines()
        
        # 빈 줄 제거 후, 원하는 문장 수만큼 반환
        filtered_lines = [line.strip() for line in lines if line.strip()]
        return "\n".join(filtered_lines[:num_sentences])

    except Exception as e:
        return f"요약 중 오류 발생: {e}"
