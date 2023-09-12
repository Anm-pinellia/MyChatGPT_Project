import openai

class Chat:
    def __init__(self) -> None:
        # 初始化对话列表，可以加入一个key为system的字典，有助于形成更加个性化的回答
        # self.conversation_list = [{'role':'system','content':'你是一个非常友善的助手'}]
        self.conversation_list = []

    # 打印对话
    def show_conversation(self, msg_list):
        for msg in msg_list:
            if msg['role'] == 'user':
                print(f"我:\t{msg['content']}\n")
            else:
                print(f"ChatGPT:\t{msg['content']}\n")

    # 打印最新对话
    def show_latestconversation(self, msg_list):
        msg = msg_list[-1]
        print(f"ChatGPT: {msg['content'].strip()}")

    # 提示chatgpt
    def ask(self, prompt):
        self.conversation_list.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.conversation_list)
        answer = response.choices[0].message['content']
        # 下面这一步是把chatGPT的回答也添加到对话列表中，这样下一次问问题的时候就能形成上下文了
        self.conversation_list.append({"role": "assistant", "content": answer})
        self.show_latestconversation(self.conversation_list)
        # self.show_conversation(self.conversation_list)

def chat_loop(organization, apikey):
    openai.organization = organization
    openai.api_key = apikey
    chat_robot = Chat()
    while True:
        question = input(f'我: ')
        chat_robot.ask(question)

def colorstr(*input):
    # Colors a string https://en.wikipedia.org/wiki/ANSI_escape_code, i.e.  colorstr('blue', 'hello world')
    *args, string = input if len(input) > 1 else ('blue', 'bold', input[0])  # color arguments, string
    colors = {'black': '\033[30m',  # basic colors
              'red': '\033[31m',
              'green': '\033[32m',
              'yellow': '\033[33m',
              'blue': '\033[34m',
              'magenta': '\033[35m',
              'cyan': '\033[36m',
              'white': '\033[37m',
              'bright_black': '\033[90m',  # bright colors
              'bright_red': '\033[91m',
              'bright_green': '\033[92m',
              'bright_yellow': '\033[93m',
              'bright_blue': '\033[94m',
              'bright_magenta': '\033[95m',
              'bright_cyan': '\033[96m',
              'bright_white': '\033[97m',
              'end': '\033[0m',  # misc
              'bold': '\033[1m',
              'underline': '\033[4m'}
    return ''.join(colors[x] for x in args) + f'{string}' + colors['end']


if __name__ == '__main__':
    organization = "org-iGW7KAYcBIQALDzwvCjhqOVy"
    api_key = "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"
    chat_loop(organization, api_key)