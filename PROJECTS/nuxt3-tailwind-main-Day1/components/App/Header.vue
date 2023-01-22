<script lang="ts" setup>
  const isOpen = ref(false)
</script>

<template>
  <header class="
      navbar-default
      bg-skin-fill
      bg-green-700
      text-skin-base
      py-3
      border-b
      sticky
      top-0">
    <div class="
      container
      mx-auto
      pl-4
      pr-2
      sm:px-0
      flex flex-row
      items-center
      gap-4
      justify-between">
      <NuxtLink to="/" class="font-bold text-lg text-white">Nuxt 3 Tailwind</NuxtLink>
      <button 
        class="appearance-none px-2 py-2 rounded sm:hidden"
        type="button"
        aria-label="menu"
        @click="isOpen = !isOpen"
      >
        <Icon name="ri:menu-line" class="w-6 h-6" />
      </button>

      <!-- Menu -->
      <div :class="isOpen ? 'fixed sm:relative top-16 shadow sm:shadow-none left-4 right-4 rounded-lg overflow-hidden bg-white sm:bg-transparent py-2':'hidden sm:flex sm:w-6/12'">
        <nav class="
          flex flex-col
          sm:relative
          w-full
          items-start
          sm:flex-row
          sm:justify-end
          sm:gap-1
          sm:items-center
        ">
          <NuxtLink to="/" class="
            px-4
            py-2
            rounded-full
            w-full
            sm:w-auto
            text-skin-base
            hover:text-skin-hover
            hover:bg-skin-fill-hover
            transition
            duration-200
            font-medium"
            exact-active-class="bg-skin-fill-active text-skin-active"
            >Home</NuxtLink>
          <NuxtLink to="/store" class="
            px-4
            py-2
            rounded-full
            w-full
            sm:w-auto
            text-skin-base
            hover:text-skin-hover
            hover:bg-skin-fill-hover
            transition
            duration-200
            font-medium"
            exact-active-class="bg-skin-fill-active text-skin-active"
            >Store</NuxtLink>
          <NuxtLink to="/blog" class="
            px-4
            py-2
            rounded-full
            w-full
            sm:w-auto
            text-skin-base
            hover:text-skin-hover
            hover:bg-skin-fill-hover
            transition
            duration-200
            font-medium"
            exact-active-class="bg-skin-fill-active text-skin-active"
            >Blog</NuxtLink>
          <NuxtLink to="/contact" class="
            px-4
            py-2
            rounded-full
            w-full
            sm:w-auto
            text-skin-base
            hover:text-skin-hover
            hover:bg-skin-fill-hover
            transition
            duration-200
            font-medium"
            exact-active-class="bg-skin-fill-active text-skin-active"
            >Contact</NuxtLink>
        </nav>
      </div>
    </div>
  </header>
</template>

<style scoped>
  .navbar-default {
    --color-text-base: #ffffff;
    --color-text-active: #ffffff;
    --color-text-hover: #ffffff;
    --color-text-muted: #1d4ed8;
    --color-fill-hover: #1d4ed8;
    --color-fill-active: #1d4ed8;
  }
</style>
