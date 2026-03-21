# 3.b) Prototype Scope

## 1. Prototype Description

The purpose of our proof of concept (POC) is to demonstrate the very basic functionalities without implementing a graphical user interface.

The system will be used via a CLI and will support the following functions:

- User can create lighting configurations  
- User can group selected room/areas to saved configuration setting
- User can deploy selected configurations to lights
- User can view the status of all deployed lights (health check)  
- User can view configuration settings for each room  
- The system stores its state in memory (REQ-11 and REQ15: version control or persistent storage will not be implemented in this POC)

---

## 2. Demonstrate

The prototype demonstrates the following requirements:

- **REQ-1:** User can configure different lighting configurations  
- **REQ-2:** User can group configurations with rooms/areas (e.g., suites, corridors, front desk, individual rooms)  
- **REQ-3:** User can centrally sync configurations to every room  
- **REQ-6:** Basic centralized health check monitoring (online/offline)  
- **REQ-7:** Monitoring that shows saved and deployed lighting settings (e.g. brightness)

---

## VP Questions

- **"I have 200 rooms. How does this save me time compared to what I do today?"**  
  - REQ-1, REQ-2, REQ-3  

- **"We just renovated the 3rd floor suites. The standard rooms stay the same. Can your system handle that?"**  
  - REQ-2  

- **"My night manager needs to check if all rooms are set correctly before a conference group arrives tomorrow. How?"**  
  - REQ-6, REQ-7  

- **"I'm not technical. Can I use this, or do I need to call IT every time?"**  
  - The system will be documented. User training is not in scope.
