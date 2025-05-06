# 🧠 KMeans Clustering

Hey there! 👋 
This project is my solution for my AI & ML Internship, where I embarked on a quest to segment mall customers using K-Means clustering. 🛒 I dove deep into unsupervised learning, explored the dataset, and experimented with various techniques to uncover meaningful customer groups. Here’s the story of my journey, the challenges I faced, and how I built this project from scratch!

---

## 🌟 What This Project Is About
This project focuses on **customer segmentation** using the K-Means clustering algorithm. The dataset I worked with is the **Mall Customer Segmentation Dataset**, which contains customer details like Annual Income and Spending Score. My goal was to group customers into meaningful clusters that could help a business target specific customer segments for marketing. 🚀

Through extensive research, I learned about the Elbow Method, Silhouette Score, and PCA visualization, applying them step-by-step to ensure my clustering was both effective and insightful. Here’s what I accomplished:
- Loaded and explored the dataset to understand customer patterns. 📊
- Used the Elbow Method to find the optimal number of clusters. 📈
- Applied K-Means clustering to segment customers into distinct groups. 🗂️
- Visualized the clusters with color-coding to make the results interpretable. 🎨
- Evaluated the clustering quality using the Silhouette Score. ✅
- Added a PCA-based visualization to see the clusters in a reduced 2D space. 📉

---

## 📁 Project Structure
Here’s how I organized my project after experimenting with different structures:
KMeans-Clustering/
├── data/
│   └── Mall_Customers.csv       # 📂 The dataset I used for clustering
├── src/
│   ├── load_data.py             # 🔍 Loads and explores the dataset
│   ├── elbow_method.py          # 📈 Determines optimal k using the Elbow Method
│   ├── kmeans_clustering.py     # 🤖 Applies K-Means and visualizes clusters
│   ├── silhouette_score.py      # ✅ Evaluates clustering quality
│   ├── pca_visualization.py     # 📉 Visualizes clusters using PCA
├── outputs/
│   ├── elbow_plot.png           # 📊 Elbow Method plot
│   ├── cluster_plot.png         # 🎨 Color-coded cluster plot
│   ├── pca_plot.png             # 📉 PCA visualization plot
├── main.py                      # 🚀 Main script to run the entire pipeline
├── README.md                    # 📝 You're reading it!
├── requirements.txt             # 🛠️ Dependencies to run the project
├── .gitignore                   # 🚫 Ignores unnecessary files


I decided to keep all plots in an `outputs/` folder to keep things tidy, which I learned is a good practice in data science projects. 🧹

---

## 🧑‍💻 My Journey and Research
When I started this project, I wasn’t very familiar with K-Means clustering, so I spent time researching how unsupervised learning works. 📚 I read articles on Medium, watched YouTube tutorials, and referred to Scikit-learn’s documentation to understand the algorithm. Here’s what I learned and how I applied it:

- **Dataset Exploration**: I began by loading the dataset and checking for missing values. I printed summary statistics to get a feel for the data, which helped me decide to use Annual Income and Spending Score as my clustering features. 🔍
- **Elbow Method**: I learned that the Elbow Method helps find the optimal number of clusters (`k`). After plotting it, I noticed a bend at `k=5`, which I used for clustering. 📈
- **K-Means Clustering**: Applying K-Means was straightforward, but I spent time experimenting with different `random_state` values to ensure consistent results. I also added color-coded visualization to make the clusters visually appealing. 🎨
- **Evaluation**: I researched evaluation metrics and found the Silhouette Score to be a great way to measure clustering quality. A score of ~0.55 for `k=5` confirmed my clusters were well-separated. ✅
- **PCA Visualization**: I wanted to go the extra mile, so I explored PCA to visualize the clusters in 2D. It was challenging to understand at first, but after reading about dimensionality reduction, I got it working! 📉

One challenge I faced was organizing the code. Initially, I had everything in one file, but it got messy. So, I refactored it into modular scripts in the `src/` folder, which made the project much cleaner and easier to maintain. 🧹 I also learned about type hints in Python and added them to my functions to make the code more professional—I hope you’ll notice the effort! 😄

---

## 🚀 How to Run My Project
If you’d like to download and run my code, I’ve made it super easy! Follow these steps to see the clustering in action. 🌟

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/KMeans-Clustering.git
   cd KMeans-Clustering

This will download my project to your local machine. 📥
2. **Install Dependencies:** I’ve included a requirements.txt file with all the libraries I used. Make sure you have Python installed, then run:
   ```bash
pip install -r requirements.txt

-This installs pandas, numpy, matplotlib, scikit-learn, and seaborn. 🛠️

3. **Prepare the Dataset:** The dataset (Mall_Customers.csv) is already included in the data/ folder. If it’s missing, you can download it from Kaggle and place it in the data/ folder. 📂

4. **Run the Script:** I’ve created a main.py script that runs the entire pipeline. Just run:
   ```bash
python main.py

-This will:

    Load and explore the dataset.
    Generate the Elbow plot (outputs/elbow_plot.png).
    Apply K-Means clustering and save the color-coded cluster plot (outputs/cluster_plot.png).
    Print the Silhouette Score to the console.
    Save the PCA visualization plot (outputs/pca_plot.png).


5. **Check the Outputs:** All plots are saved in the outputs/ folder. You can open them to see the results of my clustering! 📊

📈 What You’ll See

Here’s what the project produces:

    Elbow Plot (outputs/elbow_plot.png): Shows the optimal number of clusters (k=5). 📈
    Color-Coded Clusters (outputs/cluster_plot.png): Visualizes the five customer segments based on income and spending. 🎨
    Silhouette Score: Printed to the console (~0.55), confirming the clusters are well-separated. ✅
    PCA Visualization (outputs/pca_plot.png): A 2D view of the clusters using PCA, which I added as a bonus! 📉

🧰 Tech Stack

I used the following tools and libraries to build this project:

    Python: For coding the entire pipeline. 🐍
    pandas & numpy: For data manipulation and numerical operations. 📊
    matplotlib & seaborn: For creating beautiful plots. 🎨
    scikit-learn: For K-Means clustering, Silhouette Score, and PCA. 🤖

📝 My Insights

After clustering, I identified five distinct customer segments:

    1. High Income, High Spending: Big spenders who can be targeted with premium offers. 💎
    2. High Income, Low Spending: Potential for upselling—maybe they need incentives! 💡
    3. Average Income, Average Spending: The average customer group, good for general promotions. 🛍️
    4. Low Income, High Spending: Budget-conscious but willing to spend—great for deals! 🤑
    5. Low Income, Low Spending: Might need budget-friendly options to engage. 💸

These insights could help a business tailor its marketing strategies, which I found really exciting to discover through clustering! 🚀  
