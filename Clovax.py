# clovax_fullscan_oop.py
# 최종 - 이중 분석 모드 + 자동 재시도(backoff) 적용

from openai import OpenAI
import os
import time
import sys

# 안전하게 stdout, stderr reconfigure
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

class ClovaXScanner:
    def __init__(self, api_key, base_url="https://clovastudio.stream.ntruss.com/v1/openai/"):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.max_len = 2500
        self.final_result = []

    def load_file(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"   파일이 존재하지 않습니다: {filepath}")

        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            self.full_code = f.read()

        print(f"    읽은 파일 크기: {len(self.full_code)} bytes")
        self.chunks = [self.full_code[i:i+self.max_len] for i in range(0, len(self.full_code), self.max_len)]
        print(f"    총 {len(self.chunks)}개의 조각으로 분할 완료")

    def analyze_chunks(self):
        for idx, chunk in enumerate(self.chunks, 1):
            print(f"[{idx}/{len(self.chunks)}] 조각 이중 분석 중...")

            results = []
            for trial in range(2):
                retries = 0
                while retries < 5:
                    try:
                        response = self.client.chat.completions.create(
                            model="HCX-005",
                            messages=[
                                {
                                    "role": "system",
                                    "content": (
                                        "당신은 사이버 보안 전문가입니다. 주어진 JavaScript 안에서 - 난독화된 부분이 있으면 사람이 이해할 수 있도록 복원한 뒤, - 복원된 코드 안에서 **크립토재킹과 관련된 요소(예: 암호화폐 채굴, Coinhive, WebAssembly miner, Web Worker 채굴)** 만을 탐지해 주세요.결과는 다음과 같이 출력해 주세요: 1. 탐지된 항목만 JSON 형식으로 출력 (필요한 경우 파일명과 코드 조각 포함)\n2. 불필요한 설명, 해설 문장은 쓰지 마세요.3. 탐지된 항목이 없으면 빈 JSON `{}` 만 출력해 주세요.반드시 JSON 형식만 출력해야 합니다."
                                    )
                                },
                                {"role": "user", "content": chunk}
                            ]
                        )
                        result = response.choices[0].message.content.strip()
                        results.append(result)
                        print(f"    [시도 {trial+1}] 분석 완료")
                        break  # 성공했으니 루프 종료
                    except Exception as e:
                        print(f"    [시도 {trial+1}] 분석 실패 (재시도 {retries+1}): {e}")
                        if "429" in str(e) or "rate" in str(e).lower():
                            wait = 2 ** retries
                            print(f"      → 요청 제한 감지: {wait}초 대기 후 재시도")
                            time.sleep(wait)
                            retries += 1
                        else:
                            results.append(f"에러 발생: {e}")
                            break

                time.sleep(1)

            meaningful = [r for r in results if r.strip() not in ("{}", "", "에러 발생")]
            if meaningful:
                self.final_result.append(meaningful[0])
            else:
                self.final_result.append(results[0])

    def save_results(self, output_path="clovax_analysis_result.txt"):
        with open(output_path, "w", encoding="utf-8") as f:
            for idx, res in enumerate(self.final_result, 1):
                f.write(f"\n[조각 {idx} 결과]\n{res}\n")
        print(f"\n  분석 결과 저장 완료: {output_path}")

    def show_results(self):
        print("\n   전체 분석 결과:")
        for idx, res in enumerate(self.final_result, 1):
            print(f"\n[조각 {idx} 결과]")
            print(res)

def main():
    api_key = os.getenv("OPEN_API_KEY")
    scanner = ClovaXScanner(api_key)

    malicious_code_path = input("   분석할 파일 이름을 입력하세요 (예: combined.js1): ").strip()

    try:
        scanner.load_file(malicious_code_path)
        scanner.analyze_chunks()
        scanner.show_results()
        scanner.save_results()
    except Exception as e:
        print(f"     프로그램 중단: {e}")