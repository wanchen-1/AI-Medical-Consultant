<script setup>
import { ref } from 'vue'
const input = ref('')
const loading = ref(false)
const messages = ref([{ role: 'assistant', text: '你好，我是 AI 医疗问诊助手。请描述你的症状，我会帮助你整理信息。' }])
async function send() {
  if (!input.value.trim() || loading.value) return
  const text = input.value.trim(); messages.value.push({ role: 'user', text }); input.value = ''; loading.value = true
  try { const r = await fetch('http://localhost:8000/api/chat', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({ message: text }) }); const data = await r.json(); messages.value.push({ role: 'assistant', text: data.reply }) }
  catch { messages.value.push({ role: 'assistant', text: '服务暂时不可用，请检查后端是否已启动。' }) } finally { loading.value = false }
}
</script>
<template><main><header><h1>AI Medical Consultant</h1><span>健康信息辅助</span></header><section class="notice">本工具不能替代医生诊断。紧急症状请立即就医。</section><section class="chat"><article v-for="(m,i) in messages" :key="i" :class="m.role"><b>{{ m.role === 'assistant' ? 'AI 助手' : '你' }}</b><p>{{ m.text }}</p></article></section><form @submit.prevent="send"><input v-model="input" placeholder="描述你的症状..."/><button>发送</button></form></main></template>
