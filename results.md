# Abstract
Stop Stealing from Grandma:
Preventing Phishing Attacks on the Elderly

Scammers look for new ways to take advantage of the elderly. As important as this issue is, the current risk communication messages fall short. These messages 
are inconcise as they include negative or technical language filled with jargon. We evaluated currently available messages to find their strengths and 
weaknesses through Term Frequency-Inverse Document Frequency and sentiment analysis. We identified linguistic elements to determine that simple, easy-to-read, 
positive language made for the most effective messages. By relaying this to the caregivers, they can now use these strategies to train the elderly to prevent 
them from clicking suspicious links. Stealing from grandma will be harder than ever.



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
Our research came to find that the most common words among the different risk communication messages were descriptive words of the target population or issue; adults, privacy, scam, for example. Through TF-IDF analysis of bigrams, phrases like "aging adults" and "older victims" appeared the most frequently. These bigrams are examples of how current messages portray the target audience as an aging, frail group which reinforces the idea that victim language is the most prevelant within them.
   - The most frequently occurring words in risk communication messages were adults, privacy, and scam.  
   - Bigram analysis highlighted phrases like aging adults and older victims, reinforcing messaging patterns.  

2. **Sentiment Analysis:**
Sentiment analysis showed an overall negative skew, with villain-related words carrying the strongest and most negative sentiment weight. Victim words, the most prevelant from TF-IDF, hold a negative value as well, adding to the defeatist tone of the messages. Any hero language used holds a high sentiment value, but was far outweighed by the victim or villain language.
   - Overall sentiment skewed negative, with villain-related words carrying the strongest sentiment weight.  
   - Hero language showed higher sentiment scores, but victim language was far more prevelant.  

3. **Segment Generation:**
Segment generation and analysis is the final step in the research pipeline.

###  Graphs & Figures  

**TF-IDF Score Table:**  
![](https://github.com/user-attachments/assets/9ec5d407-9de8-4b66-8194-936799bc614c)


**Sentiment Analysis**
![](https://github.com/user-attachments/assets/39df3181-069b-4923-beb0-79fe8fcaff53)


![Hero Frequency](https://github.com/bhagdht/ChumBucket_RiskManagment/blob/main/3_ResultParty/hero_freq.png?raw=true) 


![Victim Frequency](https://github.com/bhagdht/ChumBucket_RiskManagment/blob/main/3_ResultParty/victim_freq.png?raw=true)

![Villain Frequency](https://github.com/bhagdht/ChumBucket_RiskManagment/blob/main/3_ResultParty/villain_freq.png?raw=true)

---

##  Discussion  

### **Practical Implications for Practitioners**  

- **Improving Risk Communication:**  
  Our findings suggest that current phishing risk messages often use simple terminology, they include too many technical terms. While our results do show
  thatsmaller words like "scam" and "older" are more common, the risk communication areas are filled with terms like "fraudelent digital impersonators." This is not to
  say that higher level words do not have their place in these messages, but it is important to recognize the constraints of the language we can use to address
  the target audience. Those creating the messages, as well as the people that are relaying them to those that need to hear it should take this into
  consideration. The other important piece of information obtained from these findings is that the current messages are far too often negative. The villain
  language used in almost every message brings a negative feeling of defeat before the reader is even through the first paragraph. Again, this type of language
  does need to be included, especially to create the narrative that the hero will eventually get themself out of, but it needs to be used sparingly. An emphasis
  on hero-driven narratives should be the goal of effective communication, but a certain amount of victim language should be used to show that the audience is still vulnerable. Showing
  these findings to the caregivers so that they can pass the information on to the elderly will prove to be a much stronger method of risk communication than
  current measures. By acting through a median, message creators can get the vital information to the audience without needing to worry about emphasizing
  positive narratives, as the caregivers will already be enforcing it.

  less absolute
  provide credibility and data
  fix graphs
  more emotional at the end
  

### **Threats to Validity**  

- **Government Website Restrictions:**
  Scraping sensitive data from Government websites was not allocable in this timeframe, leading to a reliance on magazine and news-based information. The sites
  we were not able to get to could contain important statistical data for what areas are most susceptible to phishing schemes, as well as what education level
  teaches people technical literacy. Future iterations will require manual data collection from these sources in order to gather more data and strengthen our
  claim. Even without these resources, valuable data was still collected from reputable news sources. Quantitative data was gathered and processed to generate figures regarding at-risk populations.
- **OpenAI Character Coding:**
  OpenAI and AI-assisted extraction for character language is vital to this project, 
  however, it can sometimes incorrectly and ineffectively classify language. To 
  nullify common problems, the classification words are verified at each step to 
  ensure proper classification and accurate results. VHuman coding or manual 
  validation could be the next step to increase the validity of the tests and the 
  project as a whole.
say why these are not making the article bad
external threats
---

### **Next Steps**  

- **Refining NLP Extraction:** Improve hero/victim/villain classification accuracy.  
- **Extending Data Sources:** Seek alternative sources for quantitative risk messaging data.  
- **A/B Testing Messages:** Evaluate real-world effectiveness with target audiences.  

---  
