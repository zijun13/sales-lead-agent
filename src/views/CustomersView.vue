<template>
  <div class="customers-container">
    <header class="page-header">
      <h1>客户列表</h1>
      <p>管理您的潜在客户和现有客户</p>
    </header>

    <div class="filters">
      <input type="text" v-model="searchTerm" placeholder="搜索客户..." class="search-input" />
      <select v-model="filterStage" class="stage-select">
        <option value="">全部阶段</option>
        <option value="prospect">潜在客户</option>
        <option value="lead">销售线索</option>
        <option value="opportunity">商机</option>
        <option value="customer">现有客户</option>
      </select>
      <select v-model="filterPriority" class="priority-select">
        <option value="">全部优先级</option>
        <option value="high">高</option>
        <option value="medium">中</option>
        <option value="low">低</option>
      </select>
    </div>

    <div class="customers-list">
      <div 
        v-for="customer in filteredCustomers" 
        :key="customer.id" 
        class="customer-card"
        @click="selectCustomer(customer)"
      >
        <div class="customer-info">
          <h3>{{ customer.name }}</h3>
          <p class="company">{{ customer.company }} - {{ customer.position }}</p>
          <p class="contact">联系方式: {{ customer.contact }}</p>
          <div class="meta">
            <span class="stage" :class="customer.stage">{{ customer.stageText }}</span>
            <span class="priority" :class="customer.priority">优先级: {{ customer.priorityText }}</span>
            <span class="last-contact">最后联系: {{ formatDate(customer.lastContact) }}</span>
          </div>
        </div>
        <div class="customer-actions">
          <button class="action-btn" @click.stop="generateFollowUp(customer)">生成话术</button>
        </div>
      </div>
    </div>

    <!-- Back to home button -->
    <div class="back-btn-container">
      <button class="back-btn" @click="goHome">返回首页</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

interface Customer {
  id: number
  name: string
  company: string
  position: string
  contact: string
  stage: string
  stageText: string
  priority: string
  priorityText: string
  lastContact: Date
}

const router = useRouter()

// Mock data for customers
const customersData = ref<Customer[]>([
  {
    id: 1,
    name: "张伟",
    company: "某科技有限公司",
    position: "CTO",
    contact: "zhangwei@example.com",
    stage: "opportunity",
    stageText: "商机",
    priority: "high",
    priorityText: "高",
    lastContact: new Date(2023, 8, 20)
  },
  {
    id: 2,
    name: "李娜",
    company: "创新制造集团",
    position: "采购经理",
    contact: "lina@innovate.com",
    stage: "lead",
    stageText: "销售线索",
    priority: "medium",
    priorityText: "中",
    lastContact: new Date(2023, 8, 15)
  },
  {
    id: 3,
    name: "王强",
    company: "未来教育集团",
    position: "技术总监",
    contact: "wangqiang@futureedu.com",
    stage: "customer",
    stageText: "现有客户",
    priority: "high",
    priorityText: "高",
    lastContact: new Date(2023, 8, 25)
  },
  {
    id: 4,
    name: "陈丽",
    company: "智慧城市解决方案",
    position: "项目经理",
    contact: "chenli@smartcity.com",
    stage: "prospect",
    stageText: "潜在客户",
    priority: "low",
    priorityText: "低",
    lastContact: new Date(2023, 7, 30)
  },
  {
    id: 5,
    name: "刘洋",
    company: "数字化转型咨询",
    position: "合伙人",
    contact: "liuyang@digital.com",
    stage: "opportunity",
    stageText: "商机",
    priority: "high",
    priorityText: "高",
    lastContact: new Date(2023, 8, 18)
  }
])

const searchTerm = ref('')
const filterStage = ref('')
const filterPriority = ref('')

const filteredCustomers = computed(() => {
  return customersData.value.filter(customer => {
    const matchesSearch = customer.name.toLowerCase().includes(searchTerm.value.toLowerCase()) || 
                          customer.company.toLowerCase().includes(searchTerm.value.toLowerCase())
    const matchesStage = !filterStage.value || customer.stage === filterStage.value
    const matchesPriority = !filterPriority.value || customer.priority === filterPriority.value
    return matchesSearch && matchesStage && matchesPriority
  })
})

const formatDate = (date: Date) => {
  return `${date.getFullYear()}-${(date.getMonth()+1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`
}

const selectCustomer = (customer: Customer) => {
  console.log(`Selected customer: ${customer.name}`)
  // In a real app, this might navigate to a detail view
}

