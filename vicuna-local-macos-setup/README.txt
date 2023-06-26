This helps setup a running vicuna chat program in local MacOS Intel CPU.

#
macOS Monterey
Version: 12.4 

#
uname -a 
Darwin user-2.local 21.5.0 Darwin Kernel Version 21.5.0: Tue Apr 26 21:08:22 PDT 2022; 
root:xnu-8020.121.3~4/RELEASE_X86_64 x86_64



#create a new dir
mkdir vicuna-local

#create python venv 
python -m venv  .venv
. .venv/bin/activate 

# check out llama.cpp
git clone https://github.com/ggerganov/llama.cpp.git 
# follow their README.md 
cd llama.cpp
make 

cd models 
wget https://huggingface.co/vicuna/ggml-vicuna-13b-1.1/resolve/main/ggml-vic13b-uncensored-q5_1.bin
#wget https://huggingface.co/vicuna/ggml-vicuna-13b-1.1/resolve/main/ggml-vic13b-uncensored-q8_0.bin

# or manually download model from url 
# select the model to download 
https://huggingface.co/vicuna/ggml-vicuna-13b-1.1/tree/main

# create a dir for models 
mkdir models 
#copy downloaded model inside the folder, the path + model name will be used in below command line 

# run program, in same folder 
# remove flag --ignore-eos, stop continuing responding, try this first  
./main -i --interactive-first -r "### Human:" --temp 0 -c 2048 -n -1 --repeat_penalty 1.2 --instruct -m ./models/ggml-vic13b-q4_0.bin

# load large model, 13.gb size, a bit slow
./main -i --interactive-first -r "### Human:" --temp 0 -c 2048 -n -1 --ignore-eos --repeat_penalty 1.2 --instruct -m ./models/ggml-vic13b-uncensored-q8_0.bin

# load 8 gb model, also slow
./main -i --interactive-first -r "### Human:" --temp 0 -c 2048 -n -1 --ignore-eos --repeat_penalty 1.2 --instruct -m ./models/ggml-vic13b-q4_0.bin


......
== Running in interactive mode. ==
 - Press Ctrl+C to interject at any time.
 - Press Return to return control to LLaMa.
 - To return control without starting a new line, end your input with '/'.
 - If you want to submit another line, end your input with '\'.

>



# help messsage 
./main -h
usage: ./main [options]

