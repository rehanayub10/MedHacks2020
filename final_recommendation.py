import numpy as np

depression = {"1":"You seem to be handling yourself well. I would recommend a form of artistic expression. Some ideas are journaling, drawing, listening to music, or writing poetry. Also, you can reach out to family and close friends for emotional support.",
              "2a":"You are in a tough spot. A great way to combat sadness is regular exercise. Given your mobility level, I would recommend light stretching daily. Also, you can reach out to family and close friends for emotional support.",
              "2b":"You are in a tough spot. A great way to combat sadness is regular exercise. Given your mobility level, I would recommend a stroll around the block daily. Also, you can reach out to family and close friends for emotional support.",
              "2c":"You are in a tough spot. A great way to combat sadness is regular exercise. Given your mobility level, I would recommend 30 minutes of intense exercise such as swimming, yoga, jogging, or dance daily. Also, you can reach out to family and close friends for emotional support.",
              "3":"Based on your responses, it seems as though therapy would be beneficial. Please schedule an appointment so you can be evaluated by a professional. Please reach out to family and friends for support as well.",
              "4":"You have mentioned hopelessness and self harm. Please call the suicide hotline at 1-800-273-8255. If you don’t mind me asking, can you rate your mobility?"}

anxiety = {"1a":"You seem to be handling yourself fairly well. A great way to combat anxiety in general is exercise. Given your mobility level, I would recommend light stretching daily. Also, taking up a hobby such as reading, journaling, or art is a great way to stay calm.  ",
           "1b":"You seem to be handling yourself fairly well. A great way to combat anxiety in general is exercise. Given your mobility level, I would recommend a stroll around the block daily. Also, taking up a hobby such as reading, journaling, or art is a great way to stay calm.  ",
           "1c":"You seem to be handling yourself fairly well. A great way to combat anxiety in general is exercise. Given your mobility level, I would recommend 30 minutes of intense exercise such as swimming, yoga, jogging, or dance daily. Also, taking up a hobby such as reading, journaling, or art is a great way to stay calm.  ",
           "2":"You are in a tough spot. A great way to combat anxiety is cognitive behavioral therapy and mindfulness meditation. There are several applications and books available to help guide the process. Also, you can reach out to family and close friends for emotional support. ",
           "3":"Based on your responses, it seems as though therapy would be beneficial. Please schedule an appointment so you can be evaluated by a professional. Please reach out to family and friends for support as well.",
           "4":"You have mentioned hopelessness and self harm. Please call the suicide hotline at 1-800-273-8255."}

anger ={"1a":"You seem to be handling yourself fairly well. A great way to combat anger management problems, in  general, is exercise. Given your mobility level, I would recommend light stretching daily. Also, try practicing breathing exercises to stay calm in stressful situations.",
        "1b":"You seem to be handling yourself fairly well. A great way to combat anger management problems, in general is exercise. Given your mobility level, I would recommend a stroll around the block daily. Also, try practicing breathing exercises to stay calm in stressful situations.",
        "1c":"You seem to be handling yourself fairly well. A great way to combat anger management problems, in general is exercise. Given your mobility level, I would recommend 30 minutes of intense exercise such as swimming, yoga, jogging, or dance daily. Also, try practicing breathing exercises to stay calm in stressful situations.  ",
        "2":"You are in a tough spot. A great way to combat anger is cognitive behavioral therapy and mindfulness meditation. There are several applications and books available to help guide the process. Consider journaling when you feel angry to help sort through your feelings.",
        "3":"Based on your responses, it seems as though therapy would be beneficial. Please schedule an appointment so you can be evaluated by a professional. Please reach out to family and friends for support as well.",
        "4":"You have mentioned hopelessness and self harm. Please call the suicide hotline at 1-800-273-8255."}


def compute_av_score(scores, responses, emotion):
    sum=0;
    j=0;
    for i in range(len(responses)):
        if(responses[i]==emotion):
            sum=sum+scores[i];
            j=j+1;
    av_sc=sum/j;
    return av_sc;

def final_rec(mobility, emotion, scores, responses):
    av_score=compute_av_score(scores, responses, emotion);
    if (emotion=='anger'):
        if (av_score>=0.0 and av_score<=0.33):
            if(mobility=='limited'):
                response=anger["1a"];
            elif (mobility == 'moderate'):
                response = anger["1b"];
            elif (mobility == 'normal'):
                response = anger["1c"];
        elif (av_score>0.33 and av_score<=0.66):
            response=anger["2"];
        elif (av_score > 0.66 and av_score <= 0.9):
            response = anger["3"];
        else:
            response = anger["4"];
    elif(emotion=='anxiety'):
        if (av_score>=0.0 and av_score<=0.33):
            if(mobility=='limited'):
                response=anxiety["1a"];
            elif (mobility == 'moderate'):
                response = anxiety["1b"];
            elif (mobility == 'normal'):
                response = anxiety["1c"];
        elif (av_score>0.33 and av_score<=0.66):
            response=anxiety["2"];
        elif (av_score > 0.66 and av_score <= 0.9):
            response = anxiety["3"];
        else:
            response = anxiety["4"];
    elif(emotion=='sad'):

        if (av_score>=0.0 and av_score<=0.33):
            response=depression["1"];
        elif (av_score>0.33and av_score<=0.66):
            if(mobility=='limited'):
                response=depression["2a"];
            elif (mobility == 'moderate'):
                response = depression["2b"];
            elif (mobility == 'normal'):
                response = depression["2c"];
        elif (av_score > 0.66 and av_score <= 0.9):
            response = depression["3"];
        else:
            response = depression["4"];
    else:
        response = "You seem to be doing well! Keep up the good job!"

    return response;

