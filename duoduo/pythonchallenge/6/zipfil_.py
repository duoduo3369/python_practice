import zipfile
z = zipfile.ZipFile("channel.zip", "r")
next_fn = '90052'
suffix = '.txt'
comments = []
def get_next_fn(s):
    return s.split()[-1]
while 1:
    try:
        fname = next_fn+suffix
        print fname,
        comments.append(z.getinfo(fname).comment)
        s = z.read(fname)
        print s
        next_fn = get_next_fn(s)
    except:
        break

print ''.join(comments)
