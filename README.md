![image](https://github.com/user-attachments/assets/f1f15de2-905e-4cd8-b967-5ddcce7b82f2)# 🧠 SONSC Biomedical AutoClustering

This repository implements **SONSC** (Self-Optimized Number of SubClusters) for automatic clustering of biomedical data using the **Improved Separation Index (ISI)**. It has been evaluated on:
- 🧬 TCGA-BRCA Gene Expression Profiles
- ❤️ ECG signals from the MIT-BIH Arrhythmia Database
- 🫁 Chest X-ray images from NIH dataset

---

## 📦 Datasets

| Dataset         | Description                              | Format      |
|----------------|------------------------------------------|-------------|
| TCGA-BRCA       | Gene expression profiles for breast cancer | CSV         |
| MIT-BIH         | ECG records and annotations               | .csv/.txt    |
| NIH Chest X-ray | Chest X-ray images (grayscale, 1024×1024) | .png         |

---

## ⚙️ Method Overview

SONSC is an unsupervised method that automatically finds the optimal number of clusters by maximizing the **ISI** score:

> **ISI = Separation² / (Cohesion + Separation²)**  
> - *Cohesion*: Within-cluster compactness  
> - *Separation*: Between-cluster distinctiveness

The search continues until ISI starts to decrease — the previous `k` is selected as optimal.

---

## 🚀 Usage

1. **Clone the repo**
   ```bash
   git clone https://github.com/Mojtaba-jahanian/SONSC-Biomedical-AutoClustering.git
   cd SONSC-Biomedical-AutoClustering
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run examples

bash
Copy
Edit
python run_tcga.py       # Gene Expression
python run_mitbih.py     # ECG Signals
python run_xray.py       # Chest X-rays
📊 Visualization
Visualizations include:

ISI vs. Number of Clusters

t-SNE projections

Heatmaps and Boxplots for expression


🛠 Requirements
Python ≥ 3.8

NumPy, Pandas, scikit-learn, matplotlib, seaborn

OpenCV or PIL (for image datasets)

📜 License
MIT License © Mojtaba Jahanian
Feel free to fork, cite, and contribute!

📬 Contact
---

## 📬 Contact

If you have any questions, suggestions, or collaboration opportunities, feel free to reach out:

- **Mojtaba Jahanian** – [mojtaba160672000@aut.ac.ir](mailto:mojtaba160672000@aut.ac.ir)
- **Abbas Karimi** – [Abbas.karimi@iau.ac.ir](mailto:Abbas.karimi@iau.ac.ir)
- **Nafiseh Osati Eraghi** – [Nafiseh.osati@iau.ac.ir](mailto:Nafiseh.osati@iau.ac.ir)
- **Faraneh Zarafshan** – [Fzarafshan@aiau.ac.ir](mailto:Fzarafshan@aiau.ac.ir)

Project Link: [https://github.com/Mojtaba-jahanian/SONSC-Biomedical-AutoClustering](https://github.com/Mojtaba-jahanian/SONSC-Biomedical-AutoClustering)

