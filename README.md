###  **Cyber Supply Chain Risk Monitoring Platform**



\# Cyber Supply Chain Risk Monitoring Platform (CSCRM)

\*\*Created by: Tamrat Workineh\*\* 

\*\* Doctoral Candidate, PhD in Cybersecurity\*\*\* 

\*\*GitHub Portfolio Project\*\*



A full end‑to‑end simulation of a Cyber Supply Chain Risk Management (CSCRM) continuous monitoring program, inspired by NIST SP 800‑161 and real federal vendor‑risk workflows.



A full end‑to‑end simulation of a Cyber Supply Chain Risk Management (CSCRM) continuous monitoring program, inspired by NIST SP 800‑161 and real federal vendor‑risk workflows. This project generates synthetic vendor ecosystems, simulates cyber risk events, computes composite risk scores, and visualizes monitoring insights through an interactive Streamlit dashboard.



**Introduction**



Modern organizations depend on complex global supply chains, making vendor cybersecurity risk one of the most critical challenges in enterprise security. A single compromised supplier can expose sensitive data, disrupt operations, or introduce vulnerabilities across the entire ecosystem.



This project demonstrates how a CSCRM program can be designed, automated, and monitored using data-driven techniques. It includes synthetic data generation, risk scoring, continuous monitoring, and a fully interactive dashboard—mirroring the responsibilities of a Cyber Supply Chain Risk Program Lead.





**Problem Statement**



Organizations often lack visibility into:



Which vendors pose the highest cyber risk



How risk evolves over time



Which risk categories (breach, ransomware, vulnerabilities, compliance) are most impactful



How to prioritize Tier 1 suppliers



How to operationalize continuous monitoring



Without structured monitoring, risk escalations are slow, remediation is inconsistent, and leadership lacks actionable insights.



This project solves these challenges by simulating a complete CSCRM monitoring pipeline.



**Project Objectives**



This project was designed to:



* Generate a realistic synthetic vendor ecosystem with Tier 1 and Tier 2/3 suppliers
* 
* Simulate cyber risk events across multiple categories and severities
* 
* Compute composite vendor risk scores using weighted models
* 
* Produce daily monitoring snapshots for trend analysis
* 
* Build an interactive dashboard for real-time monitoring
* 
* Demonstrate governance-aligned CSCRM workflows
* 
* Showcase a portfolio-ready, end-to-end cybersecurity analytics project





**Methodology**



The project follows a structured CSCRM lifecycle:



1\. Data Generation



* 200 synthetic vendors created using Faker
* 
* Tier classification based on criticality
* 
* Industries assigned randomly
* 
* Daily cyber events simulated over 180 days



Risk categories aligned to NIST SP 800‑161:



* Data Breach
* 
* Ransomware
* 
* Vulnerability
* 
* Compliance



2\. Risk Scoring Engine



* Severity mapped to numeric scores
* 
* Weighted scoring model:
* 
* Data Breach — 0.35
* 
* Ransomware — 0.30
* 
* Vulnerability — 0.20
* 
* Compliance — 0.15
* 
* Composite risk score normalized to 0–100



Vendors categorized into:



* Low
* Medium
* High
* Critical



3\. Continuous Monitoring Pipeline 



* Daily event aggregation
* Vendor-level monitoring snapshots
* Tier-based trend analysis
* Identification of high-risk vendors



4\. **Dashboard Visualization**



* Built using Streamlit + Plotly:
* KPI summary
* Risk distribution charts
* Industry risk comparison
* Time-series monitoring
* Vendor drill-down panel





**Tools \& Technologies Used**



* Python — core programming
* Pandas / NumPy — data processing
* Faker — synthetic data generation
* YAML — configuration management
* Plotly — interactive visualizations
* Streamlit — monitoring dashboard
* Jupyter Notebook — exploratory analysis
* GitHub — version control \& portfolio hosting



**Key Findings**



From the simulated monitoring program:



* Tier 1 vendors consistently generated 2× more cyber events due to higher criticality and exposure.
* Data Breach and Vulnerability categories contributed the most to composite risk scores.
* Several vendors reached Critical risk levels due to repeated high-severity events.
* Industries such as Healthcare and Finance showed higher risk concentration.
* Daily monitoring revealed clear spikes in ransomware and breach events, indicating periods of elevated threat activity.
* These insights mirror real-world CSCRM challenges and demonstrate the value of continuous monitoring.



**Lessons Learned**



* Weighted scoring models significantly improve prioritization of high-risk vendors.
* Tier-based monitoring frequency is essential—Tier 1 suppliers require more aggressive oversight.
* Synthetic data can effectively simulate real-world CSCRM environments for training and portfolio projects.
* Dashboards dramatically improve stakeholder communication and escalation workflows.
* Governance artifacts (roles, workflows, escalation paths) are as important as technical analytics.



**Conclusion**



This project successfully demonstrates how a Cyber Supply Chain Risk Monitoring Program can be designed and operationalized using modern data analytics and visualization tools. It provides a realistic, end-to-end simulation of vendor risk management aligned with federal CSCRM expectations.



The platform can be extended into a production-grade system with integrations to real vendor monitoring tools (BitSight, SecurityScorecard), GRC platforms, and automated remediation workflows.



**Next Steps**



* Future enhancements may include:
* Machine learning–based risk prediction
* Integration with real threat intelligence feeds
* Automated vendor escalation workflows
* Role-based dashboards for CORs, PMs, and cybersecurity teams
* API-based ingestion from external monitoring platforms
* Mapping risks to NIST SP 800‑53 and NIST CSF controls
* Adding a remediation tracking module
