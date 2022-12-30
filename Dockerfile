
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-buster

# bin/bashでこれ以降のコマンドを実行する。RESEARCH: bin/shではpoetry installコマンドがnot foundになってしまうため。
# かつ--no-rootを付けないと次のエラーに当たる：https://github.com/python-poetry/poetry/issues/1227
SHELL ["/bin/bash", "-c"]

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# working_dirをどこにするか決定。ドットを指定するとトップディレクトリ（usrやbinやetcがあるとこ）になる。
# testを指定するとトップディレクトリにtestフォルダが作成されて、その中でこれ以降のコマンドが実行される。
ENV APP_HOME line_msg_proc
WORKDIR $APP_HOME
# COPY [localコピー元] [container コピー先]
COPY . ./

# poetryインストール
RUN curl -sSL https://install.python-poetry.org | python3 -

# poetryへのパスを通す
ENV PATH="$PATH:~/.local/bin"
# TODO: AWSへのクレデンシャルをどうやって渡すか

# poetryでパッケージインストール
# 誰かが最初にpoetry init&&addをしてpyproject.tomlとpoetry.lockが作成されている前提
# 新しいパッケージを追加する場合、プルリクをする人がローカルの環境でpoetry addをして動くかどうか確認して、動いたらpoetry.lockも更新してpushしてもらう
RUN poetry install --no-root

# For development case
# RUN apt-get update
# RUN apt-get install vim

# $HOSTは指定しなければ0.0.0.0（localhost）で起動する
CMD poetry run gunicorn --bind $HOST:$PORT --workers 1 --threads 8 --timeout 30 app:app