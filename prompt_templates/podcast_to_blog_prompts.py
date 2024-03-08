"""
This module provides template prompts used in the 'Podcast to Blog Post' project for generating
structured blog post outlines from podcast transcripts. These prompts are designed to guide the
LLM (Language Learning Model) in producing content that's well-suited for blog publication,
including an introduction, body paragraphs, and a conclusion, while excluding non-essential
elements.
"""
PROMPT_1 = """You are an expert in summarization. Your task is to turn a podcast
transcript onto a blog post outline. Make sure the outline is composed of an 
introduction, 3 body paragraphs and, a conclusion. Omit any filler words, false starts, or
non-essential audio elements. The transcription should read smoothly for blog
publication, maintaining the essence and insights of the podcast. Exclude timestamps
and speaker labels unless they are crucial for understanding the content.
Transcript: {transcript}"""
