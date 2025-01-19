<h2><a href="https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1">Top View of Binary Tree</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">You are given a binary tree, and your task is to return its <strong>top view</strong>. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.</span></p>
<p><span style="font-size: 14pt;"><strong>Note:&nbsp;</strong></span></p>
<ul>
<li><span style="font-size: 14pt;">Return the nodes from the leftmost node to the rightmost node.</span></li>
<li><span style="font-size: 14pt;">If two nodes are at the same position (horizontal distance) and are outside the shadow of the tree, consider the leftmost node only.&nbsp;<br></span></li>
</ul>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>root[] = [1, 2, 3] <br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700490/Web/Other/blobid0_1733898095.png" width="249" height="219"> <br><strong>Output: </strong>[2, 1, 3]
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> root[] = [10, 20, 30, 40, 60, 90, 100]<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700490/Web/Other/blobid1_1733898122.png" width="306" height="271"> <br><strong>Output: </strong>[40, 20, 10, 30, 100]<br><strong>Explaination: </strong>The root 10 is visible.
On the left, 40 is the leftmost node and visible, followed by 20.
On the right, 30 and 100 are visible. Thus, the top view is 40 20 10 30 100.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> root[] = [1, 2, 3, N, 4, N, N, N, 5, N, 6]
       1
     /   \
    2     3
     \   
      4
       \
        5
         \
          6
<strong>Output: </strong>[2, 1, 3, 6]<br><strong>Explaination: </strong>Node 1 is the root and visible.
Node 2 is the left child and visible from the left side.
Node 3 is the right child and visible from the right side.
Nodes 4, 5, and 6 are vertically aligned, but only the lowest node 6 is visible from the top view. Thus, the top view is 2 1 3 6.</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ number of nodes ≤ 10<sup>5</sup><br>1 ≤ node-&gt;data ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Paytm</code>&nbsp;<code>Ola Cabs</code>&nbsp;<code>Walmart</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Binary Search Tree</code>&nbsp;<code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;