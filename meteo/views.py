from django.shortcuts import render
import requests
from django.http import JsonResponse

def lisboa_view(request):

    url = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/hp-daily-forecast-day0.json"
    response = requests.get(url)
    data = response.json()

    date= data['forecastDate']
    # Procurar o ID da cidade de Lisboa (podemos precisar ajustar isto com base na estrutura da API)
    lisboa_data = next((item for item in data['data'] if item["globalIdLocal"] == 1110600), None)

    urlemote = "https://api.ipma.pt/open-data/weather-type-classe.json"
    responseemote = requests.get(urlemote)
    dataemote = responseemote.json()

    iconPath = f"/static/meteo/w_ic_d_{int(lisboa_data['idWeatherType']):02d}anim.svg"
    emote_data = next((item for item in dataemote['data'] if item["idWeatherType"] == lisboa_data['idWeatherType']), None)

    meteo = {
        'city': 'Lisboa',
        'date':date,
        'min_temp': lisboa_data['tMin'] if lisboa_data else 'N/A',
        'max_temp': lisboa_data['tMax'] if lisboa_data else 'N/A',
        'iconPath': iconPath,
        'description':  emote_data['descWeatherTypePT'] if emote_data else 'N/A',
    }

    context = {
        'meteo': meteo
    }

    return render(request, "meteo/lisboa.html",context)



def cidades_view(request):

    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cities_response = requests.get(cities_url)
    cities_response.raise_for_status()  # Verificar se a resposta é bem-sucedida
    cities_data = cities_response.json()

    cidade = {cidade['local']: cidade['globalIdLocal'] for cidade in cities_data['data']}

    context= {
        'cidade': cidade,
        }
    return render(request, 'meteo/cidades.html', context)


def cidade_view(request, cidade_id, dia_id):


    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cities_response = requests.get(cities_url)
    cities_response.raise_for_status()  # Verificar se a resposta é bem-sucedida
    cities_data = cities_response.json()

    CITY_MAPPING = {cidade['globalIdLocal']: cidade['local'] for cidade in cities_data['data']}


    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json"
    response = requests.get(url)

    if response.status_code != 200:
        return JsonResponse({"error": "Could not fetch data from API"}, status=500)


    data = response.json()

    forecasts = data.get("data", [])
    forecasts.sort(key=lambda x: x["forecastDate"])


    try:
        dia_id = int(dia_id)
        if dia_id < 0 or dia_id >= len(forecasts):
            raise IndexError("Invalid day index")
    except (ValueError, IndexError) as e:
        return JsonResponse({"error": str(e)}, status=400)

    # Seleciona a previsão específica
    forecast = forecasts[dia_id]

    urlemote = "https://api.ipma.pt/open-data/weather-type-classe.json"
    responseemote = requests.get(urlemote)
    dataemote = responseemote.json()

    iconPath = f"/static/meteo/w_ic_d_{int(forecast['idWeatherType']):02d}anim.svg"
    emote_data = next((item for item in dataemote['data'] if item["idWeatherType"] == forecast['idWeatherType']), None)

    nomeCidade = CITY_MAPPING.get(int(cidade_id), "Desconhecido")

    context = {
        "nomeCidade" : nomeCidade,
        "cidadeid" : cidade_id,
        "forecastDate": forecast["forecastDate"],
        "data": forecast,
        'iconPath': iconPath,
        'description':  emote_data['descWeatherTypePT'] if emote_data else 'N/A',
    }

    return render(request, 'meteo/cidade.html', context)




