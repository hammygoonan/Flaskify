(function($){
    var player = document.getElementById('player');
    var album_list = document.getElementById('albums');
    var playlist_ui = document.getElementById('playlist');
    var albums;
    var track_number;
    var playlist;
    var now_playing;

    document.onkeyup = function(e){
        if(e.keyCode == 32){
            if(player.paused && player.src){
                player.play();
            }
            else if(player.src){
                player.pause();
            }
            return false;
        }
    };

    document.onkeydown = function(e){
        if(e.keyCode == 32){
            return false;
        }
    };

    function req_listener(data) {
        albums = data.album;
        $(albums).each(function(idx){
            if(this.songs.length > 0){
                var li = $('<li />');
                var a = $('<a />');
                a.attr('href', '#');
                a.data('id', idx);
                a.addClass('list-group-item')
                a.click(play_album)
                a.html('<strong>' + this.artist + '</strong><br />' + this.name)
                li.append(a);
                $(album_list).append(li);
            }
        });
    }

    function play_album(){
        $('#albums .active').removeClass('active')
        $(this).addClass('active');
        playlist = albums[$(this).data('id')].songs;
        create_playlist();
        return false;
    }

    function create_playlist(){
        $(playlist_ui).html('');

        playlist.map(function(obj, idx){
            // console.log(idx);
            var playlist_item = $('<li />');
            playlist_item.html(
                '<strong>' + obj.title + '</strong></br />' +
                obj.artist + '<br />' +
                obj.album
            )
            playlist_item.data('id', idx)
            playlist_item.addClass('list-group-item')
            playlist_item.on('click', function(){
                if($(this).hasClass('active')){
                    return
                }
                $('#playlist .active').removeClass('active')
                $(this).addClass('active')
                track_number = idx;
                now_playing = playlist[track_number];
                $(player).attr('src', now_playing.path_to_static);
                play_next();
            });
            $(playlist_ui).append(playlist_item)
        })
    }

    function play_next(){
        setInterval(function(){
            if(player.ended){
                track_number++;
                var old = $('#playlist .active').removeClass('active');
                old.next().addClass('active')
                now_playing = playlist[track_number];
                player.src = now_playing.path_to_static
            }
        }, 500);
    }

    $.get('/albums', req_listener);
})(jQuery);
