<template>
  <div class="album-square box" :style="background">
    <div class="album-square__info">
      <h5 @click="display = true">{{ data.title }}</h5>
      {{ artists }}
    </div>
    <div class="modal" :class="{'is-active': display}">
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="box">
          <h5 @click="display = true">
            {{ data.title }}
            <button
              class="is-outlined is-small is-info button is-pulled-right"
              @click="addAlbum"
            >Play all</button>
          </h5>
          <hr />
          <song v-for="song in data.songs" :data="song" :key="song.id"></song>
        </div>
      </div>
      <button class="modal-close is-large" aria-label="close" @click="display = false"></button>
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
    artists() {
      if (this.data.artists.length > 2) {
        return 'Various';
      }
      return this.data.artists.reduce((artistList, artist) => artistList + artist.name, '');
    },
  },
  methods: {
    addAlbum() {
      this.data.songs.forEach((song) => {
        this.$store.commit('addToPlaylist', song);
      });
    },
  },
};
</script>
