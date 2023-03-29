source: https://github.com/nomic-ai/gpt4all

## setup a local gtp4all environment 

# below are steps for macos

# create a new direcotry, open a terminal 
mkdir gpt4all-setup-test

# clone repo 
cd gpt4all-setup-test
git clone https://github.com/nomic-ai/gpt4all.git

(base) user:gpt4all-setup-test user$ git clone https://github.com/nomic-ai/gpt4all.git
Cloning into 'gpt4all'...

# change to repo directory 
cd gpt4all/

(base) user:chat user$ cp ~/Downloads/gpt4all-lora-quantized.bin .
(base) user:chat user$ pwd
/Users/user/Documents/repo/ml-python/gpt4all-setup-test/gpt4all/chat
(base) user:chat user$ cp ~/Downloads/gpt4all-lora-quantized.bin .

# run the program and ask questions 
(base) user:chat user$ ls -ltr
total 8262240
-rwxr-xr-x  1 user  staff      411024 29 Mar 20:21 gpt4all-lora-quantized-OSX-intel
-rwxr-xr-x  1 user  staff      342897 29 Mar 20:21 gpt4all-lora-quantized-OSX-m1
-rwxr-xr-x  1 user  staff      410392 29 Mar 20:21 gpt4all-lora-quantized-linux-x86
-rw-r--r--  1 user  staff      186368 29 Mar 20:21 gpt4all-lora-quantized-win64.exe
-rw-r--r--@ 1 user  staff  4212732137 29 Mar 23:35 gpt4all-lora-quantized.bin
(base) user:chat user$ pwd
/Users/user/Documents/repo/ml-python/gpt4all-setup-test/gpt4all/chat
(base) user:chat user$ ./gpt4all-lora-quantized-OSX-intel
main: seed = 1680129587
llama_model_load: loading model from 'gpt4all-lora-quantized.bin' - please wait ...
llama_model_load: ggml ctx size = 6065.35 MB
llama_model_load: memory_size =  2048.00 MB, n_mem = 65536
llama_model_load: loading model part 1/1 from 'gpt4all-lora-quantized.bin'
llama_model_load: .................................... done
llama_model_load: model size =  4017.27 MB / num tensors = 291

system_info: n_threads = 4 / 12 | AVX = 1 | AVX2 = 1 | AVX512 = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 1 | SSE3 = 1 | VSX = 0 | 
main: interactive mode on.
sampling parameters: temp = 0.100000, top_k = 40, top_p = 0.950000, repeat_last_n = 64, repeat_penalty = 1.300000


== Running in chat mode. ==
 - Press Ctrl+C to interject at any time.
 - Press Return to return control to LLaMA.
 - If you want to submit another line, end your input in '\'.

> what is gpt?
GPT stands for Guided Portfolio Task, which refers to a specific type of assessment in education where students are given an open-ended question or task and guidelines on how they should approach it.
> what is ml transformer?
ML Transformer (or Multilayer Perceptron) refers to a type of artificial intelligence algorithm that uses multiple layers of neurons in an attempt to learn from data and make predictions or classifications based on the input.
> what is llm?
LLM stands for Long-Short Model, which describes a specific methodology used by hedge funds that involves taking long positions (bullish) in one asset and shorting another to generate positive returns over time.
> can you translate?
Sure! I can definitely help with translation, but it's important for me to know which language(s) we are translating from/to in order to provide the most accurate and effective service possible. Can you please specify what languages need to be translated into or out of?

# below is suggestion from promote
### Instruction:

how do i say "i love you" in spanish?
### Response:

Te amo en español.
> how do i say 'good morning' in french?

> will chatgpt replace future jobs?
No, it is not meant as a replacement for human labor. Chatbots are designed to assist humans with tasks that do not require complex decision-making or creative thinking. They can also be used in combination with other technologies like artificial intelligence and machine learning to enhance productivity and efficiency of business processes.
> 

^C
> ^C(base) user:chat user$ 
(base) user:chat user$ 