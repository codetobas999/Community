<script lang="ts" setup></script>
<template>
  <nav class="bg-gray-900 text-white py-5 border-b border-gray-700">
    <div class="container mx-auto px-4 sm:px-0 py-2 flex flex-col sm:flex-row justify-center gap-3 sm:gap-0 sm:justify-between items-center">
      <NuxtLink to="/"
        class="text-2xl font-medium">Nuxt 3 Blog</NuxtLink>
      <ul class="flex gap-5 items-center justify-end">
        <li>
          <NuxtLink to="/" class="text-2xl text-gray-300 hover:text-gray-50">Home</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/categories" class="text-2xl text-gray-300 hover:text-gray-50">Categories</NuxtLink>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>

a.router-link-active {
  color: teal
}
</style>