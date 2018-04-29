<template lang="html">
  <div class="player">
    <audio controls="true" :src="src">{{ title }}</audio>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'player',
  props: ['song_id'],
  data() {
    return {
      src: '',
      title: '',
    };
  },
  mounted() {
    axios.get(`${process.env.API_URL}songs/${this.song_id}/`)
      .then((response) => {
        this.src = `${process.env.API_URL.slice(0, -1)}${response.data.src}`;
        this.title = response.data.title;
      });
  },
};
</script>
