# sometimes when discord updates, they switch out a bunch of classes for new names
# this script replaces those in the css file using someone elses' gist
# can be modified to support other formats, but for the gist it was OLDCSS = NEWCSS on each lines, so this is how i wrote this
import requests
import io

url = "https://gist.githubusercontent.com/ExperiBass/2375ac4f7088bb9410d81cd59495f462/raw/926cf7df2710a23c03786d82f963ec97f90bf39e/Discord_Class_Name_Conversion_1-10-22.txt"
r = requests.get(url)

cssfile = "discordclassic.theme.css.old"
css = ""

with open(cssfile, 'r', encoding='utf-8') as f:
    css = f.read()

lines = r.text.splitlines()

for line in lines:
    xline = line.split(" = ")

    if(xline[0] in css):
        print("found" + xline[0] + " in css. replacing with " + xline[1] + ".")
        css = css.replace(xline[0], xline[1])


file = "discordclassic-fixed.theme.css"
with open(file, "w", encoding='utf-8') as f:
    f.write(css)
