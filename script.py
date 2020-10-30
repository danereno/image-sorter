import os

# Paste the directory of the source folder inside the following single quotes
# on Windows: click on folder > shift + right click > select Copy as Path (do not include copied double quotes)
src_folder = r''
# Paste the directory of the destination folder inside the following single quotes
# on Windows: click on folder > shift + right click > select Copy as Path (do not include copied double quotes)
dest_folder = r''

if src_folder == '' or dest_folder == '':
    raise ValueError('Please specify your source and destination folders')

folder_ct = 0
move_ct = 0
for img in os.listdir(src_folder):
    level = 0
    parens = []
    for i,c in enumerate(img):
        if c == '(':
            level += 1
            if level == 1:
                start = i+1
        elif c == ')':
            level -= 1
            if level == 0:
                parens.append(img[start:i])

    tags = parens[1].split('+')
    tag = tags[0].strip()
    for t in tags:
        if '(series)' in t:
            tag = t
    
    if tag =='original' or tag == 'misc':
        tag = '!Original'

    target_folder = os.path.join(dest_folder, tag)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        folder_ct += 1

    current_path = os.path.join(src_folder, img)
    target_path = os.path.join(target_folder, img)
    os.replace(current_path, target_path)
    move_ct += 1

print(folder_ct, 'folders created')
print(move_ct, 'files moved')
    


