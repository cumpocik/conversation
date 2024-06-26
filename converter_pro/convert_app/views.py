from django.shortcuts import render
import requests

name = ['BYN']
scale = [1]
rate = [1.0]

def index_view(request):
    return render(request, 'index.html')

def get_exchange_rates():
    url = "https://www.nbrb.by/api/exrates/rates?periodicity=0"
    response = requests.get(url)
    data = response.json()

    for currency in data:
        name.append(currency["Cur_Abbreviation"])
        scale.append(currency["Cur_Scale"])
        rate.append(currency["Cur_OfficialRate"])

def convert_currency(request):
    get_exchange_rates()
    if request.method == "POST":
        amount = request.POST.get("amount")
        if amount is '':
            return render(request, "index.html", {"error_message": "Введите сумму"})
        amount = float(amount)
        from_currency = request.POST.get("from")
        to_currency = request.POST.get("to")

        index_from = name.index(from_currency)
        index_to = name.index(to_currency)

        converted_amount = amount * scale[index_from] * rate[index_from] / rate[index_to] * scale[index_to]

        return render(request, "index.html", {"converted_amount": converted_amount, 'amount': amount, 'from': name[index_from], 'to': name[index_to]})

    return render(request, "index.html")
