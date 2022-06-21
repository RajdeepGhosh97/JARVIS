# # # QUESTION ANSWER # # #
import wolframalpha
import wikipedia

# # # CUSTOM-MADE IMPORTS # # #
from features.ListenSpeak import speak , myCommand


def Q_nd_A(text):

    question = text.split(" ")
    question = " ".join(question[2:])
    try:
        #wolframalpha code here
        Wolframalpha_API = "KTYP34-95YWAAP4GE"
        client = wolframalpha.Client(Wolframalpha_API)
        res = client.query(question)
        answer = next(res.results).text 
        #print("according to wolramalpha "+ answer)
        speak("According to wolframalpha")

    except e:
        #wikipedia code here
        answer = wikipedia.summary(text , sentences=2)
        #print("according to wikipedia "+ answer)
        speak("According TO wikipedia")

    return speak(answer)