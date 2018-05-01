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
    },
    playSong(state, song) {
      state.playing = song;
    },
  },
});
