from youtube_transcript_api import YouTubeTranscriptApi
import scrapetube
import codext
import sys

if len(sys.argv) > 1:
  channelId = sys.argv[1]
else:
  channelId = "UClnw_bcNg4CAzF772qEtq4g"

videoListName = scrapetube.get_channel(channelId)
for video_id in videoListName:
  try:
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id['videoId'])
    transcript = transcript_list.find_generated_transcript(['en']).fetch()
    dscript = []
    for i in transcript:
      dscript.append(i['text'])
      message = ' '.join(dscript)
    with open("video-{}.txt".format(video_id['videoId']), 'w', encoding='utf-8') as fd:
      fd.write("https://www.youtube.com/watch?v={}".format(video_id['videoId']))
      fd.write("\n")
      fd.write(video_id['title']['runs'][0]['text'])
      fd.write("\n")
      fd.write(codext.encode(video_id['title']['runs'][0]['text'], "braille"))
      fd.write("\n")
      fd.write(codext.encode(message, "braille"))
      fd.close()
  except:
    pass
