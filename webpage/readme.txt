Crossdit Homepage setup.
The homepage consists of a Frontend and
a Chatbot backend (powered by RASA). 
In order to make the Chatbot work, one needs to install RASA
and run the following command in the RASA cmdline:
rasa run -m models --enable-api --cors "*" --debug
