<template lang="html">
  <div class="search">
    <div class="field">
      <div class="control">
        <input
          v-model="searchQuery"
          class="input"
          @keyup="sendSearch"
          placeholder="Song, Album or Artist" />
        <div class="results">
          <ul>
            <li v-for="result in results" :key="result.id">
              <a @click="addSong(result)" class="is-small">{{ result.title }}</a> -
              <span class="artist" v-if="result.artists && result.artists.length > 0">
                {{ result.artists[0].name }}
              </span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'search',
  data() {
    return {
      searchQuery: '',
      results: [],
    };
  },
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
    addSong(song) {
      this.$store.commit('addToPlaylist', song);
    },
  },
};
</script>
