<template lang="html">
  <div class="column is-2">
    {{ item.title }}<br />
    <strong>{{ item.artists[0].name}}</strong>
    <img :src="albumArt" />

  </div>
</template>

<script>
export default {
  name: 'song',
  props: ['item'],
  computed: {
    albumArt() {
      return `/albums/${this.item.albums[0].id}/artwork/`;
    }
  }
}
</script>
