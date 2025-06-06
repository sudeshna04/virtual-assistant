import re

#play_____on Youtube
def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None

# on youtube
def stTerm(command):
    stream=r'(.*?)\s+on\s+youtube'
    match=re.search(stream,command,re.IGNORECASE)
    return match.group(1) if match else None


# whatsapp helper
def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string



#chatBot helper 1:
def format_response(message):
    # Convert markdown bold **text** to <strong>text</strong>
    message = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', message)

    # Convert markdown bullets (*) to real bullets with spacing
    message = re.sub(r'\*\s*', '<br>• ', message)

    # Add spacing after periods (for readability)
    message = message.replace(". ", ".<br><br>")

    # Replace any remaining \n with <br> (just in case)
    message = message.replace("\n", "<br><br>")

    return message


#chatBot helper 2:
def split_text_by_sentences(text, max_len=300):
    # Split by sentence boundaries
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    chunks = []
    current = ""

    for sentence in sentences:
        if len(current) + len(sentence) < max_len:
            current += sentence + " "
        else:
            chunks.append(current.strip())
            current = sentence + " "
    if current:
        chunks.append(current.strip())

    return chunks





