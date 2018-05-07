<template>
  <div id="app">
    <playlist></playlist>
    <router-view/>
    <player song_id="25"></player>
  </div>
</template>

<script>

import Player from '@/components/Player';
import Playlist from '@/components/Playlist';

export default {
  name: 'App',
  components: { Player, Playlist },
};
</script>

<style src="./sass/app.sass" lang="sass"></style>
