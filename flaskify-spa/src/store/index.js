import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);


export default new Vuex.Store({
  state: {
    playlist: [],
    playing: {},
  },
  mutations: {
    addToPlaylist(state, song) {
      state.playlist.push(song);
      if (Object.keys(state.playing).length === 0) {
        state.playing = state.playlist.pop();
      }
    },
    playSong(state, song) {
      state.playing = song;
    },
    nextSong(state) {
      if (state.playlist.length > 0) {
        console.log('nextSong');
        state.playing = state.playlist.pop();
      }
    },
  },
});
