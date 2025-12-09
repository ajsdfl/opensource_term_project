"""
main.py

- 영어 뉴스 기사 텍스트를 입력받아
  1) translator.py로 한글 번역
  2) summarizer.py로 한글 3줄 요약

실행:
    python main.py
"""

from summarizer import summarize_text
from translator import translate_text


def load_article(path: str) -> str:
    """텍스트 파일에서 기사 내용 읽기"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def save_summary(path: str, summary: str):
    """요약 결과 저장"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(summary)


if __name__ == "__main__":
    # 1. 영어 기사 파일 입력
    article_path = input("영어 뉴스 기사 파일명을 입력하세요 (예: news.txt): ").strip()
    article_text = load_article(article_path)

    if not article_text.strip():
        print("❌ 기사 파일을 찾을 수 없거나 내용이 비어 있습니다.")
        raise SystemExit

    # 2. 한글 번역
    print("\n[1/2] 기사 번역 중...")
    translated_text = translate_text(article_text)

    # 💡 추가된 부분: 번역된 기사 출력
    print("\n=== 번역된 기사 (한국어) ===")
    print(translated_text)
    print("=============================")

    # 3. 한글 3줄 요약
    print("\n[2/2] 3줄 요약 중...")
    summary = summarize_text(translated_text, num_sentences=3)

    # 4. 결과 출력
    print("\n=== 3줄 요약 결과 ===")
    print(summary)

    # 5. 결과 저장
    save_summary("summary.txt", summary)
    print("\n✅ summary.txt 파일로 저장 완료")