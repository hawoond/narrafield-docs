# Narrafield Studio · 소개와 제작 가이드

제품 **Narrafield Studio** · **sortie**

내러필드 스튜디오는 예제로 쉽게 시작하고, 장면과 선택지를 연결해 나만의 이야기를 게임으로 완성하는 TRPG 엔진입니다. 이 공개 저장소는 제품 소개와 한국어·영어 사용 가이드를 제공합니다.

- [제품 소개](https://narrafield.com/)
- [제작기 메뉴별 안내](https://narrafield.com/EDITOR.html)
- [한국어 제작 가이드](https://narrafield.com/WIKI.html)
- [English creator guide](https://narrafield.com/en/WIKI.html)
- [새 기획과 화면 시안](https://narrafield.com/DESIGN.html)
- [현재 지원 범위](DEVELOPMENT.md)

사용법은 검토한 공개 데모를 기준으로 하며, `content_status: planned` 문서는 개발 목표와 시안을 설명합니다. `_data/review.yml`에 검토일·기획 버전·검증한 데모 버전을 기록합니다. 모든 가이드는 한국어와 영어로 제공하고 언어 탭으로 같은 문서를 전환합니다.

[데모 다운로드](https://narrafield.com/DEMO.html)에서 현재 개발용 알파를 제공합니다. 데모 ZIP은 공개 릴리스의 첨부 파일로 게시하고 `_data/demo.yml`에서 버전·다운로드 주소·파일 크기·SHA-256을 관리합니다. 정식 제품은 **스토어 공개 예정**이며, 공식 제품 페이지가 공개되면 `_data/stores.yml`에 이름과 HTTPS 주소를 추가합니다.

## GitHub Pages 게시

**Settings → Pages → GitHub Actions**를 선택합니다. `main` 변경 시 Jekyll 빌드, 문서·이미지·링크 검사, Pages 배포를 차례로 수행합니다. Pull request에서는 빌드와 검사만 실행합니다.

## 문서 관리

문서 원본은 제작 프로젝트에서 관리하며, 검토한 공개 파일만 이 저장소에 반영합니다. 한국어 문서는 루트, 영어 문서는 `en/`에 같은 파일 이름으로 관리합니다. 제품 소개는 `index.html`, 위키 홈은 `WIKI.md`, 목차는 `_data/navigation.yml`, 공통 번역은 `_data/ui.yml`에 있습니다. 문서 링크는 같은 언어 폴더의 `.md`로 작성하면 Jekyll이 HTML 주소로 변환합니다. 두 언어를 함께 갱신하고 언어 탭으로 서로 이동되는지 확인하세요.

이 저장소에서 받은 문서 수정 제안은 원본에도 반영해 다음 업데이트에서 유지하세요. 애플리케이션 소스, 개발 기획, 바이너리와 프로젝트 데이터는 이 저장소의 관리 대상에 포함되지 않습니다.

항구 일러스트는 콘셉트 아트입니다. 이전 개발 알파의 실제 앱 화면과 최신 제작기·플레이 화면 시안을 캡션으로 구분합니다. 시안은 데모 기능의 구현 완료를 의미하지 않습니다.
