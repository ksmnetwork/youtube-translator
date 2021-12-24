from youtube_transcript_api import YouTubeTranscriptApi
import scrapetube
import codext

videoListName = scrapetube.get_channel("UClnw_bcNg4CAzF772qEtq4g")

for video_id in videoListName:
    try:
      transcript_list = YouTubeTranscriptApi.list_transcripts(video_id['videoId'])
      transcript = transcript_list.find_generated_transcript(['en']).fetch()
      dscript = []

      for i in transcript:
        dscript.append(i['text'])
        message = ' '.join(dscript)

      video = "https://www.youtube.com/watch?v={}".format(video_id['videoId'])
      title = video_id['title']['runs'][0]['text']
      filename = "video-{}.txt".format(video_id['videoId'])

      print(video, '\n', title, '\n', codext.encode(title, "braille"), '\n', codext.encode(message, "braille"), '\n\n')

      with open(filename, 'w') as fd:
        fd.write(video)
        fd.write("\n")
        fd.write(title)
        fd.write("\n")
        fd.write(codext.encode(title, "braille"))
        fd.write("\n")
        fd.write(codext.encode(message, "braille"))
        fd.close()

    except:
        pass
