SHELL=/bin/bash
INSTALL_DIR = ~/bin
WRAPPERFILE = ${INSTALL_DIR}/find-dead-links
PYTHONFILE = ${INSTALL_DIR}/find-dead-links.py
ENV = ${INSTALL_DIR}/ENV

install: ${WRAPPERFILE} ${PYTHONFILE} ${ENV}

${WRAPPERFILE}: find-dead-links
	cp find-dead-links ${INSTALL_DIR}
	chmod 700 ${INSTALL_DIR}/find-dead-links

${PYTHONFILE}: find-dead-links.py
	cp find-dead-links.py ${INSTALL_DIR}
	chmod 700 ${INSTALL_DIR}/find-dead-links.py

${ENV}:
	virtualenv -p python3 ${ENV}
	source ${ENV}/bin/activate && pip install requests && pip install beautifulsoup4

