import moviepy.editor as mp 

def compress(size, bit, f):
    SR = size
    BR = str(bit) + "k"
    video = mp.VideoFileClip(f)
    video_compressed = video.resize(height=SR)
    new_file = get_new_filename(f)
    video_compressed.write_videofile(new_file, bitrate=BR)

