#!/usr/bin/env python3

#fasta file로부터 염기와 유전자 이름을 추출해서 dictionary에 저장 
def fasta_handler(fpath):
  seqdic = {}
  name, seq = '', ''
  for line in open(fpath):
    if line[0] == '>':
      if len(seq) > 0:
        seqdic[name] = seq
        seq = ''
      name = line[1:].rstrip()
    else:
      seq = line.rstrip()

  seqdic[name] = seq

  return seqdic

#plasmid seq, sequenced list를 받아 align한 후 dictionary에 저장
def seq_aligner(seq1, seq2, align_num):
  _long, _short = "", ""
  if seq1 >= seq2: _long, _short = seq1, seq2
  if seq1 < seq2: _long, _short = seq2, seq1
  aligned_dic = {i:[_long[i], "-" for i in range[_long]]}

  matched_index = []
  for i in range(_long):
    align_key = _long[i:int(align_num)+i]
    if align_key in _short:
      matched_index.append({ "sequence1" :i, "sequence2" :_short.index(align_key)})
  
  primary_match_bp_long = matched_index[0]["sequence1"]
  primary_match_bp_short = matched_index[0]["sequence2"]
  match_short_start = primary_match_bp_long - primary_match_bp_short
  for i in range(_short):
    if int(list(aligned_dic.keys())[-1]) <= match_short_start+i:
      aligned_dic[match_short_start+i][-1] = _short[i]
    if int(list(aligned_dic.keys())[-1]) > match_short_start+i:
      aligned_dic[match_short_start+i] = ["-", _short[i]]
  return aligned_dic

def seq_printer(aligned_dic, resultpath):
  file = open(resultpath, "a")
  format = int(str(len(aligned_dic)))
  for key, value in aligned_dic.items():
    index = "%*d" %(format, key)
    file.write(index+" ")
  file.write('\n')
  for key, value in aligned_dic.items():
    file.write(" "*format + value[0])
  for key, value in aligned_dic.items():
    file.write(" "*format + value[-1])
  for key, value in aligned_dic.items():
    match = ""
    if value[0] == value[-1]: match = "*"
    file.write(" "*format + match)

  file.close( )
        
  