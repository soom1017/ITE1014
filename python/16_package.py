#패키지: 파이썬 모듈을 계층적으로 관리하기 위해 사용
# import sys
# sys.path.append('C:/Users/min00/python/game')
# print(sys.path)

from game.sound import * # import game.sound는 되지만 import game은 안됨.
echo.echo_test()         # import game: game 디렉터리의 모듈만 참조

from game.graphic import render
render.render_test()
