OpenCVでボールの位置を検出し、ロボットへの命令を決定するプログラムを作成した
プログラム名：circle.py

理想的にはカメラ画像を入力とするが、現状はカメラ画像を見立てた画像を入力して、
プログラムの動作確認をしている

動作確認の結果を「動作確認」フォルダに格納してある
詳細は、「動作確認/動作確認結果.xlsx」を参照

以下は、linuxマシンにOpenCV(physon用)をインストールする方法を記載する
因みに筆者はCentOSにインストールした

１．physon-develインストール
以下のコマンドをたたく
----------------------------
yum install python-devel
----------------------------

２．Numpyインストール(python用OpenCVが使用するためインストール必須)
以下のコマンドをたたく
----------------------------
wget http://sourceforge.net/projects/numpy/files/NumPy/1.X.X/numpy-1.X.X.tar.gz/
tar xzvf numpy-1.X.X.tar.gz
cd numpy-1.X.X
python setup.py build （physon-develをインストールしてないとエラー）
sudo python setup.py install
----------------------------

３．Python、OpenCVインストール
以下のコマンドをたたく(Pythonはインストールされないかもしれない・・)
-----------------------------
yum install opencv-python
-----------------------------

もし、Pythonがインストールされなかったら、以下のコマンドをたたく
-----------------------------
wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
gzip -dc Python-3.5.2 | tar xvf -
cd Python-3.5.2
./configure --with-threads --enable-shared --prefix=/usr/local
make
sudo make install
-----------------------------
