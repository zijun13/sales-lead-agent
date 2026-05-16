# Sales Agent Skills Documentation

## Overview
This document outlines the skills and capabilities of the sales agent assistant for the sales lead platform.

## Core Capabilities

### 1. Lead Management
- Identify and categorize new leads
- Track lead engagement status
- Provide follow-up recommendations

### 2. Customer Interaction
- Generate personalized outreach messages
- Create follow-up templates based on customer history
- Suggest optimal communication timing

### 3. Sales Conversation Guidance
- Recommend talking points based on customer profile
- Provide objection handling suggestions
- Guide toward next steps in sales process

### 4. Opportunity Assessment
- Evaluate deal probability based on customer signals
- Identify cross-sell and up-sell opportunities
- Flag high-value prospects

## Available Functions

### generate_sales_talk(lead_type, customer_profile)
Generates appropriate sales talking points based on the type of lead and customer profile.

Parameters:
- lead_type: Type of lead ('new_lead', 'follow_up', 'opportunity', 'renewal')
- customer_profile: Object containing customer information

Returns:
- String with recommended sales approach

### analyze_customer_needs(customer_data)
Analyzes customer data to identify potential needs and pain points.

Parameters:
- customer_data: Object containing customer information and history

Returns:
- Array of identified needs/pain points

### suggest_next_action(customer_profile, interaction_history)
Suggests the most appropriate next action based on customer profile and past interactions.

Parameters:
- customer_profile: Object containing customer information
- interaction_history: Array of past interactions

Returns:
- Object with suggested action and reason