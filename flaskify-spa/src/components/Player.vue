<template lang="html">
  <div class="player">
    <audio
      :src="src"
      autoplay
      controls
      @ended="ended"
      @timeupdate="timeupdate"
    >{{ song.title }}</audio>
  </div>
</template>

<script>
export default {
  name: 'player',
  data() {
    return {
      currentTime: 0,
    };
  },
  computed: {
    song() {
      return this.$store.state.playing;
    },
    src() {
      if (Object.keys(this.$store.state.playing).length === 0) {
        return '';
      }
      return `${process.env.API_URL.slice(0, -1)}${this.$store.state.playing.src}`;
    },
  },
  methods: {
    ended() {
      this.$store.commit('nextSong');
    },
    timeupdate(a) {
      this.currentTime = a.target.currentTime / a.target.duration;
    },
  },
};
</script>
