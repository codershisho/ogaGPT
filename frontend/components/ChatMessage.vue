<template>
    <div :class="isUser ? 'text-right' : 'text-left'">
      <div
        :class="[
          'inline-block px-4 py-2 my-2 rounded-xl max-w-[80%]',
          isUser
            ? 'bg-blue-500 text-white ml-auto'
            : 'bg-gray-100 text-gray-800 mr-auto'
        ]"
      >
        {{ message }}
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    message: String,
    isUser: Boolean,
  })
  </script>
  