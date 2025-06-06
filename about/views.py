from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from about.models import About, RAG, AIConvHistory
import google.generativeai as genai
genai.configure(api_key="AIzaSyBrP93ZQh__vMrbLwptZFtdSRx9rZF7mJY")
model_name = "gemma-3-27b-it"
model = genai.GenerativeModel(model_name)

def root(request):
    about = About.objects.filter(is_active=True).first()
    return render(request, 'about.html', {'about': about})


@csrf_exempt
def chat(request):
    if request.method == 'POST':
        try:
            # 1. 사용자 질문받기
            data = json.loads(request.body)
            user_prompt = data.get('prompt') # 파싱된 질문
            # 질문자의 ip
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
            if ip_address:
                ip_address = ip_address.split(',')[0]
            else:
                ip_address = request.META.get('REMOTE_ADDR')
            
            # 2. 자료 검색 단계
            rag = RAG.objects.filter(is_active=True).first()
            if rag:
                retrieved_text = rag.content
            else:
                retrieved_text = "직업: 컨설턴트\n nbti: ENTP\n 성격: 지랄맞음"
                            
            # 3. 프롬프트 구성(RAG)
            full_prompt = f"""
                            [지침]
                            {retrieved_text}

                            [질문]
                            {user_prompt}
                            """            
            
            response = model.generate_content(
                f"""지침을 참고해서 두 문장 이내로 답변해줘. \n\n{full_prompt}\n\n답변:"""
            )
            result = response.text.strip()
            
            if result.lower().startswith("[답변]"):
                result = result[4:].strip()
            
            AIConvHistory.objects.create(
                ask = user_prompt,
                ip = ip_address,
                answer = result,
                model = model_name,
                rag = rag
            )
        
        except Exception as e:
            error = f"프롬프트: {str(e)}"
            print(error)
            result = "답변을 생성하지 못했습니다."

        return JsonResponse({'response': result})

    return JsonResponse({'error': '잘못된 요청 방식입니다.'}, status=400)

