OpenCV�Ń{�[���̈ʒu�����o���A���{�b�g�ւ̖��߂����肷��v���O�������쐬����
�v���O�������Fcircle.py

���z�I�ɂ̓J�����摜����͂Ƃ��邪�A����̓J�����摜�������Ă��摜����͂��āA
�v���O�����̓���m�F�����Ă���

����m�F�̌��ʂ��u����m�F�v�t�H���_�Ɋi�[���Ă���
�ڍׂ́A�u����m�F/����m�F����.xlsx�v���Q��

�ȉ��́Alinux�}�V����OpenCV(physon�p)���C���X�g�[��������@���L�ڂ���
���݂ɕM�҂�CentOS�ɃC���X�g�[������

�P�Dphyson-devel�C���X�g�[��
�ȉ��̃R�}���h��������
----------------------------
yum install python-devel
----------------------------

�Q�DNumpy�C���X�g�[��(python�pOpenCV���g�p���邽�߃C���X�g�[���K�{)
�ȉ��̃R�}���h��������
----------------------------
wget http://sourceforge.net/projects/numpy/files/NumPy/1.X.X/numpy-1.X.X.tar.gz/
tar xzvf numpy-1.X.X.tar.gz
cd numpy-1.X.X
python setup.py build �iphyson-devel���C���X�g�[�����ĂȂ��ƃG���[�j
sudo python setup.py install
----------------------------

�R�DPython�AOpenCV�C���X�g�[��
�ȉ��̃R�}���h��������(Python�̓C���X�g�[������Ȃ���������Ȃ��E�E)
-----------------------------
yum install opencv-python
-----------------------------

�����APython���C���X�g�[������Ȃ�������A�ȉ��̃R�}���h��������
-----------------------------
wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
gzip -dc Python-3.5.2 | tar xvf -
cd Python-3.5.2
./configure --with-threads --enable-shared --prefix=/usr/local
make
sudo make install
-----------------------------
