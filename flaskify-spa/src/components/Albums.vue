<template>
  <div>
    <div class="columns is-multiline is-mobile">
      <div
        v-for="album in albums"
        :key="album.id"
        class="column is-2-desktop is-3-tablet is-6-mobile"
      >
        <album :data="album"></album>
      </div>
    </div>
    <button class="button" @click="loadMore">Load more</button>
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
      page: 1,
    };
  },
  mounted() {
    axios.get(`${process.env.API_URL}albums/`)
      .then((response) => {
        this.albums = response.data.collection;
      });
  },
  methods: {
    loadMore() {
      this.page += 1;
      axios.get(`${process.env.API_URL}albums/?p=${this.page}`)
        .then((response) => {
          this.albums = this.albums.concat(response.data.collection);
        });
    },
  },
};
</script>
