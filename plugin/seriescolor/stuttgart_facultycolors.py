# -*- coding: utf-8 -*-
'''
	LF-Portal
	~~~~~~~~~

	Defined colors for some facilities
	
	:license: GPL, see LICENSE for more details.
'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def seriescolor(id, contributor, config):
	
	if 'Architektur' in contributor: return '0000cc'
	if 'Stadtplanung' in contributor: return '0000cc'
	if 'Umweltwissenschaften' in contributor: return '0099ff'
	if 'Bauwissenschaften' in contributor: return '0099ff'
	if 'Chemie' in contributor: return '33ccff'
	if 'Biotechnik' in contributor: return '009999'
	if 'Energietechnik' in contributor: return '009999'
	if 'Verfahrenstechnik' in contributor: return '009999'
	if 'Elektrotechnik' in contributor: return '3399ff'
	if 'Informationstechnik' in contributor: return '3399ff'
	if 'Informatik' in contributor: return '3399ff'
	if 'Geodäsie' in contributor: return '006699'
	if 'Luft- und Raumfahrttechnik' in contributor: return '006699'
	if 'Konstruktionstechnik' in contributor: return '0066cc'
	if 'Produktionstechnik' in contributor: return '0066cc'
	if 'Fahrzeugtechnik' in contributor: return '0066cc'
	if 'Mathematik' in contributor: return '0066ff'
	if 'Physik' in contributor: return '0066ff'
	if 'Philosophisch-Historische Fakultät' in contributor: return '003399'
	if 'Wirtschaftswissenschaften' in contributor: return '33cccc'
	if 'Sozialwissenschaften' in contributor: return '33cccc'

	return '333333'
