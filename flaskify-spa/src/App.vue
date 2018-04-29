<template>
  <div id="app">
    <router-view/>
    <player song_id="20"></player>
  </div>
</template>

<script>

import Player from '@/components/Player';

export default {
  name: 'App',
  components: { Player },
};
</script>

<style src="./sass/app.sass" lang="sass"></style>
