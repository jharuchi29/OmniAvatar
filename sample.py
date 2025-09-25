
import librosa
import soundfile as sf
import os

def resample_audio(input_file, output_file, target_sr=16000):
    """
    Read an audio file, resample it to target sampling rate, and save it.
    
    Parameters:
    input_file (str): Path to input audio file
    output_file (str): Path to output audio file
    target_sr (int): Target sampling rate (default: 16000)
    """
    try:
        # Read the audio file (librosa automatically loads as mono by default)
        audio_data, original_sr = librosa.load(input_file, sr=None)
        
        print(f"Original sampling rate: {original_sr} Hz")
        print(f"Audio duration: {len(audio_data) / original_sr:.2f} seconds")
        
        # Resample if needed
        if original_sr != target_sr:
            print(f"Resampling from {original_sr} Hz to {target_sr} Hz...")
            audio_resampled = librosa.resample(audio_data, 
                                             orig_sr=original_sr, 
                                             target_sr=target_sr)
        else:
            print("No resampling needed - already at target rate")
            audio_resampled = audio_data
        
        # Save the resampled audio
        sf.write(output_file, audio_resampled, target_sr)
        print(f"Saved resampled audio to: {output_file}")
        print(f"New sampling rate: {target_sr} Hz")
        
    except Exception as e:
        print(f"Error processing audio file: {e}")

# Example usage
if __name__ == "__main__":
    # Specify input and output file paths
    input_file = "case_2_01-10sec.wav"  # Change this to your input file
    output_file = "output_audio_16k.wav"  # Change this to your desired output file
    
    # Check if input file exists
    if os.path.exists(input_file):
        resample_audio(input_file, output_file, target_sr=16000)
    else:
        print(f"Input file '{input_file}' not found!")