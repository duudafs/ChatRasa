# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from datetime import datetime, timedelta
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests

class ActionCotacaoDolar(Action):

    def name(self):
        return "action_cotacao_dolar"

    def run(self, dispatcher, tracker, domain):
        ontem = (datetime.now() - timedelta(days=1)).strftime("%m-%d-%Y")

        url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{ontem}'&$format=json"

        response = requests.get(url)
        data = response.json()

        if "value" in data and len(data["value"]) > 0:
            cotacao = data["value"][0]["cotacaoVenda"]
            dispatcher.utter_message(text=f"dólar: R$ {cotacao:.2f}")
        else:
            dispatcher.utter_message(text="não consegui pegar a cotação")

        return []
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
