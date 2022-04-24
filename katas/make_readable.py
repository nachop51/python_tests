def make_readable(seconds):
    # Do something
    
    hours = 0
    minutes = 0
    if seconds >= 3600:
        hours = int(seconds / 3600)
        seconds -= int(seconds / 3600) * 3600
    if seconds >= 60:
        minutes = int(seconds / 60)
        seconds -= int(seconds / 60) * 60
    
    if hours < 10:
        if hours != 0:
            hours *= 10
            hours = str(hours)
            hours = hours[::-1]
        else:
            hours = "00"
    if minutes < 10:
        if minutes != 0:
            minutes *= 10
            minutes = str(minutes)
            minutes = minutes[::-1]
        else:
            minutes = "00"
    if seconds < 10:
        if seconds != 0:
            seconds *= 10
            seconds = str(seconds)
            seconds = seconds[::-1]
        else:
            seconds = "00"
    return f"{hours}:{minutes}:{seconds}"

print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))

# I hate this, ridiculous
# best practice: 
# def make_readable(s):
#     return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)