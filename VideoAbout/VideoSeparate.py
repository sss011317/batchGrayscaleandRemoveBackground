# pip install moviepy 
from moviepy.video.io.VideoFileClip import VideoFileClip
def VideoSeparate(videoName,fileType,startTime,endTime):
    
    Time = "-start-" + str(startTime) + " -End-" + str(endTime) +"  - "
    input_video = './%s%s' %(videoName,fileType)
    output_video = './%s%s%s' %(videoName,Time,fileType)
    with VideoFileClip(input_video) as video:
        video_clip = video.subclip(startTime, endTime)
        video_clip.write_videofile(output_video, audio_codec='aac')

if __name__=='__main__':
    videoName = input("videoName:")
    fileType = '.mp4'
    startTime = input("StartTime:")
    endTime = input("EndTime:")
    VideoSeparate(videoName,fileType,startTime,endTime)