from transformers import pipeline

print("[Translator] 번역 모델(NLLB-200) 로딩 중...")

try:
    translator_pipeline = pipeline(
        "translation",
        model="facebook/nllb-200-distilled-600M",
        src_lang="eng_Latn",
        tgt_lang="kor_Hang"
    )
except Exception as e:
    print(f"[Critical Error] 모델 로드 실패: {e}")
    translator_pipeline = None


def translate_text(text):
    # 예외 처리
    if translator_pipeline is None:
        return "오류: 번역 모델이 로드되지 않았습니다."
    
    if not text or not isinstance(text, str):
        return "오류: 번역할 텍스트가 없습니다."

    if "구현되지 않음" in text:
        return text 

    lines = text.split('\n')
    translated_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped:
            try:
                result = translator_pipeline(
                    stripped,
                    max_length=512,
                    truncation=True
                )
                translated_lines.append(result[0]['translation_text'])
            except Exception as e:
                translated_lines.append(f"[번역 실패: {e}]")
        else:
            translated_lines.append("")

    return "\n".join(translated_lines)


# 단독 실행 테스트
if __name__ == "__main__":
    print(translate_text("System check complete. Ready for deployment."))
