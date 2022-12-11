from pydub import AudioSegment
t1 = t1 * 1000 #milliseconds (t1 and t2 from old song)
t2 = t2 * 1000
newSound = AudioSegment.from_wav("old.wav")
newSound = newSound[t1:t2]
newSound.export('newSong.wav', format="wav") #export wav file

