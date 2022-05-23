from calendar import c
from manim import *
from TTS.TTS import get_mp3_file
from utils import cut, get_duration, get_web_text, get_actual_age_lunar
import time


class Video(Scene):

    def construct(self):
        # INFO 视频开头
        CAKE = ImageMobject("./media/images/icon/cake.png").scale(1.5).to_edge(
            UP, buff=2)
        username = "林晓晓"
        age = get_actual_age_lunar((1997, 6, 24))
        text = username+"，生日快乐！"
        get_mp3_file(text, "./media/sounds/happy_birthday.mp3")
        self.play(FadeIn(CAKE, run_time=0.1))
        text = Text(text, font="Coca-Cola Care Font", color="#FEB19A").scale(0.7).next_to(CAKE,DOWN,buff=1)
        self.add_sound("./media/sounds/happy_birthday.mp3",time_offset=1)
        self.play(Write(text), run_time=1)
        self.wait(3)
        self.play(FadeOut(CAKE, text))
        # INFO 主视频内容
        
        self.text = get_web_text()
        contents = self.text[1:]
        
        for content in contents:
            audio_path = "./media/sounds/video_content_" + str(
                round(time.time() * 1000))
            # content = deal_text(content)
            get_mp3_file(text=content, output_path=audio_path)
            audio_path = audio_path + ".mp3"
            audio_time = get_duration(audio_path)
            content = MarkupText(content,
                                 font="Coca-Cola Care Font",
                                 font_size=60,
                                 justify=True, color="#FEB19A").scale(0.5)
            self.add_sound(audio_path, time_offset=1)
            self.play(FadeIn(content), run_time=len(content)//50)
            self.wait(audio_time)
            self.play(FadeOut(content))
            break

