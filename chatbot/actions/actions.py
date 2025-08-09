# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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
# import nrclex
# from nrclex import NRCLex
# from rasa_sdk.types import DomainDict
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionAcknowledgeSuicide(Action):
#
#     def name(self) -> Text:
#         return "action_acknowledge_suicide"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(template="utter_suicide")
#         dispatcher.utter_message(template="utter_hotlines")
#
#         return []



# class ActionEmotion(Action):  # finalllll
#
#     def name(self) -> Text:
#         return "action_emotion"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         text = str(tracker.latest_message["text"])
#
#         emotion = NRCLex(text)
#
#         dispatcher.utter_message(
#             text=" The affect dictionary of the emotions detected are {} ".format(emotion.affect_dict))
#         dispatcher.utter_message(text=" The raw emotion scores detected are {} ".format(emotion.raw_emotion_scores))
#         dispatcher.utter_message(text=" The top emotions detected are  {} ".format(emotion.top_emotions))
#         dispatcher.utter_message(text=" The affect frequencies detected are {} ".format(emotion.affect_frequencies))


# class ActionHandleAbuse(Action):
#
#     def name(self) -> Text:
#         return "action_handle_abuse"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict) -> List[Dict[Text, Any]]:
#
#         latest_intent = tracker.latest_message['intent'].get('name')
#
#         if latest_intent == "physical_abuse":
#             dispatcher.utter_message(template="utter_physical_abuse")
#         elif latest_intent == "mental_abuse":
#             dispatcher.utter_message(template="utter_mental_abuse")
#         elif latest_intent == "sexual_abuse":
#             dispatcher.utter_message(template="utter_sexual_abuse")
#
#         return []

# class ActionHandleSocialMediaParasocial(Action):
#
#     def name(self) -> Text:
#         return "action_handle_social_media_parasocial"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_social_media_parasocial")
#         return []
#
# class ActionHandleBodyDysmorphia(Action):
#
#     def name(self) -> Text:
#         return "action_handle_body_dysmorphia"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_body_dysmorphia")
#         return []
#
# class ActionHandleBeingToxic(Action):
#
#     def name(self) -> Text:
#         return "action_handle_being_toxic"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_being_toxic")
#         return []
#
# class ActionHandleNegativeEmotions(Action):
#
#     def name(self) -> Text:
#         return "action_handle_negative_emotions"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_negative_emotions")
#         return []


# class ActionHandleStudentIssues(Action):
#
#     def name(self) -> Text:
#         return "action_handle_student_issues"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         latest_intent = tracker.latest_message['intent'].get('name')
#
#         if latest_intent == "student_issue_time_management":
#             dispatcher.utter_message(template="utter_student_issue_time_management")
#         elif latest_intent == "student_issue_low_motivation":
#             dispatcher.utter_message(template="utter_student_issue_low_motivation")
#         elif latest_intent == "student_issue_lack_of_concentration":
#             dispatcher.utter_message(template="utter_student_issue_lack_of_concentration")
#         elif latest_intent == "student_issue_distractions":
#             dispatcher.utter_message(template="utter_student_issue_distractions")
#
#         elif latest_intent == "student_issue_homesickness":
#             dispatcher.utter_message(template="utter_student_issue_homesickness")
#         elif latest_intent == "student_issue_depression":
#             dispatcher.utter_message(template="utter_student_issue_depression")
#         elif latest_intent == "student_issue_major":
#             dispatcher.utter_message(template=" utter_student_issue_major")
#         elif latest_intent == "student_issue_financial":
#             dispatcher.utter_message(template="utter_student_issue_financial")
#         elif latest_intent == "student_issue_resources":
#             dispatcher.utter_message(template="utter_student_issue_resources")
#         elif latest_intent == "student_issue_sleep":
#             dispatcher.utter_message(template="utter_student_issue_sleep")
#         elif latest_intent == "student_issue_partying":
#             dispatcher.utter_message(template="utter_student_issue_partying")
#         elif latest_intent == "student_issue_procrastination":
#             dispatcher.utter_message(template="utter_student_issue_procrastination")
#         elif latest_intent == "student_issue_memory":
#             dispatcher.utter_message(template="utter_student_issue_memory")
#         elif latest_intent == "student_issue_interest":
#             dispatcher.utter_message(template="utter_student_issue_interest")
#         elif latest_intent == "student_issue_organization":
#             dispatcher.utter_message(template="utter_student_issue_organization")
#         elif latest_intent == "student_issue_test_anxiety":
#             dispatcher.utter_message(template="utter_student_issue_test_anxiety")
#         elif latest_intent == "student_issue_technology":
#             dispatcher.utter_message(template="utter_student_issue_technology")
#         elif latest_intent == "student_issue_loneliness":
#             dispatcher.utter_message(template="utter_student_issue_loneliness")
#
#         return []


