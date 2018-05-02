<template lang="html">
  <div class="song">
    <a @click="addSong">{{ data.title }}</a>
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
  },
};
</script>
