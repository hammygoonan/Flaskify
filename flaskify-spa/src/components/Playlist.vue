<template lang="html">
  <nav class="navbar is-warning is-fixed-top" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <h1 class="title is-4 is-marginless"><a>Flaskify</a></h1>
      <a role="button"
        class="navbar-burger"
        :class="{ 'is-active': display }"
        aria-label="menu"
        aria-expanded="false"
        @click="display = true"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
      <div class="playlist" v-if="display">
        <button class="delete" aria-label="close" @click="display = false"></button>
        <h3 class="title is-6">Playlist</h3>
        <ul>
          <draggable v-model="songs" :options="{draggable:'li'}">
            <li
              v-for="(song, idx) in songs"
              :key="idx"
              draggable="true"
              style="position: relative"
            >{{ song.title }} - <strong>{{ artists(song.artists) }}</strong>
            <button class="delete is-small plist-delete" @click="deleteSong(idx)"></button></li>
          </draggable>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import draggable from 'vuedraggable';

export default {
  name: 'playlist',
  data() {
    return {
      display: false,
    };
  },
  components: { draggable },
  computed: {
    songs: {
      get() {
        return this.$store.state.playlist;
      },
      set(value) {
        this.$store.commit('reorder', value);
      },
    },
  },
  methods: {
    artists(artists) {
      return artists.reduce((artistList, artist) => artistList + artist.name, '');
    },
    deleteSong(idx) {
      this.$store.commit('deleteSong', idx);
    },
  },
};
</script>
