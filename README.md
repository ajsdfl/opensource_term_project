# 영문 뉴스 3줄 요약 번역기

## 1. 프로젝트 개요
이 프로젝트는 영어로 된 긴 뉴스 기사를 입력받아, **한글로 번역**하고 **3줄로 요약**해주는 프로그램입니다.

## 2. 이미지/영상

## 3. 사용한 패키지 및 버전
* Python
* transformers
* torch
* sentencepiece

## 4. 실행 방법
이 프로젝트는 Python 환경에서 실행됩니다.

**1. 환경 설정 (패키지 설치)**
터미널을 열고 아래 명령어를 입력하여 필요한 라이브러리(`transformers` 등)를 설치합니다.
(pip install -r requirements.txt)

**2. 입력 파일 준비**
요약하고 싶은 영어 뉴스 기사나 텍스트를 복사하여 원하는 이름 파일로 저장합니다. 이 파일은 main.py와 같은 폴더에 있어야 합니다.

**3. 프로그램 실행**
터미널에 아래 명령어를 입력하여 프로그램을 시작합니다.
python main.py

**4. 파일 경로 입력**
프로그램이 실행되면 파일명을 묻는 메시지가 나옵니다. 아까 준비한 파일명(예: news.txt)을 입력하고 엔터를 누릅니다.

**5. 결과 확인**
잠시 기다리면 화면에 3줄 요약 및 한글 번역 결과가 출력됩니다. 같은 폴더에 result.txt 파일이 생성되어 결과를 저장합니다.

## 5. 참고 자료
이 프로젝트는 다음의 오픈소스 라이브러리와 사전 학습된 모델(Pre-trained Models)을 활용하여 제작되었습니다.

* **Hugging Face Transformers Library**
  * 공식 문서: https://huggingface.co/docs/transformers/index
  
* **사용 모델 (Models Used)**
  * 요약 모델 (Bart-Large-CNN): https://huggingface.co/facebook/bart-large-cnn
  * 번역 모델 (Opus-MT-En-Ko): https://huggingface.co/Helsinki-NLP/opus-mt-en-ko

* **Python Official Documentation**
  * https://docs.python.org/3/
