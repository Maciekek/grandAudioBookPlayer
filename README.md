# Grand audio books reader 


## Description
Small program for Raspberry pi to play audio books for my grandmother. 


## How to run? 
```bash
    ./run.sh
```


### Additional things

-  how to change default volume of rasperry PI output?
```bash 
    alsamixer 
``` 
or 
```bash
    amixer sset PCM 100%
```


### Run script on startup

Edit `/etc/rc.local`


```bash
    sudo nano /etc/rc.local
```

Input 
```bash
/home/pi/grandAudioBookPlayer/app/run.sh &
```


### Merge mp3 files into one:
```bash
cat *.mp3 > all.mp3
```


### Split mp3 file into parts with audacity

You will need `Regular Interval Labels` plugin to audacity

Access to it by `Tools > Regular Interval Labels`

`Edit > Labeled audio > split`

Then `File > Export > Multiple`

