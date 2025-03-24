# Abstract
Stop Stealing from Grandma:
Preventing Phishing Attacks on the Elderly

Scammers look for new ways to trick the elderly out of their money. Current messages are largely ineffective. These messages are inconcise as they include convoluted, technical language filled with jargon. We evaluated currently available messages to find their strengths and weaknesses through Term Frequency-Inverse Document Frequency and sentiment analysis. We identified linguistic elements to determine that simple, easy-to-read, positive language made for the most effective messages. By relaying this to the caregivers, they can now use these strategies to train the elderly to prevent them from clicking suspicious links. Stealing from grandma will be harder than ever.



# Risk Communication for Elderly Phishing Protection  

##  Methods  

###  GitHub Repository  
The full implementation of our pipeline, along with README files and documentation, can be found at:  
[**GitHub Repository Link**](https://github.com/AlexanderRoylance/csci491.git)  

###  Pipeline Structure  
Below is a visual representation of our implemented pipeline:  

![Pipeline Structure](https://github.com/user-attachments/assets/720438aa-430d-423d-b1de-f4f3276b95a6)  

**Pipeline Levels:**  

1. **Scraping Level** → Extracts website text  
2. **Preprocessing Level** → Cleans and standardizes text  
3. **Operationalization Level** → Extracts Hero/Victim/Villain language  
4. **NLP Level** → Computes TF-IDF and sentiment analysis  
5. **Message Generation Level** → Constructs risk communication message segments  
6. **Analysis Level** → Visualizes and contextualizes findings  

---

##  Results  

Our analysis produced the following key findings:  

1. **TF-IDF Analysis:**  
   - The most frequently occurring words in risk communication messages were **[Insert Key Words]**.  
   - Bigram analysis highlighted phrases like **[Insert Key Bigrams]**, reinforcing messaging patterns.  

2. **Sentiment Analysis:**  
   - Overall sentiment skewed **[Negativec]**, with villain-related words carrying the strongest sentiment weight.  
   - Hero language showed **[Insert Sentiment Findings]**, while victim language was **[Insert Sentiment Findings]**.  

###  Graphs & Figures  

**TF-IDF Score Table:**  

| Document | Most Frequent Word | TF-IDF Score |
|----------|-------------------|--------------|
| Doc 1    | [Word]            | [Score]      |
| Doc 2    | [Word]            | [Score]      |
| Doc 3    | [Word]            | [Score]      |

**Sentiment Analysis**
![](https://github.com/user-attachments/assets/39df3181-069b-4923-beb0-79fe8fcaff53)


**Hero Frequecy**

![](https://github.com/bhagdht/ChumBucket_RiskManagment/blob/main/3_ResultParty/hero_freq.png?raw=true) 
**Victim Frequecy**

![](https://github.com/bhagdht/ChumBucket_RiskManagment/blob/main/3_ResultParty/victim_freq.png?raw=true)
**Villain Frequecy**

![](https://github.com/bhagdht/ChumBucket_RiskManagment/blob/main/3_ResultParty/villain_freq.png?raw=true)

---

##  Discussion  

### **Practical Implications for Practitioners**  

- **Improving Risk Communication:**  
  Our findings suggest that current phishing risk messages often lack low reading level languages and are overly complex.  
  - Practitioners should focus on **[Key Recommendation, e.g., avoiding fear-based messaging, increasing empowerment narratives]**.  
  - Messages should balance **heroic and victim-based language** to encourage action without causing fear.  

- **Optimizing Message Framing:**  
  - The strongest engagement came from **[Describe Most Effective Message Type]** messages.  
  - **Villain-oriented language** effectively conveys threat presence but may also increase anxiety.  

### **Threats to Validity**  

- **Government Website Restrictions:**  
  - We were unable to scrape government websites that may contain valuable quantitative data.  
  - Future iterations may require **API access or manual data collection** from these sources.  

- **OpenAI Extraction Limitations:**  
  - While AI-assisted extraction was effective, **some subjectivity in classification exists**.  
  - Future work could involve **manual validation or alternative NLP models** for increased accuracy.  

---

### ** Next Steps**  

- **Refining NLP Extraction:** Improve hero/victim/villain classification accuracy.  
- **Extending Data Sources:** Seek alternative sources for quantitative risk messaging data.  
- **A/B Testing Messages:** Evaluate real-world effectiveness with target audiences.  

---  
