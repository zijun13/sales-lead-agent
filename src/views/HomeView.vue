<template>
  <div class="home-container">
    <header class="header">
      <h1>Sales Lead Agent</h1>
      <p>AI-Powered Sales Intelligence Platform</p>
    </header>

    <section class="data-cards">
      <div class="card" @click="goTo('/leads')">
        <div class="card-content">
          <h3>标讯列表</h3>
          <p class="count">{{ leadsCount }}</p>
          <p class="desc">Latest bidding opportunities</p>
        </div>
      </div>

      <div class="card" @click="goTo('/customers')">
        <div class="card-content">
          <h3>客户列表</h3>
          <p class="count">{{ customersCount }}</p>
          <p class="desc">Potential customers</p>
        </div>
      </div>

      <div class="card">
        <div class="card-content">
          <h3>跟进转化</h3>
          <p class="count">{{ conversionRate }}%</p>
          <p class="desc">Conversion rate</p>
        </div>
      </div>

      <div class="card">
        <div class="card-content">
          <h3>销售额</h3>
          <p class="count">¥{{ revenue }}</p>
          <p class="desc">Total sales</p>
        </div>
      </div>
    </section>

    <section class="quick-actions">
      <button class="action-btn" @click="generateSalesTalk('new_lead')">新线索跟进</button>
      <button class="action-btn" @click="generateSalesTalk('follow_up')">客户回访</button>
      <button class="action-btn" @click="generateSalesTalk('opportunity')">商机挖掘</button>
      <button class="action-btn" @click="generateSalesTalk('renewal')">合同续签</button>
    </section>

    <section class="chat-section">
      <div class="chat-window">
        <div class="chat-header">
          <h3>Sales Assistant</h3>
        </div>
        <div class="chat-messages" ref="messagesContainerRef">
          <div v-for="(msg, index) in messages" :key="index" class="message" :class="msg.type">
            <div class="message-content">{{ msg.content }}</div>
          </div>
        </div>
        <div class="chat-input-area">
          <input type="text" placeholder="Ask anything..." disabled />
          <button class="send-btn" disabled>Send</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

interface Message {
  type: string
  content: string
}

const router = useRouter()
const leadsCount = ref(0)
const customersCount = ref(0)
const conversionRate = ref(0)
const revenue = ref('0')

const messages = ref<Message[]>([
  { type: 'assistant', content: '您好！我是销售智能助手，可以帮助您跟进销售线索和客户。' }
])

const messagesContainerRef = ref<HTMLDivElement>()

const goTo = (path: string) => {
  router.push(path)
}

// 模拟获取仪表板数据
const fetchDashboardData = async () => {
  // 模拟API调用延迟
  await new Promise(resolve => setTimeout(resolve, 500));
  
  // 使用模拟数据
  leadsCount.value = 24
  customersCount.value = 42
  conversionRate.value = 68
  revenue.value = '1,240,000'
}

const generateSalesTalk = async (type: string) => {
  try {
    // 添加用户消息
    messages.value.push({ type: 'user', content: `生成${type}话术` })
    
    // 模拟API调用延迟
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // 根据类型生成不同的话术
    let talk = '';
    switch(type) {
      case 'new_lead':
        talk = '您好！我是来自[公司名称]的[姓名]。了解到贵公司在[相关领域]有需求，我们之前为类似客户提供了[解决方案]，效果显著。是否方便安排时间详细沟通一下贵公司的具体需求？';
        break;
      case 'follow_up':
        talk = '您好！上次沟通后，我想跟进一下您对我们方案的看法。针对您提到的[具体需求点]，我们做了进一步优化，希望能更好地满足您的业务场景。';
        break;
      case 'opportunity':
        talk = '基于我们前期的交流，我发现贵公司有[具体业务痛点]的需求，我们的产品正好解决了这一问题。我们有几个成功的案例可以参考，效果都很不错。';
        break;
      case 'renewal':
        talk = '您好！您的服务即将到期，我们希望能继续为您提供支持。在过去的合作中，我们的服务为您节省了[具体收益]，续约还能享受[优惠政策]。';
        break;
      default:
        talk = '这是根据客户需求定制的销售话术，旨在有效促进沟通并达成合作意向。';
    }
    
    // 显示从AI获得的回复
    messages.value.push({ type: 'assistant', content: talk })
  } catch (error) {
    console.error('Error generating sales talk:', error)
    messages.value.push({ 
      type: 'assistant', 
      content: '抱歉，生成销售话术时出现错误，请稍后重试。' 
    })
  }

  // Auto scroll to bottom
  setTimeout(() => {
    if (messagesContainerRef.value) {
      messagesContainerRef.value.scrollTop = messagesContainerRef.value.scrollHeight
    }
  }, 100)
}

onMounted(() => {
  fetchDashboardData()
  
  // Auto scroll to bottom
  setTimeout(() => {
    if (messagesContainerRef.value) {
      messagesContainerRef.value.scrollTop = messagesContainerRef.value.scrollHeight
    }
  }, 100)
})
</script>

<style scoped>
.home-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}

.header {
  text-align: center;
  margin-bottom: 30px;
}

.header h1 {
  color: #2c3e50;
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.header p {
  color: #7f8c8d;
  font-size: 1.2rem;
}

.data-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.card {
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.card-content {
  padding: 25px;
  text-align: center;
}

.card-content h3 {
  margin: 0 0 15px;
  color: #3498db;
  font-size: 1.3rem;
}

.count {
  font-size: 2.5rem;
  font-weight: bold;
  color: #2c3e50;
  margin: 10px 0;
}

.desc {
  color: #7f8c8d;
  margin: 0;
}

.quick-actions {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 30px;
}

.action-btn {
  padding: 12px 24px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s;
}

.action-btn:hover {
  background-color: #2980b9;
}

.chat-section {
  display: flex;
  justify-content: center;
}

.chat-window {
  width: 100%;
  max-width: 800px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  height: 400px;
}

.chat-header {
  background: #3498db;
  color: white;
  padding: 15px 20px;
  text-align: left;
}

.chat-header h3 {
  margin: 0;
}

.chat-messages {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.message {
  max-width: 80%;
  padding: 12px 16px;
  border-radius: 18px;
  line-height: 1.5;
}

.message.user {
  align-self: flex-end;
  background-color: #3498db;
  color: white;
  border-bottom-right-radius: 5px;
}

.message.assistant {
  align-self: flex-start;
  background-color: #f1f0f0;
  color: #333;
  border-top-left-radius: 5px;
}

.chat-input-area {
  display: flex;
  padding: 15px;
  background: #f9f9f9;
  border-top: 1px solid #eee;
}

.chat-input-area input {
  flex: 1;
  padding: 12px 15px;
  border: 1px solid #ddd;
  border-radius: 25px;
  outline: none;
}

.send-btn {
  margin-left: 10px;
  padding: 12px 20px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 25px;
  cursor: pointer;
}
</style>