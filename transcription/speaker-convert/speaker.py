import json

def update_tok(sample):
  sample['text'] = sample['alternatives'][0]['content'].rjust(len(sample['alternatives'][0]['content'])+2, ' ')

  sample['confidence'] = sample['alternatives'][0]['confidence']
  del sample['alternatives']
  return sample


def get_speakers(filepath):
    #loading file
    joe_aws = open(filepath)
    joe_aws = json.load(joe_aws)

    #generating speaker data
    speaker = []
    for item in joe_aws['results']['speaker_labels']['segments']:
      speaker.extend(item['items'])

    #generating token data
    temp_token = joe_aws['results']['items']
    token = []
    for item in temp_token:
      if len(item)==4: token.append(item)

    #decoding from speakers and tokens
    prev_speaker = 'spk_0'
    script = ""
    change_count = 0
    txt = 'spk_'
    id2wrds = []
    words_list = []
    start_time = speaker[0]['start_time']
    for tok, speak in zip(token, speaker):
      tok = update_tok(tok)
      current_speaker = speak['speaker_label']
      if current_speaker != prev_speaker: #condition for change in speaker
        # temp = {'speaker': prev_speaker,'words':words_list, 'start_time': start_time, 'end_time': end_time}
        temp = {'speaker': txt+str(change_count),'words':words_list, 'start_time': start_time, 'end_time': end_time}
        start_time = speak['start_time']
        id2wrds.append(temp)
        change_count += 1
        # script = ""
        words_list = []
      end_time = speak['end_time']
      # script = script + tok['alternatives'][0]['content']+" "
      # script = script + tok['text']
      words_list.append(tok)
      prev_speaker = current_speaker
    # temp = {'speaker': prev_speaker,'words':words_list, 'start_time': start_time, 'end_time': end_time}
    temp = {'speaker': txt+str(change_count),'words':words_list, 'start_time': start_time, 'end_time': end_time}
    id2wrds.append(temp)  
    return id2wrds



p=get_speakers("sp.json")


json_object = json.dumps(p) 
# json_object = json.dumps(p, indent = 4) 


# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 












