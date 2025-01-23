## 학식킹: 유학생을 위한 오늘의 학식 메뉴 설명 서비스

![image](https://github.com/user-attachments/assets/ead375d6-f91c-45f6-8f41-16a4ad3927b9)

학식킹은 유학생을 위한 학식 메뉴 알리미 서비스로, 음식에 대한 설명과 특정 재료(쇠고기, 닭고기, 돼지고기, 계란, 새우)의 포함 가능성에 대한 정보를 제공합니다.

## 주요 기능

### [주요기능 1] **학식 메뉴에 대한 자세한 설명**

학식킹은 오늘의 학식 메뉴를 단순히 번역할 뿐만이 아니라 **그 음식이 어떤 맛이 나는 음식인지, 어떤 종류의 음식인지**에 대한 설명을 상세히 제공합니다. 이를 통해 한국 음식이 익숙지 않은 유학생들이 한층 더 쉽게 학생식당과 한식에 접근할 수 있는 기회를 마련합니다.

### [주요 기능 2] 학식 메뉴를 영어로 번역

학식킹은 오늘의 학식 메뉴를 **맥락을 반영하여 정확히 번역**합니다. 학식킹은 fine-tuning된 deepl API를 알맞게 활용하여 ‘육회’를 ‘Six times’가 아니라 ‘Beef Tartar’로 번역합니다. 

### **[주요 기능 3] 알러지 유발 가능성 정보 제공**

학식킹은 해당 음식에 **소고기, 돼지고기, 닭고기, 계란이 함유되었는지**에 대한 대략적인 정보를 제공합니다. 같은 음식이라도 레시피와 재료가 다를 수 있기 때문에 특정 재료의 포함 가능성을 판단하기 가장 널리 사용되는 ‘만개의 레시피’ 웹사이트를 기준으로 판단합니다.

## Quick Start

### .env.development

```jsx
REACT_APP_API_BASE_URL=[PUT_YOUR_APIGATEWAY_URL]
```

### .env.production

```jsx
REACT_APP_API_BASE_URL=[PUT_YOUR_DATABSE_URL]
API_GATEWAY_URL=[PUT_YOUR_APIGATEWAY_URL]
```

### .env

```makefile
#put your slack token
token_slack = {'channel_id': 'Put your own',
                'app_token': 'Put your own',
                'bot_token': 'Put your own'
                }
# api gateway URL                
api_server = 'Put your own'

# aws access key to handle aws cli
aws_access_key = 'Put your own'
aws_access_key_priviate = 'Put your own'

# open api key for get discription of foods
TOKEN_OPENAI = 'Put your own'

# deepl key for translation
deepl_token = 'Put your own'
```

### Installation

1. Install dependencies:
    
    ```bash
    npm install
    ```
    
2. Start the development server
    
    ```bash
    npm install
    ```
    
3. Open the project in your browser:
    
    ```bash
    http:/localhost:3000
    ```
    

## Project Structure

```makefile
Hakshik_king
├─ COPYING.txt
├─ README.md
├─ back_end
│  ├─ .env
│  ├─ APIs
│  │  ├─ DB_handler.py
│  │  ├─ food_teller.py
│  │  ├─ get_shik.py
│  │  ├─ recipe.py
│  │  ├─ router.py
│  │  ├─ routines
│  │  │  ├─ daily_lambda.py
│  │  │  └─ weekly_lambda.py
│  │  └─ translator.py
│  ├─ models.py
│  ├─ server.py
│  └─ update.py
└─ front_end
   ├─ .env.development
   ├─ .env.production
   ├─ package-lock.json
   ├─ package.json
   ├─ public
   │  ├─ LOGO_hakshikking.svg
   │  ├─ favicon.ico
   │  ├─ img
   │  │  ├─ LOGO_CI.svg
   │  │  ├─ arrow_left.svg
   │  │  └─ arrow_right.svg
   │  ├─ index.html
   │  ├─ logo192.png
   │  ├─ logo512.png
   │  ├─ manifest.json
   │  └─ robots.txt
   ├─ src
   │  ├─ App.test.tsx
   │  ├─ App.tsx
   │  ├─ api
   │  │  └─ api.ts
   │  ├─ components
   │  │  └─ Navigator.tsx
   │  ├─ icons
   │  │  ├─ ArrowLeft.tsx
   │  │  ├─ ArrowRight.tsx
   │  │  ├─ Hyperlink.tsx
   │  │  └─ LOGO_CI.tsx
   │  ├─ index.tsx
   │  ├─ locales
   │  │  ├─ en
   │  │  │  └─ translation.json
   │  │  ├─ i18n.ts
   │  │  └─ ko
   │  │     └─ translation.json
   │  ├─ pages
   │  │  └─ Main
   │  │     ├─ Main.tsx
   │  │     ├─ components
   │  │     │  ├─ CafeteriaSelector.tsx
   │  │     │  ├─ DaySelector.tsx
   │  │     │  ├─ MenuCard.tsx
   │  │     │  ├─ MenuCardsContainer.tsx
   │  │     │  ├─ MenuModal.tsx
   │  │     │  ├─ Review.tsx
   │  │     │  ├─ getToday.ts
   │  │     │  └─ menuArr_example.json
   │  │     └─ interface.ts
   │  ├─ react-app-env.d.ts
   │  ├─ setupProxy.js
   │  └─ styles
   │     ├─ GlobalStyle.tsx
   │     ├─ style_modules.tsx
   │     └─ theme.ts
   ├─ tsconfig.json
   └─ yarn.lock
```

## 기술 구현

![image](https://github.com/user-attachments/assets/885b4e72-0b5c-4413-963b-fa0b577c53a3)

### 메뉴 리스트

![image](https://github.com/user-attachments/assets/b773a39a-0a4c-45d6-b265-c616b42991a5)

- AWS의 EventBridge는 매일 자정 labmda 함수를 trigger합니다.
- lambda 함수는 자동으로 인하대학교 학생 식당 사이트를 크롤링하여 식단표 PDF 파일을 다운로드 받습니다.
- lambda함수는 식단표 **PDF 파일을 JSON 형식으로 파싱**합니다.
- 이 때 Tabula.py는 JAVA dependency를 필요로 하지만, lambda 함수는 python 3.8을 기반으로 작동하도록 세팅되어 있기 때문에 해당 환경이 구축되어 있지 않습니다.
- lambda 실행 시 매번 JAVA 환경을 구축하거나 dependency를 layer로 설치한다면 비용과 용량 상의 문제가 발생합니다.
    - lambda는 **1밀리초마다 과금**되는 서비스입니다.
    - lambda에 세팅할 수 있는 layer의 최대 크기는 200Mb입니다.
- 학식킹은 위의 문제를 해결하기 위해 **Docker container를 이용하여 정해진 실행 환경에서 해당 function이 구동될 수 있도록 설계**하였습니다.

### 메뉴 설명

![image](https://github.com/user-attachments/assets/19f3f704-5853-467e-9fa4-17a3cf8aded3)

- OpenAI의 api를 이용하여 메뉴에 대한 설명을 생성합니다.
    - 프롬프트 엔지니어링을 통해 보다 정확한 설명을 정해진 포맷으로 return하도록 파인튜닝하였습니다.
- 음식에 대한 설명을 DynamoDB에 저장하여 **DB에 해당 메뉴가 없을 때만 API를 호출**합니다.
    - OpenAI api는 **호출할 때마다 비용이 발생**하고 매번 request를 보낼 때마다 연결을 새로 수립해야 합니다.
    - 반면 DynamoDB 서비스는 **미리 테이블과 연결을 맺어 둔 상태**이기 때문에 description을 얻기까지 걸리는 시간이 훨씬 적습니다.
    - 이러한 방식을 사용하면 **사용자에게 빠르고 일관적인 경험을 제공할 수 있고, 비용을 절감**할 수 있습니다.
