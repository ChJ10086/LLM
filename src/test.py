import tools

def chat(content):
    result = tools.request(content)
    # print(result)
    parse_res = tools.parse_response_contents(result)
    return '\n'.join(parse_res)

def main():
    question = input()
    print('\n================================answer================================\n')
    res = chat(question)
    print(res)

if __name__ == "__main__":
    main()