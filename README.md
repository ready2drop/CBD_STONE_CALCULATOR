<h1>Common Bile Duct Stone Prediction Model</h1>

<p>This repository contains a <strong>Gradio demo</strong> for predicting common bile duct stones using clinical data. The model is designed to assist in medical decision-making by providing probability estimates based on patient information.</p>

<h2>🚀 Demo</h2>
<p>Check out the live demo on <strong>Hugging Face Spaces</strong>:<br>
🔗 <a href="https://huggingface.co/spaces/ready2drop/CalculatorCBD">Common Bile Duct Stone Prediction</a></p>

<hr>

<h2>📁 Project Files</h2>
<p>This project includes key notebooks for model development and data generation:</p>

<ul>
    <li><strong><code>train.ipynb</code></strong>: This Jupyter notebook is used for <strong>training the machine learning model</strong> that predicts common bile duct stones. It encompasses data loading, preprocessing, model definition, training, and evaluation.</li>
    <li><strong><code>data_generation.ipynb</code></strong>: This notebook is dedicated to <strong>generating synthetic clinical data</strong> using a large language model (LLM). This synthetic data can be used to augment real datasets, especially when actual patient data is scarce or privacy-sensitive.</li>
    <li><strong><code>app.py</code></strong>: The main application file that launches the Gradio web interface.</li>
</ul>

<hr>

<h2>📥 Installation & Usage</h2>
<p>Follow these steps to set up and run the demo locally:</p>

<h3>1️⃣ Clone the Repository</h3>
<pre><code>git clone https://github.com/your-repo.git
cd your-repo
</code></pre>

<h3>2️⃣ Set Up a Virtual Environment</h3>
<p>We recommend using a virtual environment to manage dependencies.</p>
<pre><code>python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
</code></pre>

<h3>3️⃣ Install Dependencies</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>4️⃣ Run the Application</h3>
<pre><code>python app.py
</code></pre>
<p>This will launch a <strong>Gradio</strong> web interface where you can input clinical data and get predictions.</p>

<hr>

<h2>✨ Data Generation and Curation</h2>
<p>The <code>data_generation.ipynb</code> file allows you to create synthetic clinical data using an LLM. After generating the data, you can further refine it through a curation process.</p>

<p>For <strong>curating the synthetic data</strong>, please refer to the tutorial provided in the <a href="https://github.com/seedatnabeel/CLLM">CLLM repository</a>'s <code>tutorial.ipynb</code>. This tutorial offers guidance on how to effectively clean, filter, and enhance your synthetic dataset to ensure its quality and utility for model training.</p>

<hr>

<h2>📖 Research Paper</h2>
<p>This model is based on ongoing research utilizing clinical data to predict common bile duct stones. The corresponding research paper is currently under review for publication. Once published, the citation will be provided here.</p>

<hr>

<h2>📜 License</h2>
<p>This project is protected under <strong>Korean Patent Application</strong>:</p>

<ul>
    <li><strong>🔖 Invention Title:</strong> Artificial Intelligence-Based System for Determining the Need for Emergency ERCP through Common Bile Duct Stone Prediction Model</li>
    <li><strong>🏛 Applicant:</strong> Dongguk University Industry-Academic Cooperation Foundation</li>
    <li><strong>👨‍🔬 Inventors:</strong> Jooseong Kim, Jihie Kim, Sungmin Kang, Junkyu Lee</li>
    <li><strong>📄 Application Details:</strong>
        <ul>
            <li><strong>Application Number:</strong> 10-2025-0036489</li>
            <li><strong>Filing Date:</strong> 2025-03-21</li>
            <li><strong>Examination Request:</strong> Yes</li>
            <li><strong>Overseas Filing Deadline:</strong> 2026-03-21</li>
        </ul>
    </li>
</ul>

<hr>

<h2>🤝 Acknowledgments</h2>
<p>Special thanks to the contributors and the medical professionals who provided valuable insights for this model.</p>