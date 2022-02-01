import time

from googletrans import Translator

translator = Translator(service_urls=[
    'translate.google.cn',
])

langs = ['en', 'fr', 'sv', 'el', 'zu', 'en']


def get_translation(input: str) -> str:
    for lang in langs:
        print(input)
        input = translator.translate(input, dest=lang).text
    return translator.translate(input, dest='zh-CN').text


if __name__ == '__main__':
    nowTime = time.time()
    print(get_translation('哈哈哈哈鸡汤来咯，喝啊怎么不喝'))
    print(time.time() - nowTime)