options:
  -h, --help            show this help message and exit
  -i, --interactive     run in interactive mode
  --interactive-first   run in interactive mode and wait for input right away
  -ins, --instruct      run in instruction mode (use with Alpaca models)
  --multiline-input     allows you to write or paste multiple lines without ending each in '\'
  -r PROMPT, --reverse-prompt PROMPT
                        halt generation at PROMPT, return control in interactive mode
                        (can be specified more than once for multiple prompts).
  --color               colorise output to distinguish prompt and user input from generations
  -s SEED, --seed SEED  RNG seed (default: -1, use random seed for < 0)
  -t N, --threads N     number of threads to use during computation (default: 6)
  -p PROMPT, --prompt PROMPT
                        prompt to start generation with (default: empty)
  -e                    process prompt escapes sequences (\n, \r, \t, \', \", \\)
  --prompt-cache FNAME  file to cache prompt state for faster startup (default: none)
  --prompt-cache-all    if specified, saves user input and generations to cache as well.
                        not supported with --interactive or other interactive options
  --prompt-cache-ro     if specified, uses the prompt cache but does not update it.
  --random-prompt       start with a randomized prompt.
  --in-prefix STRING    string to prefix user inputs with (default: empty)
  --in-suffix STRING    string to suffix after user inputs with (default: empty)
  -f FNAME, --file FNAME
                        prompt file to start generation.
  -n N, --n-predict N   number of tokens to predict (default: -1, -1 = infinity)
  --top-k N             top-k sampling (default: 40, 0 = disabled)
  --top-p N             top-p sampling (default: 0.9, 1.0 = disabled)
  --tfs N               tail free sampling, parameter z (default: 1.0, 1.0 = disabled)
  --typical N           locally typical sampling, parameter p (default: 1.0, 1.0 = disabled)
  --repeat-last-n N     last n tokens to consider for penalize (default: 64, 0 = disabled, -1 = ctx_size)
  --repeat-penalty N    penalize repeat sequence of tokens (default: 1.1, 1.0 = disabled)
  --presence-penalty N  repeat alpha presence penalty (default: 0.0, 0.0 = disabled)
  --frequency-penalty N repeat alpha frequency penalty (default: 0.0, 0.0 = disabled)
  --mirostat N          use Mirostat sampling.
                        Top K, Nucleus, Tail Free and Locally Typical samplers are ignored if used.
                        (default: 0, 0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0)
  --mirostat-lr N       Mirostat learning rate, parameter eta (default: 0.1)
  --mirostat-ent N      Mirostat target entropy, parameter tau (default: 5.0)
  -l TOKEN_ID(+/-)BIAS, --logit-bias TOKEN_ID(+/-)BIAS
                        modifies the likelihood of token appearing in the completion,
                        i.e. `--logit-bias 15043+1` to increase likelihood of token ' Hello',
                        or `--logit-bias 15043-1` to decrease likelihood of token ' Hello'
  -c N, --ctx-size N    size of the prompt context (default: 512)
  --ignore-eos          ignore end of stream token and continue generating (implies --logit-bias 2-inf)
  --no-penalize-nl      do not penalize newline token
  --memory-f32          use f32 instead of f16 for memory key+value (default: disabled)
                        not recommended: doubles context memory required and no measurable increase in quality
  --temp N              temperature (default: 0.8)
  -b N, --batch-size N  batch size for prompt processing (default: 512)
  --perplexity          compute perplexity over the prompt
  --keep                number of tokens to keep from the initial prompt (default: 0, -1 = all)
  --mlock               force system to keep model in RAM rather than swapping or compressing
  --no-mmap             do not memory-map model (slower load but may reduce pageouts if not using mlock)
  --numa                attempt optimizations that help on some NUMA systems
                        if run without this previously, it is recommended to drop the system page cache before using this
                        see https://github.com/ggerganov/llama.cpp/issues/1437
  --mtest               compute maximum memory usage
  --export              export the computation graph to 'llama.ggml'
  --verbose-prompt      print prompt before generation
  --lora FNAME          apply LoRA adapter (implies --no-mmap)
  --lora-base FNAME     optional model to use as a base for the layers modified by the LoRA adapter
  -m FNAME, --model FNAME
                        model path (default: models/7B/ggml-model.bin)


##
> write an court appeal letter for ticket violation
Dear Sir/Madam,
I am writing this letter to contest the traffic citation that I received on [date of citation]. I believe that there has been a mistake and I would like the opportunity to present my case.
Firstly, I was not speeding at the time of the citation. I maintain that I was driving safely and within the limit. Furthermore, I have a clean driving record and this is my first offense. I am a responsible driver who takes safety seriously and I would like to keep my record clean.
I understand the importance of following traffic laws and respecting the safety of others on the road. However, in this case, I believe that there has been a mistake and I hope you will consider reviewing the evidence and dismissing the citation.
Thank you for your time and consideration.
Sincerely, [Your Name]


>translate pinecone in japanese
**pinecone** の日本語訳は「松綱」です。


> translate chatgpt in korean 
**chatGPT** 의 한국어 번역은 "챗굴"이라는 것으로 보입니다.


> is miniware ts-101 solder gun good? 
It is difficult to determine whether or not a specific product, such as the MiniWare Ts-101 Solder Gun, is "good" without more context. The quality and effectiveness of a tool like this will depend on various factors, including its intended use, the skill level of the user, and personal preferences. Some users may find it to be an excellent tool for their needs, while others might have negative experiences with it. It is recommended that you research multiple options and read reviews from other users before making a decision about which solder gun to purchase.


> write an python fastAPI web server which connects to openai model chatgpt-4
To create a Python FastAPI web server that connects to the OpenAI ChatGPT-4 model, you can use the `FastAPI` library and the `transformers` library. Here is an example code snippet to get started:
```python
from fastapi import FastAPI
import transformers

app = FastAPI()

# Load the pretrained ChatGPT-4 model from Hugging Face Transformers
model = transformers.AutoModel.from_pretrained('openai/chat-gpt4')

@app.post("/chat")
def chat(message: str):
    # Process the input message using the ChatGPT-4 model
    output = model.generate(inputs=message)
    
    return {"text": output}
```
This code creates a FastAPI app with a single endpoint `/chat` that accepts POST requests and processes them using the pretrained ChatGPT-4 model from Hugging Face Transformers. The `model.generate()` function takes an input message as text, feeds it into the model, and returns the generated response as JSON.


> i have a sequence of numbers 2,4,6,8,10, write next 5 numbers
The next five numbers in the sequence are 12, 14, 16, 18 and 20.


>

## compile and run a web api server 
cd llama.cpp
make server
./server -m models/ggml-vic13b-q4_0.bin -c 2048
...
{"timestamp":1687817876,"level":"INFO","function":"main","line":968,"message":"HTTP server listening","hostname":"127.0.0.1","port":8080}


# open another terminal, test local curl request 

curl --request POST \
>     --url http://localhost:8080/completion \
>     --data '{"prompt": "Building a website can be done in 10 simple steps:","n_predict": 128}'

# response 
{"content":"\n\nStep 1: Define the purpose of your website. What is its main goal? Who is your target audience? These questions will help guide the rest of the design and development process.\n\nStep 2: Choose a domain name for your website. This should be something easy to remember and relevant to your website's purpose.\n\nStep 3: Decide on a web hosting service. There are many options available, so do some research to find one that fits your needs and budget.\n\nStep 4: Choose a content management system (CMS) or website builder platform. This will make","generation_settings":{"frequency_penalty":0.0,"ignore_eos":false,"logit_bias":[],"mirostat":0,"mirostat_eta":0.10000000149011612,"mirostat_tau":5.0,"n_keep":0,"n_predict":128,"penalize_nl":true,"presence_penalty":0.0,"repeat_last_n":64,"repeat_penalty":1.100000023841858,"seed":-1,"stop":[],"stream":false,"temp":0.800000011920929,"tfs_z":1.0,"top_k":40,"top_p":0.949999988079071,"typical_p":1.0},"model":"models/ggml-vic13b-q4_0.bin","prompt":" Building a website can be done in 10 simple steps:","stop":true,"stopped_eos":false,"stopped_limit":true,"stopped_word":false,"stopping_word":"","tokens_predicted":128,"truncated":false}
