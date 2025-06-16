simple html, css, and javascript (i will be the one to create this)

will use flask 


the app will convert the sound on my computer (i will run this app on background (there is a start button) and i will play a sound clip on my computer and the app will type the converted sound on the computer). The format of the text should be like this

'''
Hi Austin. How are you?

I'm fine. Okay... So today, Rajiv could you first introduce yourself a little bit?

Sure. Well I'm a Telecom ____ here. I graduated sometime in 1999. And after that I worked for some various companies out here. My last company that I worked for was Lucent. And then after that I started off on my own. And for the past two years I've been trying to do this Sedna Wireless thing. As part of Sedna Wireless we released Call Graph.

Okay. The reason that I know your company, Sedna Wireless is because this product Call Graph, yeah, I think that's, if I think correctly it's kind of like Skype recorder. It's like a plugin for Skype, right.

It is a call recording application for Skype. It works in the background and it records all your calls into an mp3 file. And then you can play it back, you can search through your call records. It's basically meant for... It's a productivity application. Somebody who would like to have records of his calls, he can use our software.

Yes. And the reason that I found it interesting is that, I'm not sure if you aware of this fact, your software Call Graph seems to be the only one that can be used for free! And with the functionality of Stereo. What I mean is that your software Call Graph can record the conversation into separate audio tracks. So that will be perfect choice for Podcasts. Because most of the ___ come into the situation that the two people have different volumes. So it will be very very hard to do the modification, to do the post production.

Right. That's true. We record it in separate tracks which makes it very easy to edit the files. You can use any external audio editor. For example, Audacity is a very good audio editor. And you can export the tracks separately. Plus there is also a feature in which you can record the calls in a wav file. So if you do record the calls in a wav file then you don't lose any quality. The quality is maintained, of the call.

Yes. So I think, frankly there are other software in the market that provide the same functionality of separate tracks. But they all require, a little bit registration fee. So it's a very very outstanding point, from my point of view.

Yes. Great that you like Call Graph.

So I think you should emphasize this point. I actually spent several days to search through the Internet about Skype recording solutions. And I was very surprised that Call Graph was not mentioned very much. It only has 50,000 Google hits, compared to other software, maybe several million hits.

Well one of the reason is that we released it recently, it's around just two months old. And it got covered by a few popular weblogs, few popular Blogs. For example LifeHacker covered us. And DownloadSquad covered us. But I guess it takes some time to spread through the Google's network.

'''

meaning, per speaker is per paragraph, so the app must identify how many speaker(person are there)

also, here are some needed to highlight:

-The transcript is broken into paragraphs on each change of speaker. Each speakers continuous diction is on one single paragraph and paragraphs are separated by empty lines.
-Inaudible parts are marked with a blank, ____ to make it stand out from the rest of the transcript. These blanks may or may not get filled during review, but are always checked.

also, here are some transciption guidelines that needs to be followed:

The raw transcript should not contain text other than the spoken audio. No headers/footers, speaker tracking, time-codes, comments etcetera.
No part of the audio should be omitted, unless specified otherwise by an instruction or another guideline.
Inaudible parts should be omitted and marked with a blank ____.
Laughter should be omitted and marked with [laughter] or [chuckle].
Ellipsis ... should be used to indicate unfinished sentences or mid-sentence pauses.
Contractions, wanna, gonna, kinda, gotta, should not be expanded.
Numbers one to nine should be transcribed in letters and numerals otherwise, except for measurements.
A new paragraph should be started at each change of speaker and paragraphs should be separated by an empty line.
Fillers (right, you know, I think, like, I mean, so, actually, basically), false starts, stutters and partial words should be omitted, except for strict verbatim files.
Utterances should be omitted for non-strict verbatim files, unless necessary. For strict verbatim files, only the following utterances should be transcribed: Mm-hmm if in agreement, Uh-huh if in disagreement, Umm and Uh.
Additional Notes:

Strict verbatim files are indicated with an instruction. Files without the instruction should be considered as non-strict verbatim.
Blanks that are filled during the Review, Proofreading and QC steps are considered as major mistakes (except for names and acronyms).
For Guideline VII, measurements are considered as anything which has a unit (kg, ml, currency units, etcetera).
For Guideline IX, the filler words specified have to be frequently repeated by a speaker during the conversation to be considered a filler. In-frequent usage of those words should be transcribed.
False starts are when the speaker starts a statement but immediately corrects it to something else.
For Guideline IX, all files are non-strict verbatim by default. Strict verbatim files are indicated by an instruction on the file. Therefore if the instruction is not present, all utterances, fillers, false starts, stutters should be omitted. If the instruction is present, nothing should be omitted and the raw transcript should match the audio word for word.
The only case when an utterance is required in a non-strict verbatim file is when it is a response to a direct question. The unless necessary part of Guideline X specifies that.

Style Suggestions:

The following are some styles that we recommend. Please note that this list is not exhaustive. If you require additional guidance, please contact support.

Punctuations are free style. Please use your discretion on placement of commas, periods, semicolons, exclamations etc.
Spelling styles are different for each file and the styles suggested by the spell check should be followed.
All proper nouns should be first letter capitalized, e.g., names of places, person, organizations, job titles, etcetera.
Spelled out names should be all capitalized and separated by hyphens. E.g. A-D-A-M.
Use etcetera instead of etc.
Use i.e., instead of ie.
Use e.g., instead of Eg.
Alright and All right are both acceptable.
A statement can begin with an And.
Generic drug names should be all lowercase and branded drug names should be first letter capitalized. Google once to check if they are generic or branded.
Special marking schemes for phonetics and spelling should not be used. Blanks should be used instead.
Periods should not be used in acronyms. E.g. PhD instead of Ph.D.
The following examples further illustrates Transcription Guideline VII.
Time: 10:00 AM
Date: March 2, 2012
Temperature: 5 degrees
Money: $5, $500,000, $5 Billion
Percentage: 5%
Speed: 5 miles per hour
Dimension: 6 x 10, 5 feet 2 inches
Address: 213 2nd Street
Era: in your 20s, in the '90s
Rank: ninth, 10th

at the bottom of the converted text container on the UI, there is a convert to txt file button and copy button

with these, do i need to create an AI bot?


remove the container design on the title and upload shits
also improve the design of the choose file and input text
make the text container bigger with scroll feature on the right (the text must be not too big)
put margin between the text cont and tot he buttons

the format must be

AUDIO TO TEXT CONVERTER

CHOOSE FILE button

ENTER FILE name (WHITE BG, NOT OUTLINE)

TEXT container

BUTTONS