# class ActionHandleSubstanceAbuse(Action):
#
#     def name(self) -> Text:
#         return "action_handle_substance_abuse"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         # Get the latest intent from the tracker
#         latest_intent = tracker.latest_message['intent'].get('name')
#
#         # Define responses for each type of substance abuse
#         if latest_intent == "substance_abuse_drugs":
#             dispatcher.utter_message(template="utter_substance_abuse_drugs")
#         elif latest_intent == "substance_abuse_smoking":
#             dispatcher.utter_message(template="utter_substance_abuse_smoking")
#         elif latest_intent == "substance_abuse_alcohol":
#             dispatcher.utter_message(template="utter_substance_abuse_alcohol")
#         # Add more conditions for other types of substance abuse
#
#         return []

# class ActionTellJokes(Action):
#
#     def name(self) -> Text:
#         return "action_tell_joke"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_joke")
#         return []

# class ActionAnswerBipolarDisorder(Action):
#     def name(self) -> Text:
#         return "action_answer_bipolar_disorder"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_bipolar_disorder")
#         return []

# class ActionAnswerOCD(Action):
#     def name(self) -> Text:
#         return "action_answer_ocd"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_ocd")
#         return []
#
# class ActionAnswerPTSD(Action):
#     def name(self) -> Text:
#         return "action_answer_ptsd"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_ptsd")
#         return []
#
# class ActionAnswerSchizophrenia(Action):
#     def name(self) -> Text:
#         return "action_answer_schizophrenia"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_schizophrenia")
#         return []
#
# class ActionAnswerDementia(Action):
#     def name(self) -> Text:
#         return "action_answer_dementia"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_dementia")
#         return []
#
# class ActionAnswerAutism(Action):
#     def name(self) -> Text:
#         return "action_answer_autism"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_autism")
#         return []


# class ActionProvideWellbeingInfo(Action):
#
#     def name(self) -> Text:
#         return "action_provide_wellbeing_info"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         intent = tracker.latest_message['intent'].get('name')
#
#         if intent == "ask_self_care_practices":
#             dispatcher.utter_message(template="utter_self_care_practices")
#         elif intent == "ask_mental_wellbeing_practices":
#             dispatcher.utter_message(template="utter_mental_wellbeing_practices")
#         elif intent == "ask_healthy_eating_tips":
#             dispatcher.utter_message(template="utter_healthy_eating_tips")
#         elif intent == "ask_mindfulness_meditation":
#             dispatcher.utter_message(template="utter_mindfulness_meditation")
#         elif intent == "ask_hydration_importance":
#             dispatcher.utter_message(template="utter_hydration_importance")
#         elif intent == "ask_journaling_benefits":
#             dispatcher.utter_message(template="utter_journaling_benefits")
#         elif intent == "ask_time_in_nature":
#             dispatcher.utter_message(template="utter_time_in_nature")
#         elif intent == "ask_creative_activities":
#             dispatcher.utter_message(template="utter_creative_activities")
#         elif intent == "ask_social_connections":
#             dispatcher.utter_message(template="utter_social_connections")
#         elif intent == "ask_personal_boundaries":
#             dispatcher.utter_message(template="utter_personal_boundaries")
#         elif intent == "ask_therapy_counseling":
#             dispatcher.utter_message(template="utter_therapy_counseling")
#         elif intent == "ask_relaxation_techniques":
#             dispatcher.utter_message(template="utter_relaxation_techniques")
#         elif intent == "ask_gratitude_practice":
#             dispatcher.utter_message(template="utter_gratitude_practice")
#         elif intent == "ask_positive_affirmations":
#             dispatcher.utter_message(template="utter_positive_affirmations")
#         elif intent == "ask_mbsr":
#             dispatcher.utter_message(template="utter_mbsr")
#         elif intent == "ask_screen_time":
#             dispatcher.utter_message(template="utter_screen_time")
#         elif intent == "ask_self_compassion":
#             dispatcher.utter_message(template="utter_self_compassion")
#         elif intent == "ask_volunteer_work":
#             dispatcher.utter_message(template="utter_volunteer_work")
#         elif intent == "ask_routine_structure":
#             dispatcher.utter_message(template="utter_routine_structure")
#         elif intent == "ask_support_groups":
#             dispatcher.utter_message(template="utter_support_groups")
#         elif intent == "express_gratitude":
#             dispatcher.utter_message(template="utter_gratitude_response")
#
#         return []