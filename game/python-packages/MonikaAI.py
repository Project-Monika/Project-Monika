from enum import Enum
import math
import random
EmotionState = Enum("Happy","Sad","Angry","Disgusted","Romantic","Calm","Brave","Fear")
import time
class EmotionalRange():
    HighEmotion = EmotionState.Happy
    LowEmotion = EmotionState.Sad
    Value = 100.0
    def __init__(self, State1, State2, value):
        self.HighEmotion = State1
        self.LowEmotion = State2
        self.Value = value
    def ChangeValue(self, Value):
        self.Value = Clamp(self.Value + ((Value*random.randint(75,125)/100)), 0,100)

class AIManager():
    random.seed(time.time)
    ERanges = []
    ERanges.append(EmotionalRange(EmotionState.Happy, EmotionState.Sad, random.randint(250, 750)/10)) #Happy-Sad
    ERanges.append(EmotionalRange(EmotionState.Angry, EmotionState.Calm, random.randint(250, 750)/10)) #Angry-Calm
    ERanges.append(EmotionalRange(EmotionState.Disgusted, EmotionState.Calm, random.randint(250, 750)/10)) #Disgusted-Calm
    ERanges.append(EmotionalRange(EmotionState.Romantic, EmotionState.Calm, random.randint(250, 750)/10)) #Romantic-Calm
    ERanges.append(EmotionalRange(EmotionState.Brave, EmotionState.Fear, random.randint(250, 750)/10)) #Brave-Fear
    ERanges.append(EmotionalRange(EmotionState.Romantic, EmotionState.Fear, random.randint(250, 750)/10)) #Romatic-Fear
    ERanges.append(EmotionalRange(EmotionState.Romantic, EmotionState.Sad, random.randint(250, 750)/10)) #Romatic-Sad

    def Diffrence(self,Happy, Sad, Angry, Disgusted, Romatic, Calm, Brave, Fear):
        Value = 0.0;
        Value = self.Percentage(Happy,self.GetValue(EmotionState.Happy))
        Value = Value + self.Percentage(Sad,self.GetValue(EmotionState.Sad))
        Value = Value + self.Percentage(Angry,self.GetValue(EmotionState.Angry))
        Value = Value + self.Percentage(Disgusted,self.GetValue(EmotionState.Disgusted))
        Value = Value + self.Percentage(Romatic,self.GetValue(EmotionState.Romantic))
        Value = Value + self.Percentage(Calm,self.GetValue(EmotionState.Calm))
        Value = Value + self.Percentage(Brave,self.GetValue(EmotionState.Brave))
        Value = Value + self.Percentage(Fear,self.GetValue(EmotionState.Fear))
        return Value/8.0

    def GetValue(self,Emotion):
        Value = 0.0
        Counter = 0
        for ERange in self.ERanges:
            if ERange.HighEmotion == Emotion:
                Value = Value + ERange.Value
                Counter = Counter + 1
            elif ERange.LowEmotion == Emotion:
                Value = Value + 100 - ERange.Value
                Counter = Counter + 1
        if Counter != 0:
            return Value/Counter
        else:
            return Value
        

    def Percentage(self,V1, V2):
        return ((V1-V2))/(V1 + V2)/2 #math.copysign(1,V1-V2)*
    def MoodChange(self,Emotion, Value):
        if Emotion == "Happy":
            for ERange in self.ERanges:
                if ERange.HighEmotion == EmotionState.Happy:
                    ERange.ChangeValue(Value)
                elif ERange.LowEmotion == EmotionState.Happy:
                    ERange.ChangeValue(-Value)
        elif Emotion == "Sad":
            for ERange in self.ERanges:
                if ERange.HighEmotion == EmotionState.Sad:
                    ERange.ChangeValue(Value)
                elif ERange.LowEmotion == EmotionState.Sad:
                    ERange.ChangeValue(-Value)
        elif Emotion == "Angry":
            for ERange in self.ERanges:
                if ERange.HighEmotion == EmotionState.Angry:
                    ERange.ChangeValue(Value)
                elif ERange.LowEmotion == EmotionState.Angry:
                    ERange.ChangeValue(-Value)
        elif Emotion == "Disgusted":
            for ERange in self.ERanges:
                if ERange.HighEmotion == EmotionState.Disgusted:
                    ERange.ChangeValue(Value)
                elif ERange.LowEmotion == EmotionState.Disgusted:
                    ERange.ChangeValue(-Value)
        elif Emotion == "Romantic":
            for ERange in self.ERanges:
                if ERange.HighEmotion == EmotionState.Romantic:
                    ERange.ChangeValue(Value)
                elif ERange.LowEmotion == EmotionState.Romantic:
                    ERange.ChangeValue(-Value)
        elif Emotion == "Calm":
            for ERange in self.ERanges:
                if ERange.HighEmotion == EmotionState.Calm:
                    ERange.ChangeValue(Value)
                elif ERange.LowEmotion == EmotionState.Calm:
                    ERange.ChangeValue(-Value)
        elif Emotion == "Brave":
            for ERange in self.ERanges:
                if ERange.HighEmotion == EmotionState.Brave:
                    ERange.ChangeValue(Value)
                elif ERange.LowEmotion == EmotionState.Brave:
                    ERange.ChangeValue(-Value)
        elif Emotion == "Fear":
            for ERange in self.ERanges:
                if ERange.HighEmotion == EmotionState.Fear:
                    ERange.ChangeValue(Value)
                elif ERange.LowEmotion == EmotionState.Fear:
                    ERange.ChangeValue(-Value)




        def MoodSwing(self):
            Prob= random.randint(1, 115)
            Value = random.randint(10, 20)
            if Prob > 75:
                if Prob < 80:
                    MoodChange("Happy", Value)
                if Prob < 85:
                    MoodChange("Sad", Value)
                if Prob < 90:
                    MoodChange("Angry", Value)
                if Prob < 95:
                    MoodChange("Disgusted", Value)
                if Prob < 100:
                    MoodChange("Romantic", Value)
                if Prob < 105:
                    MoodChange("Calm", Value)
                if Prob < 110:
                    MoodChange("Brave", Value)
                else:
                    MoodChange("Fear", Value)



def Clamp (Value, LowerLimit, UpperLimit):
    if Value > UpperLimit:
        return UpperLimit
    elif Value < LowerLimit:
        return LowerLimit

    return Value
    
    