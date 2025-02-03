<h2><a href="https://www.geeksforgeeks.org/problems/introduction-to-dp/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=introduction-to-dp">Introduction to DP</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Geek is learning data structures, and he recently learned about the top-down and bottom-up dynamic programming approaches</span><span style="font-size: 18px;">. Geek is having trouble telling them apart from one another.</span></p>
<p><span style="font-size: 18px;">When given an integer n, where n is based on a 0-based index, find the <strong>n<sup>th</sup></strong>&nbsp;Fibonacci number.</span></p>
<p><span style="font-size: 18px;">Every ith number in the series equals the sum of the <strong>(i-1)<sup>th</sup></strong>&nbsp;and<strong> (i-2)<sup>th</sup></strong>&nbsp;numbers, where the first and second numbers are specified as <strong>0</strong> and <strong>1</strong>, respectively.</span></p>
<p><span style="font-size: 18px;">For the given issue, code both <strong>top-down</strong> and <strong>bottom-up</strong> approaches</span><span style="font-size: 18px;">.</span></p>
<p><span style="font-size: 18px;"><strong>Note : </strong>As the answer might be large, <strong>return the final answer modulo 10<sup>9&nbsp;</sup>+ 7</strong></span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
n = 5
<strong>Output: </strong>5
<strong>Explanation:</strong> 0,1,1,2,3,5 as we can see 5<sup>th</sup>&nbsp;number is 5.</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
n = 6
<strong>Output: </strong>8
<strong>Explanation:</strong> 0,1,1,2,3,5,8 as we can see 6<sup>th</sup>&nbsp;number is 8.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= n &lt;= 10<sup>4</sup></span></p>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read input or print anything. Your task is to complete two&nbsp;functions <strong>topDown() and bottomUp()</strong> which take <strong>n</strong> as input parameters and return the <strong>n<sup>th&nbsp;</sup></strong>Fibonacci number.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong>&nbsp;O(n)<br><strong>Expected Auxiliary Space:</strong>&nbsp;O(n)</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Dynamic Programming</code>&nbsp;<code>Recursion</code>&nbsp;<code>Algorithms</code>&nbsp;