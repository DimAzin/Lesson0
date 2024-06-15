
from pprint import pprint
file_name = 'test.txt'


file_content = (b'# -*- coding: utf-8 -*-\r\n'
                b'My soul is dark - Oh! quickly string\r\n'
                b'The harp I yet can brook to hear;\r\n'
                b'And let thy gentle fingers fling\r\n'
                b"Its melting murmurs o'er mine ear.\r\n"
                b'If in this heart a hope be dear,\r\n'
                b'That sound shall charm it forth again:\r\n'
                b'If in these eyes there lurk a tear,\r\n'
                b"'Twill flow, and cease to burn my brain.\r\n"
                b'\r\n'
                b'But bid the strain be wild and deep,\r\n'
                b'Nor let thy notes of joy be first:\r\n'
                b'I tell thee, minstrel, I must weep,\r\n'
                b'Or else this heavy heart will burst;\r\n'
                b'For it hath been by sorrow nursed,\r\n'
                b'And ached in sleepless silence, long;\r\n'
                b"And now 'tis doomed to know the worst,\r\n"
                b'And break at once - or yield to song.\r\n')

file = open(file_name, mode='wb')
file.write(file_content)
file.close()

file = open(file_name, mode='rb')
file_content = file.read()
file.close()
pprint(file_content)

