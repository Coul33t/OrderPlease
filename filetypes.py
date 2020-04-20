FILETYPES = {
    'images': ('jpg', 'gif', 'png', 'bmp', 'tif', 'tiff'),
    'videos': ('flv', 'mp4', '3gp', 'wmv'),
    'music': ('mp3', 'flac', 'wav'),
    'ebook': ('epub', 'mobi'),
    'documents': ('pdf', 'txt', 'odt', 'ods', 'docx', 'doc', 'xlsx', 'bib', 'rtf'),
    'executables': ('exe'),
    'torrents': ('torrent'),
    'programming': ('py', 'cpp', 'c', 'h', 'p8', 'js', 'java', 'php'),
    'tablatures': ('gp5'),
    'archive': ('7z', 'zip', 'rar', 'tar', 'gz', 'tgz', 'jar'),
    'web': ('htm', 'html', 'css'),
    'others': None
}

REVERSED_FILETYPES = {
    'jpg,gif,png,bmp,tif,tiff': 'images',
    'flv,mp4,3gp,wmv': 'videos',
    'mp3,flac,wav': 'music',
    'epub,mobi': 'ebook',
    'pdf,txt,odt,ods,docx,doc,xlsx,bib,rtf': 'documents',
    'exe': 'executables',
    'torrent': 'torrents',
    'py,cpp,c,h,p8,js,java,php': 'programming',
    'gp5': 'tablatures',
    '7z,zip,rar,tar,gz,tgz,jar': 'archive',
    'html,html,css': 'web'
}