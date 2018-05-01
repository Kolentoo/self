<template>
  <div id="app">
    <transition name="fade">
      <router-view>

      </router-view>
    </transition>
  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>

<style scoped>
  .fade-enter{opacity:0;}
  .fade-enter-active{transition:all 0.4s;}
  .fade-leave-active{transition:all 0.4s;}
  .fade-leave-to{transform:translateX(100%);}
</style>
