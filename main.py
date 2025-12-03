import os
import sys

# 지금은 에러 방지를 위해 try-except로 감싸둡니다.
try:
    import translator  # 번역 담당 파일
    import summarizer  # 요약 담당 파일
except ImportError:
    print("아직 없습니다.")
    pass

def read_text_file(file_path):
    """
    텍스트 파일(.txt)을 읽어서 내용을 문자열로 반환하는 함수
    """
    if not os.path.exists(file_path):
        print(f"[Error] 파일을 찾을 수 없습니다: {file_path}")
        return None
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except Exception as e:
        print(f"[Error] 파일 읽기 오류: {e}")
        return None

def main():
    print("=== 3줄 요약 번역기 ===")
    
    # 1. 파일 입력 받기
    file_path = input("요약할 영어 기사 텍스트 파일을 입력하세요 (예: news.txt): ").strip()
    
    original_text = read_text_file(file_path)
    
    if not original_text:
        print("프로그램을 종료합니다.")
        return

    print("\n[1] 파일 읽기 성공!")
    print(f"내용 길이: {len(original_text)} 자")

    # 2. 번역 (팀원 B 파트)
    translated_text = "아직 번역 기능이 구현되지 않음"
    if 'translator' in sys.modules and hasattr(translator, 'translate_text'):
        print("\n[3] 번역 진행 중...")
        translated_text = translator.translate_text(summary_text)
    else:
        print("\n[Pass] 번역 모듈이 비어있습니다.")
    
    # 3. 요약 (팀원 C 파트)
    summary_text = "아직 요약 기능이 구현되지 않음" 
    if 'summarizer' in sys.modules and hasattr(summarizer, 'summarize_text'):
        print("\n[2] 요약 진행 중...")
        summary_text = summarizer.summarize_text(original_text)
    else:
        print("\n[Pass] 요약 모듈이 비어있습니다.")

    # 4. 결과 출력 및 저장
    print("-" * 30)
    print("[최종 결과]")
    print(translated_text)
    print("-" * 30)

    # 결과 파일 저장
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(translated_text)
    print("결과가 result.txt에 저장되었습니다.")

if __name__ == "__main__":
    main()