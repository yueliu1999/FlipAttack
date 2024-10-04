<div align="center">
<h2><a href="https://github.com/yueliu1999/FlipAttack/blob/main/FlipAttack.pdf">FlipAttack: Jailbreak LLMs via Flipping</a></h2>

[Yue Liu](https://yueliu1999.github.io/), [Xiaoxin He](https://xiaoxinhe.github.io/),  [Miao Xiong](https://miaoxiong2320.github.io/), [Jinlan Fu](https://jinlanfu.github.io/), [Shumin Deng](https://231sm.github.io/), [Bryan Hooi](https://bhooi.github.io/)

[National University Singapore](https://nus.edu.sg/)

</div>



<p align = "justify">
This paper proposes a simple yet effective jailbreak attack named FlipAttack against black-box LLMs. First, from the autoregressive nature, we reveal that LLMs tend to understand the text from left to right and find that they struggle to comprehend the text when noise is added to the left side. Motivated by these insights, we propose to disguise the harmful prompt by constructing left-side noise merely based on the prompt itself, then generalize this idea to 4 flipping modes. Second, we verify the strong ability of LLMs to perform the text-flipping task, and then develop 4 variants to guide LLMs to denoise, understand, and execute harmful behaviors accurately. These designs keep FlipAttack universal, stealthy, and simple, allowing it to jailbreak black-box LLMs within only 1 query. Experiments on 8 LLMs demonstrate the superiority of FlipAttack. Remarkably, it achieves ~98% attack success rate on GPT-4o, and ~98% bypass rate against 5 guardrail models on average.
</p>


<img src="./assets/radar_plot.png" alt="radar_plot" style="zoom:61%;" />

<p align="center">
Figure 1. The attack success rate of our proposed FlipAttack, the runner-up black-box attack ReNeLLM, and the best white-box attack AutoDAN on 8 LLMs for 7 categories of harm contents.
</p>





### Quick Start
1. change to source code dictionary
    ```
    cd ./src
    ```

2. calculate ASR-GPT of FlipAttack on AdvBench
    ```
    python eval_gpt.py
    ```
    ```
           ASR-GPT of FlipAttack against 8 LLMs on AdvBench       
    | ---------------------------- | ---------------------------- |
    |          Victim LLM          |           ASR-GPT            |
    | ---------------------------- | ---------------------------- |
    |        GPT-3.5 Turbo         |            94.81%            |
    |         GPT-4 Turbo          |            98.85%            |
    |            GPT-4             |            89.42%            |
    |            GPT-4o            |            98.08%            |
    |         GPT-4o mini          |            61.35%            |
    |      Claude 3.5 Sonnet       |            86.54%            |
    |        LLaMA 3.1 405B        |            28.27%            |
    |        Mixtral 8x22B         |            97.12%            |
    | ---------------------------- | ---------------------------- |
    |           Average            |            81.80%            |
    | ---------------------------- | ---------------------------- |
    ```
3. calculate ASR-GPT of FlipAttack on AdvBench subset (50 harmful behaviors)

    ```
    python eval_subset_gpt.py
    ```
    ```   
        ASR-GPT of FlipAttack against 8 LLMs on AdvBench subset    
    | ---------------------------- | ---------------------------- |
    |          Victim LLM          |           ASR-GPT            |
    | ---------------------------- | ---------------------------- |
    |        GPT-3.5 Turbo         |            96.00%            |
    |         GPT-4 Turbo          |           100.00%            |
    |            GPT-4             |            88.00%            |
    |            GPT-4o            |           100.00%            |
    |         GPT-4o mini          |            58.00%            |
    |      Claude 3.5 Sonnet       |            88.00%            |
    |        LLaMA 3.1 405B        |            26.00%            |
    |        Mixtral 8x22B         |           100.00%            |
    | ---------------------------- | ---------------------------- |
    |           Average            |            82.00%            |
    | ---------------------------- | ---------------------------- |
    ```

4. calculate ASR-DICT of FlipAttack on AdvBench

    ```
    python eval_dict.py
    ```
    ```      
          ASR-DICT of FlipAttack against 8 LLMs on AdvBench       
    | ---------------------------- | ---------------------------- |
    |          Victim LLM          |           ASR-DICT           |
    | ---------------------------- | ---------------------------- |
    |        GPT-3.5 Turbo         |            85.58%            |
    |         GPT-4 Turbo          |            83.46%            |
    |            GPT-4             |            62.12%            |
    |            GPT-4o            |            83.08%            |
    |         GPT-4o mini          |            87.50%            |
    |      Claude 3.5 Sonnet       |            90.19%            |
    |        LLaMA 3.1 405B        |            85.19%            |
    |        Mixtral 8x22B         |            58.27%            |
    | ---------------------------- | ---------------------------- |
    |           Average            |            79.42%            |
    | ---------------------------- | ---------------------------- |
    ```


5. calculate ASR-DICT of FlipAttack on AdvBench subset (50 harmful behaviors)
    ```
    python eval_subset_dict.py
    ```
    ```
       ASR-DICT of FlipAttack against 8 LLMs on AdvBench subset   
    | ---------------------------- | ---------------------------- |
    |          Victim LLM          |           ASR-DICT           |
    | ---------------------------- | ---------------------------- |
    |        GPT-3.5 Turbo         |            84.00%            |
    |         GPT-4 Turbo          |            86.00%            |
    |            GPT-4             |            72.00%            |
    |            GPT-4o            |            78.00%            |
    |         GPT-4o mini          |            90.00%            |
    |      Claude 3.5 Sonnet       |            94.00%            |
    |        LLaMA 3.1 405B        |            86.00%            |
    |        Mixtral 8x22B         |            54.00%            |
    | ---------------------------- | ---------------------------- |
    |           Average            |            80.50%            |
    | ---------------------------- | ---------------------------- |
    ```



### Main Result

<p align="center">
Table 1: The attack success rate (%) of 16 methods on 8 LLMs. The bold and underlined values are the best and runner-up results. The evaluation metric is ASR-GPT based on GPT-4.
</p>
<img src="./assets/performance.png" alt="performance" style="zoom:1%;" />





<img src="./assets/cost.png" alt="cost" style="zoom:61%;" />

<p align="center">
Figure 2: Token cost & attack performance of 16 attack methods. A larger bubble indicates higher token costs. FlipAttack, ReNeLLM, AutoDAN denotes the best black-box attack, the runner-up black-box attack, and the best white-box attack in terms of attack performance, respectively.
</p>



