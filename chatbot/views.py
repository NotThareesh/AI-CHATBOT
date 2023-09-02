from django.shortcuts import render
from .models import PromptData
import openai

contents = []

def chatAPI(request, query):
  openai.api_key = "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"
  # openai.api_key = "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"

  prompt = f"Search the web for information about '{query}' and provide a concise answer:\n"
  
  try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

  except Exception as e:
     print(e)
     return "Some Error Occured"

  return response.choices[0].text.strip()
  # if request.method == 'POST':
  #   prompt = request.POST['prompt']
  #   response = openai.ChatCompletion.create(
  #     model="text-davinci-003",
  #     prompt=prompt,
  #     temperature=1,
  #     max_tokens=256,
  #     top_p=1,
  #     frequency_penalty=0,
  #     presence_penalty=0
  #   )
  #   return JsonResponse(response)
  
  # return JsonResponse('BAD API RESPONSE')

# Create your views here.
def home(request):
    if request.method == 'POST':
        data = request.POST.get('prompt')

        response = chatAPI(request, data)

        contents.append([data, response])

        instance = PromptData.objects.create(
            username='None',
            prompt=contents,
        )

        instance.save()

    return render(request, 'base.html', context={'data': contents, 'user': 'None'})
