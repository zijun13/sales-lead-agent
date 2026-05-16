"""
Sales Agent AI Module
Implements core logic for sales assistance and conversation generation
"""

import json
from datetime import datetime
from typing import Dict, List, Optional


class SalesAgent:
    """
    Main class for the sales agent functionality
    """
    
    def __init__(self):
        """Initialize the sales agent with default configurations"""
        self.conversation_history = []
        
    def generate_sales_talk(self, lead_type: str, customer_profile: Dict) -> str:
        """
        Generates appropriate sales talking points based on the type of lead and customer profile
        
        Args:
            lead_type: Type of lead ('new_lead', 'follow_up', 'opportunity', 'renewal')
            customer_profile: Dictionary containing customer information
            
        Returns:
            String with recommended sales approach
        """
        if lead_type == 'new_lead':
            return self._generate_new_lead_talk(customer_profile)
        elif lead_type == 'follow_up':
            return self._generate_follow_up_talk(customer_profile)
        elif lead_type == 'opportunity':
            return self._generate_opportunity_talk(customer_profile)
        elif lead_type == 'renewal':
            return self._generate_renewal_talk(customer_profile)
        else:
            return "感谢您的关注，我们可以进一步讨论您的需求。"
    
    def _generate_new_lead_talk(self, customer_profile: Dict) -> str:
        """Generate sales talk for new leads"""
        company = customer_profile.get('company', '贵公司')
        industry = customer_profile.get('industry', '所在行业')
        
        return f"您好，看到{company}在{industry}领域的发展，我们有相关的解决方案可能对您有帮助。能否介绍一下您目前在这方面是否有相关计划或需求？"
    
    def _generate_follow_up_talk(self, customer_profile: Dict) -> str:
        """Generate sales talk for follow-ups"""
        contact_name = customer_profile.get('contact_name', '客户')
        
        return f"您好{contact_name}，距离我们上次沟通已经有一段时间了，产品使用情况如何？是否有新的业务需求需要我们支持？"
    
    def _generate_opportunity_talk(self, customer_profile: Dict) -> str:
        """Generate sales talk for opportunities"""
        opportunity = customer_profile.get('opportunity', '商机')
        
        return f"根据行业趋势分析，{opportunity}是一个值得关注的方向。我们有一些成功案例或许能给您带来启发，是否方便详细沟通？"
    
    def _generate_renewal_talk(self, customer_profile: Dict) -> str:
        """Generate sales talk for renewals"""
        contract_date = customer_profile.get('contract_end_date', '合同日期')
        
        return f"您的合同将在{contract_date}到期，我们有新的服务升级方案，是否安排时间详细介绍下？"
    
    def analyze_customer_needs(self, customer_data: Dict) -> List[str]:
        """
        Analyze customer data to identify potential needs and pain points
        
        Args:
            customer_data: Dictionary containing customer information and history
            
        Returns:
            List of identified needs/pain points
        """
        needs = []
        
        # Analyze based on industry
        industry = customer_data.get('industry')
        if industry:
            if industry in ['制造业', '工业']:
                needs.append("生产效率优化")
                needs.append("成本控制方案")
            elif industry in ['教育', '培训']:
                needs.append("数字化教学方案")
                needs.append("远程学习支持")
            elif industry in ['医疗', '健康']:
                needs.append("患者管理系统")
                needs.append("数据安全合规")
        
        # Analyze based on size
        size = customer_data.get('size')
        if size:
            if size == 'small':
                needs.append("简化运营管理")
                needs.append("提高自动化水平")
            elif size == 'large':
                needs.append("系统集成方案")
                needs.append("数据驱动决策")
        
        # Analyze based on previous interactions
        interactions = customer_data.get('interactions', [])
        if len(interactions) > 5:
            needs.append("深度合作关系建立")
        
        return needs if needs else ["提高业务效率", "降低成本", "增强竞争力"]
    
    def suggest_next_action(self, customer_profile: Dict, interaction_history: List[Dict]) -> Dict:
        """
        Suggest the most appropriate next action based on customer profile and past interactions
        
        Args:
            customer_profile: Dictionary containing customer information
            interaction_history: List of past interactions
            
        Returns:
            Dictionary with suggested action and reason
        """
        # Determine customer stage based on interaction history
        num_interactions = len(interaction_history)
        last_interaction = interaction_history[-1] if interaction_history else {}
        
        # Default suggestion
        suggestion = {
            "action": "电话跟进",
            "reason": "保持与客户的联系是建立信任的关键步骤",
            "priority": "medium"
        }
        
        # Adjust based on number of interactions
        if num_interactions == 0:
            suggestion["action"] = "初次拜访"
            suggestion["reason"] = "首次接触客户，建立初步关系"
            suggestion["priority"] = "high"
        elif num_interactions == 1:
            suggestion["action"] = "发送资料"
            suggestion["reason"] = "向客户提供详细的产品/服务信息"
            suggestion["priority"] = "high"
        elif num_interactions < 5:
            suggestion["action"] = "需求调研"
            suggestion["reason"] = "深入了解客户的具体需求"
            suggestion["priority"] = "medium"
        else:
            suggestion["action"] = "方案演示"
            suggestion["reason"] = "向客户展示针对性的解决方案"
            suggestion["priority"] = "high"
            
        # Adjust based on last interaction outcome
        outcome = last_interaction.get('outcome', '')
        if 'positive' in outcome.lower():
            suggestion["action"] = "推进合作"
            suggestion["reason"] = "客户反馈积极，应推进下一步合作"
            suggestion["priority"] = "high"
        elif 'negative' in outcome.lower():
            suggestion["action"] = "问题解决"
            suggestion["reason"] = "需要解决客户提出的问题或疑虑"
            suggestion["priority"] = "high"
        elif 'maybe' in outcome.lower() or 'considering' in outcome.lower():
            suggestion["action"] = "定期跟进"
            suggestion["reason"] = "客户仍在考虑中，需定期保持联系"
            suggestion["priority"] = "low"
        
        return suggestion
    
    def add_conversation(self, message: str, sender: str = "user"):
        """Add a message to the conversation history"""
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "sender": sender,
            "message": message
        })


def main():
    """Example usage of the SalesAgent"""
    agent = SalesAgent()
    
    # Example customer profile
    customer = {
        "company": "某制造企业",
        "industry": "制造业",
        "contact_name": "张总",
        "size": "large"
    }
    
    # Generate sales talk for a new lead
    talk = agent.generate_sales_talk('new_lead', customer)
    print(f"New Lead Talk: {talk}")
    
    # Analyze customer needs
    needs = agent.analyze_customer_needs(customer)
    print(f"Identified Needs: {needs}")
    
    # Suggest next action
    interaction_history = [{"outcome": "positive"}]
    action_suggestion = agent.suggest_next_action(customer, interaction_history)
    print(f"Action Suggestion: {action_suggestion}")


if __name__ == "__main__":
    main()