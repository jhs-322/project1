from UrlLoader import MakeFileByUrl
from Clovax import main as clova_main
from Score import main as score_main

if __name__== "__main__":
    # JS 추출하고 - 링크 입력받아서 진행
    mfb = MakeFileByUrl()
    mfb.get_url()
    mfb.make_folder()
    mfb.download_file()
    mfb.extract_js()
    mfb.combine_js()
    # AI 난독화 복호화와 정적분석 - 파일 입력받아서 진행
    clova_main()
    # 점수제 - 파일 입력받아서 체크
    score_main()
    # 자동 종료 방지
    input("\n창을 닫으려면 엔터 키를 누르세요.") 