#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:34:42 2018

@author: mints
"""
from bs4 import BeautifulSoup
import sys
from glob import glob

index = ' '.join(open('index.html').readlines())
soup = BeautifulSoup(index, 'html.parser')
"""
    <!-- Image Section - set the background image for the header in the line below -->
    <section class="py-5 bg-image-full" >
      <!-- Put anything you want here! There is just a spacer below for demo purposes! -->
      <div style="height: 200px;"></div>
    </section>
"""
for file in sys.argv[1:]:
    tag_image = soup.new_tag('section')
    tag_image['class'] = "py-5 bg-image-full"
    tag_image['style'] = "background-image: url('images/sky-space-dark-galaxy.jpg');"
    div = soup.new_tag('div')
    div['style'] = "height: 200px;"
    tag_image.append(div)
    soup.footer.insert_before(tag_image)
    soup2 = BeautifulSoup(' '.join(open(file).readlines()), 'html.parser')
    section = soup.new_tag('section')
    section['class'] = 'py-5'
    tag = soup2.body
    tag.name = 'div'
    tag['class'] = 'container'
    section.append(tag)
    soup.footer.insert_before(section)
print(soup.prettify())