from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
import ai



def parseUserInput(requestedVideo: str) -> str:
  """
  Extracts the YouTube video ID from a full URL or returns the ID if provided.
  
  Args:
    requestedVideo (str): A YouTube video URL or video ID

  Returns:
    str: The extracted YouTube video ID.
  """
  pattern = r"(?:v=|youtu\.be/|embed/|shorts/)([A-Za-z0-9_-]{11})"

  match = re.search(pattern, requestedVideo)
  
  if match:
      return match.group(1)  # Return the extracted video ID
  elif len(requestedVideo) == 11 and re.match(r"^[A-Za-z0-9_-]{11}$", requestedVideo):
      return requestedVideo  # Already an ID, return as is
  else:
      raise ValueError("Invalid YouTube link or video ID.")


def queryParseApi(link: str) -> str:
  try:
     resp = yta.get_transcript(link)

  except:
     raise ValueError('Unable to Fetch Transcript for Specified Video.\nPlease try again Later.')
  
  joined_str = ''

  for dict in resp:
    joined_str += dict['text']

  return joined_str
  

def queryAI(transcript: str) -> str:
  pass


def formatText(textCargo: str) -> None:
   print(textCargo.center(50, '_'), '\n')



def main():
  formatText('WELCOME TO VIDEOWORM')
  
  
  formatText('Please Input Desired Video to be Analyzed:')
  # usrInput = input()
  usrInput = 'https://www.youtube.com/watch?v=Q9uXOSGS8IQ'
  
  parsedUsrInput = parseUserInput(usrInput)
  
  try:
    transcript = queryParseApi(parsedUsrInput)
  except:
    pass

  analyzed_text = ai.analyzer(transcript)
  

  # Format OpenAI resp
  # Return Resp to User







if __name__ == '__main__':
  main()