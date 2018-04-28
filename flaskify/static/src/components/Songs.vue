<template lang="html">
  <div class="columns is-multiline is-mobile">
    <song v-for="song in songs" :item="song" :key="song.id"></song>
  </div>
  </div>
</template>

<script>
import Song from './Song.vue';
import axios from 'axios';

export default {
  name: 'songs',
  data() {
    return {
      songs: [],
    };
  },
  components: { Song },
  mounted() {
    axios.get('/songs/')
      .then((response) => {
        this.songs = response.data.items;
      })
  },
};
</script>
