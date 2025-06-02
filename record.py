import os
import subprocess
import io
import RPi.GPIO as GPIO
from google.cloud import speech

# 1. 녹음할 파일 이름
wav_path = "recorded.wav"


def get_mic_device():
    result = subprocess.run("arecord -l" , shell = True , capture_output= True , text= True)
    output = result.stdout

    lines = output.splitlines()
    for line in lines:
        if 'card' in line:
            card_number = line.split()[1]
            card_number = card_number.split(':')[0]
            return f"plughw:{card_number},0"

    return None 
# 2. 녹음 (arecord 사용: 16bit, 16kHz, Mono, 8초)
# print(get_mic_device())

print("8초간 녹음 시작...")
subprocess.run([
    "arecord",
    "-D", get_mic_device(),      # USB 마이크에 맞게 수정
    "-f", "S16_LE",          # 16-bit
    "-r", "16000",           # 샘플레이트
    "-c", "1",               # 모노
    "-d", "8",               # 8초간 녹음
    wav_path
])

print("녹음 완료, STT 요청 중...")
# # 3. Google 인증 키 환경변수
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/capstone/project/aei-2024-cae3d9acf5b5.json"
# client = speech.SpeechClient()

# # 4. 녹음된 wav 파일 읽기
# with io.open(wav_path, "rb") as f:
#     content = f.read()

# audio = speech.RecognitionAudio(content=content)

# # 5. STT 요청 설정
# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=16000,
#     language_code="ko-KR"
# )

# # 6. 요청 및 결과 저장
# response = client.recognize(config=config, audio=audio)

# with open("/home/capstone/결과.txt", "a", encoding="utf-8") as f:
#     for result in response.results:
#         transcript = result.alternatives[0].transcript
#         print("인식 결과:", transcript)
#         f.write(transcript + "\n")

# os.system("python3 /home/capstone/project/koelectra_small.py")
# os.system("python3 /home/capstone/project/button_control.py")
