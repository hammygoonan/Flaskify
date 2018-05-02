<template>
  <div class="album-square box" :style="background">
    <div class="album-square__info">
      <h5 @click="display = !display">{{ data.title }}</h5>
      <span v-for="artist in data.artists" :key="artist.id">{{ artist.name }}</span>
    </div>
    <div class="album-square__song-list box" v-if="display">
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
    background() {
      return `background-image: url('${process.env.API_URL}albums/${this.data.id}/artwork/');`;
    },
  },
};
</script>
