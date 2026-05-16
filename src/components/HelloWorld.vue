<template>
  <h1>{{ msg }}</h1>

  <p>
    <a href="https://v3.vuejs.org/guide/composition-api-introduction.html" target="_blank">Vue 3 Composition API Documentation</a> |
    <a href="https://next.router.vuejs.org/" target="_blank">Vue Router Documentation</a> |
    <a href="https://github.com/vuejs/create-vue" target="_blank">create-vue</a>
  </p>

  <p>
    Install the
    <a href="https://github.com/vuejs/language-tools" target="_blank">Vue Language Tools</a>
    extension for enhanced syntax highlighting and rich IntelliSense features.
  </p>
</template>

<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<style scoped>
a {
  color: #42b883;
}
</style>