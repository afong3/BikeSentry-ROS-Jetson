# Purpose: Take data from the microphone, preprocess the audio data for classification model input
# Python2.7
# Refer to Confluence: StopBikeTheft/Designs/ROS Designs/AudioManager

class AudioManager:
	def __init__(self, sample_rate):
		"""
		Initialize class with sample_rate of audio recordings.

		"""
		self.sample_rate = sample_rate

	def process_audio(self, raw_mic_data)
		"""
		raw_mic_data must be entered as a .wav file without lossy compression
		Returns: frequency data as a list 
		"""
		#TODO: insert all the process_audio things that are necessary 
		#TODO: make all the processing substantially faster because damn it's slow right now 
		next 
