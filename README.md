<!DOCTYPE html>
<html lang="en">

<h1>Optimizing Weak Orders via MILP — Supporting Material</h1>

<p>This repository provides the supplementary material for the article:</p>

<p><strong><em>“Optimizing Weak Orders via MILP”</em></strong></p>

<p><strong>Authors</strong><br>
Juan A. Aledo – Universidad de Castilla-La Mancha (UCLM), Spain<br>
Concepción Domínguez – Universidad de Murcia (UM), Spain<br>
Juan de Dios Jaime-Alcántara – Universidad Miguel Hernández de Elche (UMH), Spain<br>
Mercedes Landete – Universidad Miguel Hernández de Elche (UMH), Spain
</p>

<hr>

<h2>📁 Repository structure</h2>

<pre><code>Instances/
 ├── 1/
 └── 2/
Models/
Docs/
 ├── solutions.pdf
 └── model-configs-and-counterexample.pdf
README.md
</code></pre>

<ul>
  <li><code>Instances/1/</code>: instances used for <strong>comparison experiments</strong> with existing models.</li>
  <li><code>Instances/2/</code>: instances used to <strong>evaluate the proposed MILP formulations</strong>.</li>
  <li><code>Models/</code>: Xpress/Mosel model files implementing the MILP formulations presented in the article.</li>
  <li><code>Docs/</code>:
    <ul>
      <li><code>solutions.pdf</code>: solutions of the considered instances/problems.</li>
      <li><code>model-configs-and-counterexample.pdf</code>: additional material including a comparison of model configurations and a counterexample illustrating the behaviour of the p-OBOP formulation.</li>
    </ul>
  </li>
</ul>

<hr>

<h2>📄 Format of the <code>.dat</code> files</h2>

<p>Each instance is provided in plain text format and contains:</p>

<ul>
  <li><code>n</code>: number of items</li>
  <li><code>m</code>: number of voters</li>
  <li><code>c</code>: an <code>n × n</code> matrix with aggregated preference intensities</li>
</ul>

<p>The general structure is:</p>

<pre><code>n: &lt;number_of_items&gt;
m: &lt;number_of_voters&gt;
c:
[
  &lt;row_1&gt;
  &lt;row_2&gt;
  ...
  &lt;row_n&gt;
]
</code></pre>

<p>Example:</p>

<pre><code>n: 10
m: 23
c:
[
 0.5 1 0.75 1 0.2941176 0.1363636 0.8095238 0.4090909 0 0.8
 0 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0 0.5
 0.25 0.5 0.5 1 0.25 0 0 0 0 0
 0 0.5 0 0.5 0.5 0 0.5 0 0 1
 0.7058824 0.5 0.75 0.5 0.5 0.3888889 0.9444444 0.5555556 0.0555556 0.7777778
 0.8636364 0.5 1 1 0.6111111 0.5 0.8636364 0.7391304 0.2608696 0.8181818
 0.1904762 0.5 1 0.5 0.0555556 0.1363636 0.5 0.3636364 0 0.2727273
 0.5909091 0.5 1 1 0.4444444 0.2608696 0.6363636 0.5 0.0434783 0.5454545
 1 1 1 1 0.9444444 0.7391304 1 0.9565217 0.5 1
 0.2 0.5 1 0 0.2222222 0.1818182 0.7272727 0.4545455 0 0.5
]
</code></pre>

<hr>

<h2>▶️ Using the models</h2>

<p>
The Mosel files in <code>Models/</code> correspond directly to the MILP formulations described in the article.
To run an instance:
</p>

<ol>
  <li>Open one of the <code>.mos</code> files in Xpress.</li>
  <li>Provide a <code>.dat</code> file from <code>Instances/1/</code> or <code>Instances/2/</code>.</li>
  <li>Execute the model to obtain the optimal weak order and the corresponding objective value.</li>
</ol>

<p>The meaning and purpose of each formulation are described in detail in the article.</p>

<hr>

<h2>📝 Citation</h2>

<p>If you use this material, please cite:</p>

<pre><code>@article{landete2025optimizing,
  title   = {Optimizing Weak Orders via MILP},
  author  = {Aledo, Juan A and Dom{\'i}nguez, Concepci{\'o}n and Jaime-Alc{\'a}ntara, Juan de Dios and Landete, Mercedes},
  journal = {to appear},
  year    = {2025}
}
</code></pre>

</body>
</html>
