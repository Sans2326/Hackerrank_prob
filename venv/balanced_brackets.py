s=input()
def balance(st):
    print('[]'*st.count('['))
    print(')('*st.count('('))
    print('{'+str(st.count('{')))
def unbalance(st):
    print('['+str(st.count('[')))
    print(']'+str(st.count(']')))
    print('('+str(st.count('(')))
    print(')'+str(st.count(')')))
    print('{'+str(st.count('{')))
    print('}'+str(st.count('}')))
def check_balance(st):
    if((st.count('[')==st.count(']')) and (st.count('{')==st.count('}'))
       and (st.count('(')==st.count(')'))):
       # print("Balanced")
       balance(st)
    else:
       # print("Not Balanced")
       unbalance(st)
check_balance(s)


#input -[]{)}
#output -[1
#]1
#(0
#)1
#{1
#}1
#input2 -{[{}][()()]}
#[][]
#)()(
#{2

