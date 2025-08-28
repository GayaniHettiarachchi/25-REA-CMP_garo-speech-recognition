# Charlie Redmon
# 2025-08-10
# Download audio and text bulletins from sample set

#%%

import os
import requests 
import pandas as pd
from tqdm import tqdm 
from pydub import AudioSegment

# dirs
audio_dir = "../dat/AIR/audio/"

# data
d = pd.read_csv('../dat/proc/audio-bulletins.csv')
d = d[d.Language == 'Garo']
d = d[d.URL != 'nan']
d = d.reset_index()

# loop through and download files
for i in tqdm(range(0, d.shape[0])):

    ilang = str(d.loc[i, 'Language'])
    icity = str(d.loc[i, 'Station'])
    idate = str(d.loc[i, 'Date'])
    itime = str(d.loc[i, 'Time'])
    aurl = str(d.loc[i, 'URL'])

    fn = "_".join([ilang, icity, idate, itime]) 
    audiofn = fn + ".mp3" 

    # download audio
    r = requests.get(aurl)
    with open(os.path.join(audio_dir, audiofn), 'wb') as f:
        f.write(r.content)
    



# %%
