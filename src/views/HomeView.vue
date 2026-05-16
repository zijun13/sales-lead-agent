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
      <button class="action-btn" @click="generateSalesTalk('opportunity')">商机挖掘')</button>
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
import axios from 'axios'

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

const fetchDashboardData = async () => {
  try {
    const response = await axios.get('/api/dashboard/stats')
    leadsCount.value = response.data.leadsCount
    customersCount.value = response.data.customersCount
    conversionRate.value = response.data.conversionRate
    revenue.value = response.data.revenue
  } catch (error) {
    console.error('Failed to fetch dashboard data:', error)
    // Fallback to default values or handle error UI
  }
}

const generateSalesTalk = async (type: string) => {
  try {
    // 添加用户消息
    messages.value.push({ type: 'user', content: `生成${type}话术` })
    
    // 调用后端API
    const response = await axios.post('/api/generate-talk', {
      lead_type: type,
      customer_profile: {
        company: '示例公司',
        industry: '科技行业',
        contact_name: '客户'
      }
    })
    
    // 显示从AI获得的回复
    messages.value.push({ type: 'assistant', content: response.data.talk })
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
```

```
<template>
  <div class="home">
    <h1>Sales Lead Dashboard</h1>
    
    <div class="add-lead-form">
      <h2>Add New Lead</h2>
      <form @submit.prevent="addLead">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="newLead.name" required>
        </div>
        
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="newLead.email" required>
        </div>
        
        <div class="form-group">
          <label for="company">Company:</label>
          <input type="text" id="company" v-model="newLead.company" required>
        </div>
        
        <button type="submit" :disabled="loading">
          {{ loading ? 'Adding...' : 'Add Lead' }}
        </button>
      </form>
      
      <p v-if="message" class="message">{{ message }}</p>
    </div>
    
    <div class="leads-list">
      <h2>Recent Leads</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Company</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="lead in leads" :key="lead.id">
            <td>{{ lead.id }}</td>
            <td>{{ lead.name }}</td>
            <td>{{ lead.email }}</td>
            <td>{{ lead.company }}</td>
            <td><span class="status" :class="lead.status">{{ lead.status }}</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

interface Lead {
  id: number;
  name: string;
  email: string;
  company: string;
  status: 'new' | 'contacted' | 'qualified' | 'lost';
}

const leads = ref<Lead[]>([
  { id: 1, name: 'John Smith', email: 'john@example.com', company: 'ABC Corp', status: 'new' },
  { id: 2, name: 'Sarah Johnson', email: 'sarah@example.com', company: 'XYZ Ltd', status: 'contacted' },
  { id: 3, name: 'Michael Brown', email: 'michael@example.com', company: 'Tech Inc', status: 'qualified' },
]);

const newLead = ref({
  name: '',
  email: '',
  company: ''
});

const loading = ref(false);
const message = ref('');

const addLead = async () => {
  if (!newLead.value.name || !newLead.value.email || !newLead.value.company) {
    message.value = 'Please fill in all fields';
    return;
  }

  loading.value = true;
  
  // 模拟 API 调用延迟
  await new Promise(resolve => setTimeout(resolve, 1000));
  
  // 添加新潜在客户到列表
  const lead: Lead = {
    id: leads.value.length + 1,
    name: newLead.value.name,
    email: newLead.value.email,
    company: newLead.value.company,
    status: 'new'
  };
  
  leads.value.push(lead);
  
  // 重置表单
  newLead.value = { name: '', email: '', company: '' };
  message.value = 'Lead added successfully!';
  loading.value = false;
};
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.add-lead-form {
  background: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  background-color: #42b983;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.message {
  margin-top: 10px;
  padding: 10px;
  background-color: #dff0d8;
  color: #3c763d;
  border-radius: 4px;
}

.leads-list table {
  width: 100%;
  border-collapse: collapse;
}

.leads-list th,
.leads-list td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.leads-list th {
  background-color: #f2f2f2;
}

.status {
  padding: 4px 8px;
  border-radius: 4px;
  color: white;
  font-size: 0.8em;
}

.status.new {
  background-color: #42b983;
}

.status.contacted {
  background-color: #6baeff;
}

.status.qualified {
  background-color: #ffa500;
}

.status.lost {
  background-color: #e74c3c;
}
</style>