# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionComputeManure(Action):
   def name(self):
      # type: () -> Text
      return "action_compute_manure"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

      area = tracker.get_slot('field_size')
      location = tracker.get_slot('location')
      crop = tracker.get_slot('crop_type')

      return [SlotSet("manure_quantity", int(area)*10),
               SlotSet("location", None),SlotSet("field_size", None),
               SlotSet("crop_type", None)]

class ActionComputeManureProduction(Action):
   def name(self):
      # type: () -> Text
      return "action_compute_manure_production"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
      animal_number = tracker.get_slot('animal_number')
      animal_type = tracker.get_slot('animal_type')
      stable_type = tracker.get_slot('stable_type')

      return [SlotSet("manure_production_estimate", float(animal_number) * 10.0),
               SlotSet("animal_number", None),SlotSet("animal_type", None),
               SlotSet("stable_type", None)]