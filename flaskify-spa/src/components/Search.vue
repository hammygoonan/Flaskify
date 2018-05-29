<template lang="html">
  <div class="search">
    <div class="field">
      <div class="control">
        <input
          v-model="searchQuery"
          class="input"
          @keyup="sendSearch"
          placeholder="Song, Album or Artist" />
      </div>
    </div>
    <div class="results">
      <song :data="result" v-for="result in results" :key="result.id"></song>
    </div>
  </div>

</template>

<script>
import axios from 'axios';
import Song from '@/components/Song';

export default {
  name: 'search',
  data() {
    return {
      searchQuery: '',
      results: [],
    };
  },
  components: { Song },
  methods: {
    sendSearch() {
      if (this.searchQuery.length < 3) {
        this.results = [];
      } else {
        axios.get(`${process.env.API_URL}songs/search/?q=${this.searchQuery}`)
          .then((response) => {
            this.results = response.data.collection;
          });
      }
    },
  },
};
</script>
