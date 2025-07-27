<template>
    <div class="min-h-screen flex flex-col bg-gray-50 text-gray-800">
      <header class="bg-white shadow p-4">
        <h1 class="text-xl font-bold">手順書検索アプリ</h1>
      </header>
  
      <main class="flex-1 p-4">
        <slot />
      </main>
  
      <footer class="bg-gray-100 text-sm text-center py-3 text-gray-500">
        &copy; 2025 OgaGPT
      </footer>
    </div>
  </template>