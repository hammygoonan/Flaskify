<template lang="html">
  <div class="song">
    <a @click="addSong">
      {{ data.title }}
      <span class="artist"> - {{ artists }}</span><br />
      <small>{{ album }}</small>
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
  },
  computed: {
    album() {
      if ('albums' in this.data) {
        return this.data.albums[0].title;
      }
      return '';
    },
    artists() {
      return this.data.artists.reduce((artistList, artist) => artistList + artist.name, '');
    },
  },
};
</script>
