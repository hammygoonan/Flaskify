<template lang="html">
  <div class="player">
    <audio
      :src="src"
      autoplay
      @ended="ended"
      @timeupdate="timeupdate"
    >{{ song.title }}</audio>
    <div class="columns">
      <div class="column is-2 audio-controls">
        <button
          class="audio-control play"
          @click="togglePlay"
          :class="{ 'is-hidden' : !player.paused }"
        >
          <span class="icon">
            <i class="fas fa-play"></i>
          </span>
        </button>
        <button
          class="audio-control play"
          @click="togglePlay"
          :class="{ 'is-hidden' : player.paused }"
        >
          <span class="icon">
            <i class="fas fa-pause"></i>
          </span>
        </button>
        <button class="audio-control next" @click="next">
          <span class="icon">
            <i class="fas fa-step-forward"></i>
          </span>
        </button>
      </div>
      <div class="column is-8 player-detail">
        <h4 class="title is-4 has-text-white">{{ song.title }}</h4>
        <h5 class="subtitle is-6 has-text-white" v-if="currentSong.artists">
          by {{ currentSong.artists[0].name }}
        </h5>
        <progress
          class="progress"
          :value="currentTime"
          max="1"
          @click="seek"
        >{{ currentTime }}%</progress>
        <p>
          <span class="is-pulled-left">{{ formatTime(player.currentTime) }}</span>
          <span class="is-pulled-right">{{ formatTime(player.duration) }}</span>
        </p>
      </div>
      <div class="column is-2">
        <img :src="albumArt" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'player',
  data() {
    return {
      currentTime: 0,
      currentSong: {},
      albumArt: '',
      player: {},
    };
  },
  computed: {
    song() {
      return this.$store.state.playing;
    },
    src() {
      if (Object.keys(this.$store.state.playing).length === 0) {
        return '';
      }
      return `${process.env.API_URL.slice(0, -1)}${this.$store.state.playing.src}`;
    },
  },
  mounted() {
    this.player = this.$el.querySelector('audio');
  },
  methods: {
    ended() {
      this.currentTime = 0;
      this.$store.commit('nextSong');
    },
    timeupdate(a) {
      const currentTime = a.target.currentTime / a.target.duration;
      if (currentTime >= 0) {
        this.currentTime = a.target.currentTime / a.target.duration;
      } else {
        this.currentTime = 0;
      }
    },
    seek(e) {
      const position = e.pageX - e.target.offsetLeft;
      const currentTime = position / e.target.offsetWidth;
      this.currentTime = currentTime;
      this.player.currentTime = this.player.duration * currentTime;
    },
    togglePlay() {
      if (this.player.paused) {
        this.player.play();
      } else {
        this.player.pause();
      }
    },
    next() {
      this.currentTime = 0;
      this.$store.commit('nextSong');
    },
    formatTime(seconds) {
      if (seconds) {
        const sec = Math.floor(seconds % 60);
        const mins = Math.floor(seconds / 60);
        return `${mins}:${(sec < 10 ? '0' : '')}${sec}`;
      }
      return '';
    },
  },
  watch: {
    song() {
      axios.get(`${process.env.API_URL}songs/${this.$store.state.playing.id}/`)
        .then((response) => {
          this.currentSong = response.data;
          if (response.data.albums.length > 0) {
            this.albumArt = `${process.env.API_URL}albums/${response.data.albums[0].id}/artwork/`;
          } else {
            this.albumArt = '';
          }
        });
    },
  },
};
</script>