const generateFollowUp = (customer: Customer) => {
  alert(`为 "${customer.name}" 生成销售跟进话术:\n\n您好 ${customer.name}，我是来自[公司名称]的[姓名]。了解到贵公司在[相关领域]有需求，我们之前为类似客户提供了[解决方案]，效果显著。是否方便安排时间详细沟通一下贵公司的具体需求？`)
}

const goHome = () => {
  router.push('/')
}
</script>

<style scoped>
.customers-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}

.page-header {
  text-align: center;
  margin-bottom: 30px;
}

.page-header h1 {
  color: #2c3e50;
  font-size: 2rem;
  margin-bottom: 10px;
}

.filters {
  display: flex;
  gap: 15px;
  margin-bottom: 25px;
  justify-content: center;
  flex-wrap: wrap;
}

.search-input {
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
  width: 250px;
  font-size: 1rem;
}

.stage-select, .priority-select {
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

.customers-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.customer-card {
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.customer-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.customer-info h3 {
  margin: 0 0 8px;
  color: #2c3e50;
  font-size: 1.3rem;
}

.customer-info .company {
  color: #3498db;
  font-weight: bold;
  margin: 0 0 8px;
}

.customer-info .contact {
  color: #7f8c8d;
  margin: 0 0 15px;
  font-size: 0.95rem;
}

.meta {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}

.meta span {
  font-size: 0.9rem;
  padding: 3px 8px;
  border-radius: 3px;
}

.meta .stage {
  background-color: #eaf5fb;
  color: #3498db;
}

.meta .stage.prospect {
  background-color: #fff3e0;
  color: #ff9800;
}

.meta .stage.lead {
  background-color: #e8f5e9;
  color: #4caf50;
}

.meta .stage.opportunity {
  background-color: #e3f2fd;
  color: #2196f3;
}

.meta .stage.customer {
  background-color: #f3e5f5;
  color: #9c27b0;
}

.meta .priority {
  background-color: #ffebee;
  color: #f44336;
}

.meta .priority.high {
  background-color: #ffcdd2;
  color: #c62828;
}

.meta .priority.medium {
  background-color: #fff8e1;
  color: #f57f17;
}

.meta .priority.low {
  background-color: #e8f5e9;
  color: #2e7d32;
}

.meta .last-contact {
  background-color: #eceff1;
  color: #546e7a;
}

.customer-actions {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.action-btn {
  padding: 8px 16px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background-color 0.3s;
}

.action-btn:hover {
  background-color: #2980b9;
}

.back-btn-container {
  display: flex;
  justify-content: center;
  margin-top: 30px;
}

.back-btn {
  padding: 12px 24px;
  background-color: #95a5a6;
  color: white;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s;
}

.back-btn:hover {
  background-color: #7f8c8d;
}
</style>
```

```
<template>
  <div class="customers">
    <h1>Customer Management</h1>
    
    <div v-if="loading" class="loading">Loading customers...</div>
    
    <div v-else>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Company</th>
            <th>Purchase History</th>
            <th>Last Contact</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="customer in customers" :key="customer.id">
            <td>{{ customer.id }}</td>
            <td>{{ customer.name }}</td>
            <td>{{ customer.email }}</td>
            <td>{{ customer.company }}</td>
            <td>{{ customer.purchaseHistory.join(', ') }}</td>
            <td>{{ customer.lastContact }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

interface Customer {
  id: number;
  name: string;
  email: string;
  company: string;
  purchaseHistory: string[];
  lastContact: string;
}

const customers = ref<Customer[]>([]);

const loading = ref(true);

onMounted(async () => {
  // 模拟加载数据
  await new Promise(resolve => setTimeout(resolve, 1000));
  
  customers.value = [
    {
      id: 1,
      name: 'John Smith',
      email: 'john@example.com',
      company: 'ABC Corp',
      purchaseHistory: ['Product A', 'Service B'],
      lastContact: '2023-05-15'
    },
    {
      id: 2,
      name: 'Sarah Johnson',
      email: 'sarah@example.com',
      company: 'XYZ Ltd',
      purchaseHistory: ['Product C'],
      lastContact: '2023-06-20'
    },
    {
      id: 3,
      name: 'Michael Brown',
      email: 'michael@example.com',
      company: 'Tech Inc',
      purchaseHistory: ['Service A', 'Product B', 'Product D'],
      lastContact: '2023-07-10'
    }
  ];
  
  loading.value = false;
});
</script>

<style scoped>
.customers {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.loading {
  text-align: center;
  font-size: 18px;
  margin-top: 50px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f2f2f2;
}
</style>