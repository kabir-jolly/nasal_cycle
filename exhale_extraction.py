from pydub import AudioSegment

recording = AudioSegment.from_wav("/Users/kabirjolly/Library/Mobile Documents/com~apple~CloudDocs/Microphone Recordings/7_22 Testing/Microphone_R_Test2_Trial2.wav")
three_sec = 3000
# 3-6, 9-12, 15-18, 21-24, 27-30
exhalations = recording[three_sec:2*three_sec]
for i in range(3, 10, 2):
	print(three_sec*i, " ", three_sec*(i+1))
	exhalations += recording[three_sec * i : three_sec * (i + 1)]
exhalations.export("exhalations_cut.wav", format = "wav")