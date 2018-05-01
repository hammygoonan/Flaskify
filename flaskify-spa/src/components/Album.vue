<template>
  <div class="album-square" :style="colour">
    <strong @click="display = !display">{{ data.title }}</strong><br />
    <span v-for="artist in data.artists" :key="artist.id">{{ artist.name }}</span>
    <div class="album-square__song-list" v-if="display">
      <div>Play all</div>
      <hr />
      <song v-for="song in data.songs" :data="song" :key="song.id"></song>
    </div>
  </div>
</template>

<script>

import Song from '@/components/Song';

export default {
  name: 'album',
  props: ['data'],
  data() {
    return {
      display: false,
    };
  },
  components: { Song },
  computed: {
    colour() {
      return `background-color: #${Math.floor(Math.random() * 16777215).toString(16)}`;
    },
  },
};
</script>
