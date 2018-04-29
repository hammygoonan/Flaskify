<template>
  <div class="album-square" :style="colour">
    <strong>{{ data.title }}</strong><br />
    <span v-for="artist in data.artists" :key="artist.id">{{ artist.name }}</span>
  </div>
</template>

<script>

export default {
  name: 'album',
  props: ['data'],
  computed: {
    colour() {
      return `background-color: #${Math.floor(Math.random() * 16777215).toString(16)}`;
    },
  },
};
</script>
