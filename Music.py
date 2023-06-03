import speech_recognition as sr
import pygame

pygame.init()

# 음악 파일 경로
music_file = 'C:\\play_music_gader\\eco-technology-145636.mp3'

# 음악 재생 상태 변수
is_playing = False

# 음악 재생 함수
def play_music():
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    global is_playing
    is_playing = True

# 음악 멈춤 함수
def stop_music():
    pygame.mixer.music.stop()
    global is_playing
    is_playing = False

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("음성을 입력하세요:")
        audio = r.listen(source)
    try:
        user_input = r.recognize_google(audio, language="ko-KR")
        return user_input
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"Google Speech Recognition 서비스에 오류가 발생했습니다: {e}")

def main():  
    # 사용자 입력 받기
    while True:
        user_input = speech_to_text()

        if user_input == '재생':
            if not is_playing:
                play_music()
                print("음악이 재생되었습니다.")
            else:
                print("이미 음악이 재생 중입니다.")
        elif user_input == '멈춰':
            if is_playing:
                stop_music()
                print("음악이 멈췄습니다.")
            else:
                print("음악이 이미 멈춰있습니다.")
        elif user_input == '나가':
            quit()
        else:
            print("인식된 명령어가 없습니다. '재생' 또는 '멈춰' 또는 '나가'을 말해주세요.")


if __name__ == "__main__":
    main()
