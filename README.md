## Hi) I'll talk about how I created a voice assistant (and now am working on improving it)

<br>

There is only talk about chatgpt around, and I hear all the time: Maria, you work in IT, help me connect to chatgpt (blocked in Russia)

and I thought it would be fun to say that you can talk to him right now, you just need to say the command word

and in general it is interesting to just chat with him))

![image](https://user-images.githubusercontent.com/109607272/236424584-fd57aa9c-ce5c-4fd2-88eb-8ecdca4e4fb5.png)


<br><br>
---------------------------------------------------------
So, the work was divided into several stages: 
1. speech recording
2. converting to text(STT)
3. search command phrase to cut text
4. api request to chatgpt
5. voice response(TTS)
<br><br>


I used the sounddevice library to record sound. Recorded for 5 seconds, after which she sent the record for transcription of the whisper model.
Whisper - a model based on the architecture of the transformer (I described how it works in past projects, you can find it). Use the large model for more accurate speech recognition.

![image](https://user-images.githubusercontent.com/109607272/236423588-cbcc38b9-5aa7-4727-8306-7c37137fc99a.png)

I send the decrypted text to api and voice the answer using the gtts library.

Code:

`record.py` - recording audio

`transcriber.py` - transcibing

`main.py` - starts the assistant

