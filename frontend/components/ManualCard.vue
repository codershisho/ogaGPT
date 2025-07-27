<template>
    <div class="border rounded-xl p-4 shadow hover:shadow-md transition">
      <h3 class="text-lg font-bold mb-2">{{ title }}</h3>
      <a
        :href="url"
        target="_blank"
        class="text-blue-600 hover:underline"
      >
        手順書を見る
      </a>
    </div>
  </template>
  
  <script setup>
  defineProps({
    title: String,
    url: String,
  })
  </script>
  