d = {"john":40, "peter":45} 
print(d["john"])

all_albums=Album.objects.all()
    html=''
    for album in all_albums:
        url='/myapp/'+ str(album.id) + '/'