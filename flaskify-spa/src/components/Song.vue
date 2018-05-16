<template lang="html">
  <div class="song">
    <a @click="addSong" class="is-small">
      {{ data.title }} - <strong>{{ artists(data.artists) }}</strong>
    </a>
  </div>
</template>

<script>
export default {
  name: 'song',
  props: ['data'],
  methods: {
    addSong() {
      this.$store.commit('addToPlaylist', this.data);
      // this.$store.commit('playSong', this.data);
    },
    artists(artists) {
      return artists.reduce((artistList, artist) => artistList + artist.name, '');
    },
  },
};
</script>
