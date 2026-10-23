<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Supporting Material — Weak Order Rank Aggregation</title>
</head>
<body>

<h1>An optimization-based approach to ranking aggregation with weak order outputs — Supporting Material</h1>

<p>
  <a href="https://doi.org/10.5281/zenodo.23565472">
    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.23565472.svg" alt="DOI">
  </a>
</p>

<p>This repository provides the supplementary material for the article:</p>

<p><strong><em>“An optimization-based approach to ranking aggregation with weak order outputs”</em></strong></p>

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
 ├── 2/
 ├── 3/
 └── 4/
Models/
Docs/
 ├── Solutions.pdf
 └── Supplementary material: comparison of p-OBOP formulations.pdf
generator.py
README.md
</code></pre>

<ul>
  <li><code>Instances/1/</code>: PrefLib and MovieLens benchmark instances used for <strong>comparison with published heuristic results</strong>.</li>
  <li><code>Instances/2/</code>: the ten BOX instances used to <strong>evaluate the constrained OBOP variants</strong>.</li>
  <li><code>Instances/3/</code>: instances used for the <strong>sports applications</strong>: UEFA Champions League seeding pots, ISSF World Championship qualification, and World Artistic Gymnastics Championships qualification.</li>
  <li><code>Instances/4/</code>: the 25 synthetic instances used for the <strong>computational scalability experiments</strong>, with five instances for each size <code>n ∈ {20, 40, 60, 80, 100}</code>.</li>
  <li><code>Models/</code>: Xpress/Mosel model files implementing the MILP formulations presented in the article, including the static and lazy-constraint OBOP implementations. The latter includes the callback and separation routines.</li>
  <li><code>Docs/</code>:
    <ul>
      <li><code>Solutions.pdf</code>: supplementary document reporting the solutions obtained for the benchmark instances.</li>
      <li><code>Supplementary material: comparison of p-OBOP formulations.pdf</code>: additional computational comparisons of the p-OBOP formulations.</li>
    </ul>
  </li>
  <li><code>generator.py</code>: editable Python script used to generate the synthetic instances. It uses only the Python standard library.</li>
</ul>

<hr>

<h2>📄 Format of the <code>.dat</code> files</h2>

<p>Each instance is provided in plain text format. Benchmark instances contain:</p>

<ul>
  <li><code>n</code>: number of items.</li>
  <li><code>m</code>: number of voters.</li>
  <li><code>c</code>: an <code>n × n</code> matrix with aggregated preference intensities.</li>
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

<p>
The sports application files also contain descriptive metadata.
The synthetic instance files contain <code>n</code> and <code>c</code>,
without <code>m</code>, since their matrices are generated directly.
When using these files, omit <code>m</code> from the model's data
initialization and output statements.
</p>

<hr>

<h2>⚙️ Generating the synthetic instances</h2>

<p>
Open <code>generator.py</code> in PyCharm or another Python IDE and run it.
The generation parameters can be edited at the beginning of the script.
By default, it creates a <code>synthetic_instances/</code> folder alongside
the script and writes 25 instances named <code>I1.dat</code> to
<code>I25.dat</code>.
</p>

<p>The default configuration is:</p>

<ul>
  <li>Instance sizes: <code>n ∈ {20, 40, 60, 80, 100}</code>.</li>
  <li>Five instances per size.</li>
  <li>Beta distribution parameters: <code>ALPHA = 3</code> and <code>BETA = 1</code>.</li>
  <li>Random seed: <code>42</code>.</li>
  <li>Output precision: ten decimal places.</li>
</ul>

<p>
For each pair <code>r &lt; s</code>, the script draws a value from a
Beta(3, 1) distribution and rounds it to ten decimal places to obtain
<code>c[r][s]</code>. It then sets <code>c[s][r] = 1 - c[r][s]</code>.
All diagonal entries are set to <code>0.5</code>.
</p>

<p>
Instances are numbered consecutively by increasing size:
<code>I1.dat</code>–<code>I5.dat</code> have 20 items,
<code>I6.dat</code>–<code>I10.dat</code> have 40 items,
<code>I11.dat</code>–<code>I15.dat</code> have 60 items,
<code>I16.dat</code>–<code>I20.dat</code> have 80 items, and
<code>I21.dat</code>–<code>I25.dat</code> have 100 items.
</p>

<p>
The output directory can be changed by editing <code>OUTPUT_DIR</code>.
Running the script again in the same directory overwrites files with
the same names. No third-party Python packages are required.
</p>

<hr>

<h2>▶️ Using the models</h2>

<p>
The Mosel files in <code>Models/</code> correspond directly to the MILP
formulations described in the article. The experiments used
FICO Xpress 9.4.2 and Mosel 6.6.1.
To run an instance:
</p>

<ol>
  <li>Open one of the <code>.mos</code> files in Xpress.</li>
  <li>Set <code>DATAFILE</code> to an existing <code>.dat</code> file from <code>Instances/1/</code>, <code>Instances/2/</code>, <code>Instances/3/</code> or <code>Instances/4/</code>.</li>
  <li>Set <code>OUTFILE</code> to the desired output file and ensure that its parent directory exists.</li>
  <li>Set the parameters of the selected variant: <code>p</code> for the number of buckets, <code>q</code> for prescribed bucket sizes, <code>k</code> for the upper-part size, or the group definitions, representation bounds, and bucket limits <code>p1</code> and <code>p2</code> for Fair OBOP.</li>
  <li>For files without <code>m</code>, omit this parameter from the data initialization and output statements.</li>
  <li>Execute the model to obtain a weak order and its objective value. Inspect the termination status and bound to determine whether optimality was certified.</li>
</ol>

<p>
Adjust the instance paths, model parameters, and solver settings to match
the experiment described in the article.
</p>

<p>
The meaning and purpose of each formulation are described in detail
in the article.
</p>

<hr>

<h2>📝 Citation</h2>

<p>If you use this material, please cite:</p>

<pre><code>@unpublished{aledo2026aggregation,
  title   = {An optimization-based approach to ranking aggregation with weak order outputs},
  author  = {Aledo, Juan A. and Dom{\'i}nguez, Concepci{\'o}n and Jaime-Alc{\'a}ntara, Juan de Dios and Landete, Mercedes},
  note    = {Manuscript},
  year    = {2026}
}
</code></pre>

</body>
</html>
