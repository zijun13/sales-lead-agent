<template>
  <div class="leads-container">
    <header class="page-header">
      <h1>标讯列表</h1>
      <p>最新招标信息及销售机会</p>
    </header>

    <div class="filters">
      <input type="text" v-model="searchTerm" placeholder="搜索标讯..." class="search-input" />
      <select v-model="filterStatus" class="status-select">
        <option value="">全部状态</option>
        <option value="new">新线索</option>
        <option value="contacted">已联系</option>
        <option value="qualified">已确认</option>
        <option value="closed">已关闭</option>
      </select>
    </div>

    <div class="leads-list">
      <div 
        v-for="lead in filteredLeads" 
        :key="lead.id" 
        class="lead-card"
        @click="selectLead(lead)"
      >
        <div class="lead-info">
          <h3>{{ lead.title }}</h3>
          <p class="company">{{ lead.company }}</p>
          <p class="details">{{ lead.description }}</p>
          <div class="meta">
            <span class="date">{{ formatDate(lead.date) }}</span>
            <span class="status" :class="lead.status">{{ lead.statusText }}</span>
            <span class="budget">预算: ¥{{ lead.budget }}</span>
          </div>
        </div>
        <div class="lead-actions">
          <button class="action-btn" @click.stop="generateFollowUp(lead)">生成话术</button>
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

interface Lead {
  id: number
  title: string
  company: string
  description: string
  date: Date
  status: string
  statusText: string
  budget: string
}

const router = useRouter()

// Mock data for leads
const leadsData = ref<Lead[]>([
  {
    id: 1,
    title: "政府机构IT系统升级项目",
    company: "某市政府信息中心",
    description: "需要对现有IT基础设施进行全面升级，包括服务器、网络设备和管理软件。",
    date: new Date(2023, 8, 15),
    status: "new",
    statusText: "新线索",
    budget: "500万"
  },
  {
    id: 2,
    title: "制造业ERP系统实施",
    company: "某制造企业",
    description: "实施企业资源规划系统，整合财务、采购、库存和生产管理流程。",
    date: new Date(2023, 8, 18),
    status: "contacted",
    statusText: "已联系",
    budget: "300万"
  },
  {
    id: 3,
    title: "教育行业在线学习平台",
    company: "某教育集团",
    description: "开发定制化的在线学习平台，支持直播课程和作业管理系统。",
    date: new Date(2023, 8, 20),
    status: "qualified",
    statusText: "已确认",
    budget: "200万"
  },
  {
    id: 4,
    title: "零售业数据分析系统",
    company: "某连锁零售企业",
    description: "开发定制化的数据分析系统，用于分析顾客购买行为和库存优化。",
    date: new Date(2023, 8, 22),
    status: "closed",
    statusText: "已关闭",
    budget: "150万"
  }
])

const searchTerm = ref('')
const filterStatus = ref('')

const filteredLeads = computed(() => {
  return leadsData.value.filter(lead => {
    const matchesSearch = lead.title.toLowerCase().includes(searchTerm.value.toLowerCase()) || 
                         lead.company.toLowerCase().includes(searchTerm.value.toLowerCase())
    const matchesStatus = !filterStatus.value || lead.status === filterStatus.value
    return matchesSearch && matchesStatus
  })
})

const formatDate = (date: Date) => {
  return `${date.getFullYear()}-${(date.getMonth()+1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`
}

const selectLead = (lead: Lead) => {
  console.log(`Selected lead: ${lead.title}`)
  // In a real app, this might navigate to a detail view
}

const generateFollowUp = (lead: Lead) => {
  alert(`为 "${lead.title}" 生成销售跟进话术:\n\n您好，我了解到贵公司发布了 "${lead.title}" 项目，我们在此领域有丰富的经验，已完成多个类似项目。是否方便安排时间详细介绍我们的解决方案？`)
}

const goHome = () => {
  router.push('/')
}
</script>

<style scoped>
.leads-container {
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

.status-select {
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

.leads-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.lead-card {
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

.lead-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.lead-info h3 {
  margin: 0 0 8px;
  color: #2c3e50;
  font-size: 1.3rem;
}

.lead-info .company {
  color: #3498db;
  font-weight: bold;
  margin: 0 0 8px;
}

.lead-info .details {
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

.meta .date {
  background-color: #e1f5fe;
  color: #0277bd;
}

.meta .status {
  background-color: #e8f5e9;
  color: #2e7d32;
}

.meta .status.new {
  background-color: #e8f5e9;
  color: #2e7d32;
}

.meta .status.contacted {
  background-color: #e3f2fd;
  color: #1565c0;
}

.meta .status.qualified {
  background-color: #fff8e1;
  color: #f57f17;
}

.meta .status.closed {
  background-color: #ffebee;
  color: #c62828;
}

.meta .budget {
  background-color: #f3e5f5;
  color: #7b1fa2;
}

.lead-actions {
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