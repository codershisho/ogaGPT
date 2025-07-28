<template>
    <div class="min-h-screen bg-gray-50 p-4 flex flex-col">
      <div class="flex-1 overflow-y-auto space-y-2">
        <ChatMessage
          v-for="(msg, idx) in messages"
          :key="idx"
          :message="msg.text"
          :is-user="msg.isUser"
        />
  
        <div v-if="result">
          <h2 class="text-sm text-gray-500 mt-4 mb-2">おすすめ手順書</h2>
          <ManualCard
            v-for="(manual, i) in result.manuals"
            :key="i"
            :title="manual.title"
            :url="manual.url"
          />
        </div>
      </div>
  
      <form
        class="mt-4 flex items-center gap-2"
        @submit.prevent="send"
      >
        <input
          v-model="input"
          class="flex-1 border rounded-xl p-2"
          placeholder="メッセージを入力"
        >
        <button
          type="submit"
          class="bg-blue-600 text-white rounded-xl px-4 py-2 hover:bg-blue-700"
        >
          送信
        </button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import ChatMessage from '~/components/ChatMessage.vue'
  import ManualCard from '~/components/ManualCard.vue'
  
  const input = ref('')
  const messages = ref([])
  const result = ref(null)
  
  const send = async () => {
    if (!input.value) return
  
    // ユーザーのメッセージを追加
    messages.value.push({ text: input.value, isUser: true })
  
    // API送信
    const res = await $fetch('/api/chat', {
      method: 'POST',
      body: { text: input.value },
    })
  
    // Botの返信を追加
    messages.value.push({ text: res.reply, isUser: false })
  
    // 手順書が含まれていれば結果を表示
    if (res.manuals) {
      result.value = { manuals: res.manuals }
    } else {
      result.value = null
    }
  
    input.value = ''
  }
  </script>
  