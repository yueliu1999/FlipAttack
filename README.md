<div align="center">
<h2><a href="https://github.com/yueliu1999/FlipAttack/blob/main/FlipAttack.pdf">FlipAttack: Jailbreak LLMs via Flipping</a></h2>

[Yue Liu](https://yueliu1999.github.io/), [Xiaoxin He](https://xiaoxinhe.github.io/),  [Miao Xiong](https://miaoxiong2320.github.io/), [Jinlan Fu](https://jinlanfu.github.io/), [Shumin Deng](https://231sm.github.io/), [Bryan Hooi](https://bhooi.github.io/)

[National University Singapore](https://nus.edu.sg/)

</div>









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
