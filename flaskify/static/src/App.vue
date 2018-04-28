<template>
  <div id="app">
    <top-nav></top-nav>
    <songs></songs>
  </div>
</template>

<script>
import Nav from './components/Nav.vue';
import Songs from './components/Songs.vue';

export default {
  name: 'app',
  components: { 'top-nav': Nav, Songs },
}
</script>
