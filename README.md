# What This Is

The project is to have a text-based dump of everything I know about A Link to the Past. I acknowledge that this is unlikely to ever materialize, but I think it will be fun and useful to do anyway. This is inspired in part by [Gwern](https://www.gwern.net/About)'s approach to a web of living essays.

# Why

Well, I need notes for myself, so why not upload them?

Additionally, text-based information on this game is _terribly_ lacking. I could edit the wiki, but it turns out that the pressure of writing something that matches my internal bar of "good enough for the wiki" prevents me from writing anything at all.

There is a vast amount of information out there, including in my own head, that exists only in video form and/or discord chatlogs. Videos are great for some things but incredibly inefficient in many ways. Also I just don't really like learning from videos. So the idea is to have a place for text explainers.

# The Process

Right now, the process is that I will write a page whenever I feel like doing so, up to whatever quality standard I feel inspired to reach that day. Additionally, I am tentatively offering to let [Twitch followers](https://twitch.tv/foxlisk) pick one room each. I will find some other mechanism for keeping it going (unless I decide to abandon it, I guess).

At some point I would like to organize the info better. Maybe I'll reach a point where I have a build process that fixes up links and images and shit. Maybe it'll just be a mess of markdown forever. No promises.

You can contribute by writing up a page of your own and providing a PR. Assuming it is correct and legible I will probably accept it; completeness is not required.

# Making Images/GIFs

Mostly, I've been doing a brief recording in OBS, trimming the video to size using the built-in Photos app on windows, chopping out the overlay stuff using VLC, and converting to gif on ezgif.com. This suuuuuuuuuucks but I don't feel like writing software for windows OR WSL, and tooling sucks, so whatever.

## VLC steps:

1. Go to Media -> Convert/Save
1. Select the relevant file
1. Click "Convert/Save" or select Convert from the little dropdown on that button
1. Select the "gameplay-from-stream-recording" conversion profile. Its settings:
  1. Encapsulation: mp4/mov
  1. Video codec: mp4, 9k bitrate, filters "video cropping filter" checked
  1. The "video cropping filter" parameters are set by going to "tools" -> "Preferences" -> selecting "all" in the bottom left, finding "video -> filters -> croppadd" and setting the values to:
    * top: 10
    * bottom: 12
    * left: 13
    * right: 497
1. Then select a destination file and do the conversion.

## ezgif steps:

1. Go to ezgif.com
1. Select Video to GIF (this is default option anyway it looks like)
1. Upload the video file VLC output
1. The trim should already be right
1. Size: 480xAUTO seems good
1. Frame rate: 20. 25 does not divide 30 so there's no point.
