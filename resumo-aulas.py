import openai
import speech_recognition as sr
import subprocess
import os
from pydub import AudioSegment
import env
# Configurar a chave API da OpenAI
openai.api_key = '.env'

def converter_audio(audio_path):
    try:
        print(f"Convertendo áudio: {audio_path}")
        output_path = "temp.wav"
        # Verifica se o ficheiro existe e remove-o
        if os.path.exists(output_path):
            os.remove(output_path)
        command = f"ffmpeg -i \"{audio_path}\" -ar 16000 -ac 1 {output_path}"
        subprocess.run(command, shell=True, check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"Erro ao converter áudio: {e}")
        raise

def dividir_audio(wav_path, chunk_length_ms=60000):
    try:
        audio = AudioSegment.from_wav(wav_path)
        audio_chunks = [audio[i:i+chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
        
        chunk_files = []
        for i, chunk in enumerate(audio_chunks):
            chunk_file = f"chunk_{i}.wav"
            chunk.export(chunk_file, format="wav")
            chunk_files.append(chunk_file)
        
        return chunk_files
    except Exception as e:
        print(f"Erro ao dividir o áudio: {e}")
        raise

def transcrever_audio_chunks(chunk_files, language="en-US"):
    recognizer = sr.Recognizer()
    transcricao = ""
    
    for chunk_file in chunk_files:
        try:
            with sr.AudioFile(chunk_file) as source:
                audio_data = recognizer.record(source)
                texto = recognizer.recognize_google(audio_data, language=language)
                transcricao += texto + " "
        except sr.UnknownValueError:
            print(f"Erro: Google Speech Recognition não conseguiu entender o áudio no ficheiro {chunk_file}")
        except sr.RequestError as e:
            print(f"Erro: Não foi possível solicitar os resultados do serviço de reconhecimento de fala do Google; {e}")
    
    return transcricao.strip()

def transcrever_audio(audio_path, language="en-US"):
    try:
        print(f"Transcrevendo áudio: {audio_path}")
        wav_path = converter_audio(audio_path)
        chunk_files = dividir_audio(wav_path)
        texto = transcrever_audio_chunks(chunk_files, language)
        
        for chunk_file in chunk_files:
            os.remove(chunk_file)
        
        print(f"Texto transcrito: {texto}")
        return texto
    except Exception as e:
        print(f"Erro ao transcrever áudio: {e}")
        raise

def resumir_texto(texto):
    try:
        print(f"Resumindo texto: {texto}")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente útil que resume textos."},
                {"role": "user", "content": f"Resuma o seguinte texto em português de Portugal: {texto}"}
            ]
        )
        
        resumo = response['choices'][0]['message']['content'].strip()
        print(f"Resumo: {resumo}")
        return resumo
    except openai.error.OpenAIError as e:
        print(f"Erro na API da OpenAI: {e}")
        raise
    except Exception as e:
        print(f"Erro ao resumir texto: {e}")
        raise

def dividir_texto_em_topicos(texto):
    try:
        print(f"Dividindo texto em tópicos: {texto}")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente útil que divide textos em tópicos."},
                {"role": "user", "content": f"Divida o seguinte texto em tópicos: {texto}"}
            ]
        )
        
        topicos = response['choices'][0]['message']['content'].strip()
        print(f"Tópicos: {topicos}")
        return topicos
    except openai.error.OpenAIError as e:
        print(f"Erro na API da OpenAI: {e}")
        raise
    except Exception as e:
        print(f"Erro ao dividir texto em tópicos: {e}")
        raise

def main(audio_path):
    try:
        language = "en-US"  # Ajuste o idioma conforme necessário
        texto = transcrever_audio(audio_path, language)
        if texto:
            with open("transcricao.txt", "w", encoding="utf-8") as f:
                f.write(texto)
            print("Transcrição escrita no ficheiro transcricao.txt")

            resumo = resumir_texto(texto)
            if resumo:
                print("Texto Original:", texto)
                print("Resumo:", resumo)
                
                with open("resumo.txt", "w", encoding="utf-8") as f:
                    f.write(resumo)
                print("Resumo escrito no ficheiro resumo.txt")
            else:
                print("Erro: O resumo está vazio.")
            
            topicos = dividir_texto_em_topicos(texto)
            if topicos:
                with open("topicos.txt", "w", encoding="utf-8") as f:
                    f.write(topicos)
                print("Tópicos escritos no ficheiro topicos.txt")
            else:
                print("Erro: Os tópicos estão vazios.")
        else:
            print("Erro: O texto transcrito está vazio.")
    except Exception as e:
        print(f"Erro no processo principal: {e}")

# Substitua 'a_sua_chave_api_aqui' pela sua chave de API
main(r"C:\Users\liand\Downloads\15 crazy new JS framework features you dont know yet.mp3")
