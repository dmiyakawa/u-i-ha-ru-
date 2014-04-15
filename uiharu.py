#!/usr/bin/python
from __future__ import print_function

import Image
import sys

HEADER = '''\
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:paddingBottom="@dimen/activity_vertical_margin"
    android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"
    tools:context="jp.ascii.training2014.MainActivity$PlaceholderFragment" >
'''

FOOTER = '''\
</LinearLayout>
'''

Y_HEADER = '''\
    <LinearLayout
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" >
'''

Y_FOOTER = '''\
    </LinearLayout>
'''

BUTTON = '''\
        <Button
            android:id="@+id/button{}"
            android:background="#{:x}{:x}{:x}{:x}"
            android:layout_width="8px"
            android:layout_height="8px"
            android:minHeight="8px"
            android:minWidth="8px" />
'''

img = Image.open('uiharu_yodare_40x40.png')
(width, height) = img.size
print(HEADER)
for y in xrange(0, height):
    print(Y_HEADER)
    for x in xrange(0, width):
        button_id = y * width + x
        (r, g, b, a) = img.getpixel((x, y))
        #print(x, y, button_id)
        print(BUTTON.format(button_id, a, r, g, b))
    print(Y_FOOTER)
print(FOOTER)
