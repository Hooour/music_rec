#!/bin/bash
# convert mp3 to wav
for filename in ./input_mp3/*.mp3;
	do name=`echo "${filename%.*}"`;
	echo $name;
	ffmpeg -i $filename $name.wav;
done

mv input_mp3/*.wav output_wav/