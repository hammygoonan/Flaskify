import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);


export default new Vuex.Store({
  state: {
    playlist: [],
    playing: {},
    page: 1,
  },
  mutations: {
    addToPlaylist(state, song) {
      state.playlist.push(song);
      if (Object.keys(state.playing).length === 0) {
        state.playing = state.playlist.shift();
      }
    },
    playSong(state, song) {
      state.playing = song;
    },
    nextSong(state) {
      if (state.playlist.length > 0) {
        state.playing = state.playlist.shift();
      } else {
        state.playing = {};
      }
    },
    reorder(state, value) {
      state.playlist = value;
    },
    deleteSong(state, idx) {
      state.playlist.splice(idx, 1);
    },
  },
});
