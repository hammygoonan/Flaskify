<template lang="html">
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <h1 class="title"><a>Flaskify</a></h1>
      <a role="button"
        class="navbar-burger"
        :class="{ 'is-active': display }"
        aria-label="menu"
        aria-expanded="false"
        @click="display = true"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
      <div class="playlist" v-if="display">
        <button class="delete" aria-label="close" @click="display = false"></button>
        <h3 class="title is-6">Playlist</h3>
        <ul>
          <li v-for="song in songs" :key="song.id">{{ song.title }}</li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'playlist',
  data() {
    return {
      display: false,
    };
  },
  computed: {
    songs() {
      return this.$store.state.playlist;
    },
  },
};
</script>
