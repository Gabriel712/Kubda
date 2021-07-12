from flask import Flask,request
import requests
from bs4 import BeautifulSoup

app = Flask("Kubda")

@app.route("/", methods=["GET", "POST"])
def kub_site_response_time():
    if "site" in request.args:
        # parametro site na URL
        site = request.args.get("site")

        # acessando site
        response = requests.get(site)

        # calcula o tempo de resposta
        time_response = response.elapsed.total_seconds()

        # status da resposta do site / 200 / 404 ...
        status_response = response.status_code

        # coleta o HTML/response do site
        text_response = response.text

        # invoca o BeautifulSoup para a leitura do HTML
        soup = BeautifulSoup(text_response, 'html.parser')

        # coleta o titulo da pagina usando o BeautifulSoup
        title_reponse = soup.find('title').string


        map_response = {
        "site":site,
        "time_response":time_response,
        "status":status_response,
        "size":len(text_response),
        "title_reponse":title_reponse
        }

        return(map_response)

    return("Olá, seus Kubs estão OK!")
