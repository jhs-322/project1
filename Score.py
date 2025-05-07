import re
import json


def main():
        
    output_file = "final.txt"
    
    while(True):
        try:
            input_file = input("분석할 파일 경로를 입력하세요: ")
            with open(input_file, "r", encoding="utf-8") as f:
                content = f.read()
                break
        except FileNotFoundError:
            print("존재하지 않는 파일입니다. 다시 시도해주세요.")
        except Exception as e:
            print(f"[!] 파일 열기 실패 : {e}")

    chunks = re.split(r"\[조각 \d+ 결과\]", content)

    extracted = []

    for chunk in chunks:
        try:
            json_match = re.search(r"```json(.*?)```", chunk, re.DOTALL)
            if not json_match:
                continue

            json_text = json_match.group(1).strip()
            data = json.loads(json_text)

            # "crypto"가 포함된 키를 모두 찾는다
            for key in data:
                if "crypto" in key.lower() and data[key]:  # 비어있지 않음 확인
                    extracted.append(json.dumps(data[key], ensure_ascii=False, indent=2))

        except Exception as e:
            continue  # JSON 오류, 키 오류 등은 무시

    # 결과 저장
    with open(output_file, "w", encoding="utf-8") as f:
        for e in extracted:
            f.write(e + "\n\n")

    # 위험도 평가 출력

    print("\n[최종 결과]")
    print(f"{len(extracted)}개의 위험요소가 발견되었습니다 : {output_file}")
    if len(extracted) >= 3:
        print("🔴 [고위험] cryptojacking 시도 중인 사이트입니다. 🔴")
    elif len(extracted) >0:
        print("🟡 [위험] cryptojacking 시도 중인 사이트일 가능성이 높습니다. 🟡")
    elif len(extracted)==0:
        print("🟢 [안전] 감지된 cryptojacking 요소가 없습니다. 🟢")