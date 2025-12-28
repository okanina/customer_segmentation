from moviepy.editor import VideoFileClip, vfx

clip = VideoFileClip("assets/part_2.mp4")
fast = clip.fx(vfx.speedx, 2)  # 2x speed
fast.write_gif("training_pipeline_short_2.gif", fps=10)
