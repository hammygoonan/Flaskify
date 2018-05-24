<template lang="html">
  <div class="song">
    <a @click="addSong" class="is-small">
      {{ data.title }}
      <span class="artist"> - {{ artists(data.artists) }}</span>
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
    },
    artists(artists) {
      return artists.reduce((artistList, artist) => artistList + artist.name, '');
    },
  },
};
</script>
