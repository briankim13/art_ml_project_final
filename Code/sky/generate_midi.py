from midiutil import MIDIFile
import numpy as np 

degrees  = []  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

data = np.loadtxt("note_to_make_midi.txt",dtype = 'int')
for d in data:
	degrees.append(d) 

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)
# MyMIDI.deinterleave = False 


for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("midifile.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)