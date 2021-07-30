from pydub import AudioSegment

filepath = "/Users/kabirjolly/Library/Mobile Documents/com~apple~CloudDocs/Microphone Recordings/7_22 Testing/Microphone_R_Test2_Trial2.wav"
recording = AudioSegment.from_wav(filepath)
three_sec = 3000
# 3-6, 9-12, 15-18, 21-24, 27-30
exhalations = recording[three_sec:2*three_sec]
cut_num = 1
print(f"Cut {cut_num}: ", three_sec, " ", three_sec * 2)
cut_num += 1
for i in range(3, 10, 2):
	print(f"Cut {cut_num}: ", three_sec * i, " ", three_sec * (i+1))
	exhalations += recording[three_sec * i : three_sec * (i + 1)]
	cut_num += 1
try:
	exhalations.export(f"exhalations_only_{filepath.split('/')[-1]}", format = "wav")
	print("Export successful!")
except:
	print("Export was NOT successful")