# import whisper
# import sounddevice as sd
# import numpy as np
# from isapi.samples.redirector_asynch import CHUNK_SIZE
# from networkx.algorithms.shortest_paths.unweighted import single_target_shortest_path_length
# from whisper.audio import SAMPLE_RATE
#
# model= whisper.load_model('base', device='cpu')
#
# def get_audio():
#     SAMPLE_RATE = 16000
#     SILENCE_TRESHOLD = 0.001
#     SILENCE_DURATION = 2
#     CHUNK_SIZE = 1024
#     audio_chunks = []
#     silence_chunks = 0
#     speaking_starting = False
#     chunks_for_silence = int(SILENCE_DURATION * SAMPLE_RATE / CHUNK_SIZE)
#     print(chunks_for_silence)
#     # print("Speak")
#     with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="float32", blocksize=CHUNK_SIZE) as stream:
#         while True:
#             chunk, _ = stream.read(CHUNK_SIZE)
#             volume = np.abs(chunk).mean()
#             print(volume)
#             if volume > SILENCE_TRESHOLD:
#                 speaking_starting = True
#                 silence_chunks = 0
#                 audio_chunks.append(chunk)
#             elif speaking_starting:
#                 silence_chunks += 1
#                 audio_chunks.append(chunk)
#                 if silence_chunks >= chunks_for_silence:
#                     print("Silence detected")
#                     break
#     return np.concatenate(audio_chunks).flatten()
#
# def get_transcribe():
#     audio = get_audio()
#     return model.transcribe(audio, fp16=False)
# result =get_transcribe()
# print(result["text"])