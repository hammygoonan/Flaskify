<template>
  <div class="columns is-multiline">
    <div v-for="album in albums" :key="album.id" class="column is-2-desktop is-3-tablet">
      <album :data="album"></album>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Album from '@/components/Album';

export default {
  name: 'albums',
  components: { Album },
  data() {
    return {
      albums: [],
    };
  },
  mounted() {
    axios.get(`${process.env.API_URL}albums/`)
      .then((response) => {
        this.albums = response.data.collection;
      });
  },
};
</script>
