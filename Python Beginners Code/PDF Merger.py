#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PyPDF2 import PdfMerger
pdfs=["1.pdf","2.pdf","3.pdf"]
merger=PdfMerger()

for pdf in pdfs:
    merger.append(pdf)
    
merger.write("merged.pdf")
merger.close()

