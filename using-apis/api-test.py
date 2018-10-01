
import musicbrainzngs
import sys

musicbrainzngs.set_useragent('MyMusicBrainzAPITest', 1.0)

def get_artist_place_of_origin(artist_name):
    artist = musicbrainzngs.search_artists(artist_name)
    try:
        origin_country = artist['artist-list'][0]['area']['name']
    except:
        print('Either the artist or their origin cannot be found!')
        exit()
    return origin_country


def get_genre_tags(artist_name):
    artist = musicbrainzngs.search_artists(artist_name)
    try:
        tag_list = artist['artist-list'][0]['tag-list']
    except:
        print('Either the artist or their genre tags cannot be found!')
        exit()
    final_tag_list = []
    for i in range(len(tag_list)):
        final_tag_list.append(tag_list[i]['name'])

    return final_tag_list

def main():
    print('This program allows you to find the place of origin of a musical artist, or retrieve a list of genres associated with the artist.')
    artist = input("First, please enter the name of an artist: ")
    origin_or_genres = input('Now, enter either "o" to find their place of origin, or "g" to get a list of genres: ')
    while (origin_or_genres != 'o') and (origin_or_genres != 'g'):
        origin_or_genres = input('Please enter either "o" to get origin or "g" to get genres: ')

    if origin_or_genres == 'o':
        print('The place of origin of ' + artist + ': ' + get_artist_place_of_origin(artist))
    elif origin_or_genres == 'g':
        genre_list = get_genre_tags(artist)
        genre_list_string = ''
        for i in range(len(genre_list) - 2):
            genre_list_string += genre_list[i] + ', '
        genre_list_string += genre_list[len(genre_list) - 1]
        print('The following genres are associated with ' + artist + ' : '+ genre_list_string)

main()