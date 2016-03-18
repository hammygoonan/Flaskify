(function(){
    var player = document.getElementById('player');
    var album_list = document.getElementById('albums');
    var playlist_ui = document.getElementById('playlist');
    var albums;
    var track_number;
    var playlist;
    var now_playing;

    document.onkeyup = function(e){
        if(e.keyCode == 32){
            if(player.paused){
                player.play();
            }
            else{
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

    function json_ajax(url, success){
        var request = new XMLHttpRequest();
        request.addEventListener("load", success);
        request.responseType = "json"
        request.open("GET", url);
        request.send();
    }

    function req_listener() {
        albums = this.response.album
        albums.map(function(obj, index){
            if(obj.songs.length > 0){
                var li = document.createElement('li');
                var link = album_link(obj, index)
                li.appendChild(link);
                album_list.appendChild(li);
            }
        });
    }

    function album_link(obj, idx){
        var album_element = document.createElement('a');
        album_element.href = "#";
        album_element.dataset.id = idx
        album_element.className = 'list-group-item'
        album_element.onclick = play_album;
        var text = document.createTextNode(obj.artist + ' - ' + obj.name);
        album_element.appendChild(text)
        return album_element;
    }

    function play_album(){
        playlist = albums[this.dataset.id].songs;
        // track_number = 0;
        // now_playing = playlist[track_number];
        // player.src = now_playing.path.replace('/Users/hammy', '/static/music');
        create_playlist();
        return false;
    }

    function create_playlist(){
        playlist_ui.textContent = '';

        playlist.map(function(obj, idx){
            // console.log(idx);
            var playlist_item = document.createElement('li');
            var text = document.createTextNode(obj.name + ' (' + obj.artist + ')');
            playlist_item.appendChild(text);
            playlist_item.dataset.id = idx
            playlist_item.className = 'list-group-item'
            playlist_item.onclick = function(){
                if(this.classList.contains('active')){
                    return;
                }
                var active = document.getElementsByClassName('active')
                for (var i = 0; i < active.length; ++i) {
                    active[i].classList.remove('active')
                }
                playlist_item.classList.toggle('active');
                track_number = idx;
                now_playing = playlist[track_number];
                player.src = now_playing.path.replace('/Users/hammy', '/static/music');
                play_next();
            }
            playlist_ui.appendChild(playlist_item)
        })
    }

    function play_next(){
        setInterval(function(){
            if(player.ended){
                track_number++;
                var active = document.getElementsByClassName('active')
                var old_active = active[0]
                for (var i = 0; i < active.length; ++i) {
                    active[i].classList.remove('active');
                }
                old_active.nextSibling.classList.toggle('active');
                now_playing = playlist[track_number];
                player.src = now_playing.path.replace('/Users/hammy', '/static/music')
            }
        }, 500);
    }

    json_ajax('/albums', req_listener);
})();
