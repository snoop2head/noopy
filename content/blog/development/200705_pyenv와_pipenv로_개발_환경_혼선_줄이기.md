---
title: 'conda는 이제 그만 쓸래요 - pyenv & poetry'
date: 2020-07-12 13:01:13
category: 'development'
draft: false


---

## 개발환경

* OS: Mac OS Catalina 10.15.5
* Terminal: iTerm2 & Oh my zsh & Power10k

## conda는 이제 그만 쓸래요 

* conda는 절대 네버 쓰지 말자. package 하나 다운로드 받는 것도 힘든데 굳이 쓸 필요가 없다. 안 그러면 썸네일의 저 꼬여버린 개발 환경이 될 수도 있다...

* 나는 웹개발과 데이터분석에 모두 관심이 있다. 웹개발에 필요한 library, 데이터 분석에 필요한 library를 모두 다운받았다. 그러다보니, 다음과 같이 팩키지 관리가 엉망진창이다.

![image-20200705141721211](https://bucket-for-blog.s3.ap-northeast-2.amazonaws.com/markdown_files/img/image-20200705141721211.png)

따라서 이 두 가지 문제점을 모두 해결하고 싶었다.

## pyenv & poetry 사용 목적

나는 pyenv와 poetry를 사용한 목적은 세 가지였다.

1) Web 개발용 python과 Data analysis용 python을 분리시키고 싶었다.
2) Jupyter notebook 실행할 때 conda 4.8 이상 package manager로 설치하면 에러 대환장파티가 났다.
3) pypy interpreter가 C Python interpreter보다 적어도 [5배는 더 빠르다는데](https://speed.pypy.org/), 테스트해보고 싶었다.

사실 데이터분석은 Google Colab으로 하는 게 편하다. 하지만 무거운 작업들은 로컬 컴퓨터로 돌리는 게 더 빠르다. 따라서 jupyter notebook을 사용하는 가상환경과 web 개발을 하는 가상환경을 분리할 필요성을 느꼈다.

![image-20200705131527160](https://bucket-for-blog.s3.ap-northeast-2.amazonaws.com/markdown_files/img/image-20200705131527160.png)

* pyenv는 python version manager이다. node.js에서 따지면 nvm이라고 할 수 있겠다. 
* poetry는 각 프로젝트의 package version들을 명시하고, dependency들을 관리한다. node.js에서 따지면 npm이라고 할 수 있겠다. 

### Reference

* [pyenv docs](https://github.com/pyenv/pyenv) && [pyenv virtualenv docs](https://github.com/pyenv/pyenv-virtualenv)

* [개발도상국 빵형님의 bash 셋팅 방법: vim 사용 방법 부분은 건너 뛰어도 됨](https://www.youtube.com/watch?v=y7gtdZQJk3s)

* [zsh shelll 유저들의 pyenv 셋팅 방법](https://jyhwng.github.io/dev-env-setup)

* [powerlevel10k virtual environment name 두 번 표시되는 것 해결](https://github.com/romkatv/powerlevel10k/issues/730)

## Step-by-step Configuration

일단 pyenv와 pyenv-virtualenv를 다운로드받는다

```shell
# pyenv, pyenv-virtualenv download
brew install pyenv
brew install pyenv-virtualenv
```

.zshrc 파일에 설정을 추가한다

```bash
# ~/.zshrc

# pyenv command
eval "$(pyenv init -)"

# pyenv-virtualenv command
eval "$(pyenv virtualenv-init -)"
```

그러면 어떤 파이선을 다운로드할 수 있는지 확인하고, 다운로드 받는다. 필자는 세 가지를 다운로드 받았다: `3.8.3`, `3.7.7`, `pypy3.6-7.3.1`

```shell
#check available python version list to download
pyenv install --list
# install selected python version to the local
pyenv install PYTHON-VERSION
```

웹개발용 가상환경, 데이터 분석용 가상환경, pypy 실험용 가상환경 세 가지를 만들어본다

```shell
#create virtual environment
pyenv virtualenv PYTHON-VERSION ENVIRONMENT-NAME
#check available virtual environments in local
pyenv virtualenvs
# DELETING VIRTUAL ENVIRONMENT
pyenv uninstall ENVIRONMENT-NAME
```

이 때 power10k를 업데이트 해줘야 virtual environment가 중복 표시 안 된다.

```shell
git -C ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/ themes/powerlevel10k pull
```

해당 설정 부분을 .p10k.zsh 파일에 추가한다.

```shell
# ~/.p10k.zsh
typeset -g POWERLEVEL9K_VIRTUALENV_SHOW_WITH_PYENV=false
typeset -g POWERLEVEL9K_PYENV_CONTENT_EXPANSION='${P9K_CONTENT}${${P9K_PYENV_PYTHON_VERSION:#$P9K_CONTENT}:+ $P9K_PYENV_PYTHON_VERSION}'
```

가상환경을 실행시켜본다

```shell
#activate virtual environment
pyenv activate ENVIRONMENT-NAME
#check available packages
pip list
#upgrade pip
pip install --upgrade pip
#GET OUT OF VIRTUAL ENVIRONMENT
pyenv deactivate
```

그러면 다음과 같이 표시된다. 

![image-20200705141052057](https://bucket-for-blog.s3.ap-northeast-2.amazonaws.com/markdown_files/img/image-20200705141052057.png)

![image-20200705141158107](https://bucket-for-blog.s3.ap-northeast-2.amazonaws.com/markdown_files/img/image-20200705141158107.png)

특정 repository에 들어가면 virtual environment가 자동으로 실행되게 만들고 싶으면 다음과 같이 실행하면 된다.
```shell
pyenv local ENVIRONMENT-NAME
```
![](https://images.velog.io/images/snoop2head/post/1d9b71c9-7137-4e88-8c14-a5ea69c51758/image.png)
몇몇은 autoenv를 사용하기도 하는데, [현재 catalina OS에서 autoenv로 가상환경을 실행시킬 때 무한 반복 에러가 발생한다.](https://github.com/inishchith/autoenv/issues/188) 따라서 pyenv local 명령어로 특정 repository에 가상환경을 부여해주는 게 더 낫다.

## poetry vs pipenv

!youtube[1GIIaGbL9qQ?t=422]

위의 강연을 요약해보자면...

일단, pipenv는 느리다. pipenv를 사용해본 분들은 아마 이런 경험을 해보셨을 거다. 팩키지 10개를 다운로드받으면, 그 중 몇 개는 반드시 fail한다.

![Pipenv fails to install latest version of pyarrow on linux · Issue ...](https://user-images.githubusercontent.com/9082460/38740664-84971498-3f0e-11e8-8b4d-fee09c6051da.png)

무엇보다 maintainer가 성실해보이지는 않는다. 위의 강연이 poetry와 pipenv를 잘 비교했는데, 강연자가 상사하게 문의한 issue에 그저 "no"라는 답변을 달았다고 한다...

![image-20200705140545984](https://bucket-for-blog.s3.ap-northeast-2.amazonaws.com/markdown_files/img/image-20200705140545984.png)

그래서 poetry로 갈아탔다. Virtual environment 속에서 다음과 같이 실행했다.

* python 3.7를 쓴 virtual environment `data`는 데이터 분석용이기 때문에, 해당 커멘드를 추가로 실행했다. 
  * `pip install jupyter notebook`
  * `pip install poetry`
* python 3.8를 쓰는 virtual environment `web`은 웹개발용이기 때문에, poetry만 받았다.
  * `pip install poetry`

project repository로 가서 poetry를 다음과 같이 사용하면 된다

![image-20200705141533771](https://bucket-for-blog.s3.ap-northeast-2.amazonaws.com/markdown_files/img/image-20200705141533771.png)

![image-20200705141607811](https://bucket-for-blog.s3.ap-northeast-2.amazonaws.com/markdown_files/img/image-20200705141607811.png)

> 이쯤 되면 rust의 cargo가 얼마나 대단한 지 알 수 있다. 
> 후... 그래도 conda 없이 jupyter notebook을 사용할 수 있다는 점에서는 만족한다.