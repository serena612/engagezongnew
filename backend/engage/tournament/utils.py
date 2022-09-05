
def split_number_chunks(amount, chunk_size=10):
    remainder = amount % chunk_size
    value = amount - remainder
    parts = value // chunk_size
    chunks = [chunk_size] * parts
    if remainder >= 3:
        chunks.append(remainder)
    elif 0 < remainder < 3:
        last_chunk = chunks.pop()
        diff = 3 - remainder
        last_chunk -= diff
        chunks.append(last_chunk)
        chunks.append(remainder + diff)

    return chunks
