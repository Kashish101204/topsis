# Title: TOPSIS Web Application

---

## 1. Methodology

<p align="center">
  <img src="assets/methodology.png" alt="Methodology Diagram" width="700">
</p>

**Workflow:**

Data Collection → Data Pre-processing → TOPSIS Computation → Result Generation → Result Delivery

---

## 2. Description

- **Input Type:** CSV file containing alternatives and criteria values  
- **Decision Method:** TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)  
- **User Inputs:**  
  - Weights (comma-separated)  
  - Impacts (+ or -)  
  - Email ID  
- **Output:**  
  - CSV file with TOPSIS score and rank  
- **Platform:** Web-based (Flask)

---

## 3. Input / Output

### Sample Input
- CSV file with numeric criteria
- Weights: `1,1,1,1`
- Impacts: `+,+,-,+`

### Sample Output

| Alternative | Topsis Score | Rank |
|------------|--------------|------|
| A1         | 0.82         | 1    |
| A2         | 0.65         | 2    |
| A3         | 0.41         | 3    |

---

## 4. Screenshot
<img width="675" height="684" alt="Screenshot 2026-02-04 230721" src="https://github.com/user-attachments/assets/cb93777f-1877-4718-9f6e-7bc6de688007" />




