import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
)

# TODO Make these files available on the local file system
# You may need to update the file paths
files = [
  upload_to_gemini("1miQlr2CP3JKH7eAdK171VfeFCK347V3Z", mime_type="application/octet-stream"),
]

response = model.generate_content([
  "What object is this? Describe how it might be used",
  "Object: The input is a PC hardware Image (any component related to computers)",
  "Description: only state the name of the hardware and its type(for example if a cpu just write intel i710th gen if it was like that, for the gpu the same), if the input is anything other than a pc hardware related stuff answer with i cant help you that",
  "Object: ",
  files[0],
  "​",
  "Description: ",
])

print(response.text)