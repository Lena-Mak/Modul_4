#def strcounter(s): #aab  O(N*M) => O(N*N) => O(N^2)
  #  for sym in set(s): # ab перебирает множества символов строки М(уник)
 #       counter = 0
#        for sub_sym in s: # aab N(все)
          #  if sym==sub_sym:
         #       counter+=1
      #  print(sym, counter)

#strcounter('abcdaaadc')


def strcounter(s): #aab  O(N + M) => O(N+N) => O(2N) => o(N)
    syms_counter = {}
    for sym in s: # ab перебирает множества символов строки М(уник)
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items(): #благодаря items: a 1  b 1 ...
        print(sym, count)
strcounter('aadc')









