import copy

cur_map = []
stack = []
color_list = []
m = 0
n = 0


class Cell:
    def __init__(self,x,y,string):
        self.x = x
        self.y = y
        if (string[-1] !='#'):
            try:
                color = color_list.index(string[-1])
            except:
                print("wrong color try again")
                exit()
        else:
            color = string[-1]
        string = string[:-1]
        self.isComplete = False
        
        if string != '*':
            string = int(string)
        
        self.color = color
        self.number = string
        if self.color != '#' and self.number != '*':
            self.isComplete = True
        self.num_domain = [x for x in range(1,n+1)]
        self.color_domain = [x for x in range(m)]
        

    def __str__(self):
        return "[{}{}],{}{}".format(self.x,self.y ,self.number, self.color)
    
    def __repr__(self):  
        if self.color != '#':
            return "{}{}".format(self.number,color_list[self.color]) 
        else:
            return "{}#".format(self.number) 



def get_input():
    for i in input().rstrip().split(" "):
        color_list.append(i)
    color_list.reverse()
    for i in range(n):
        cur_map.append([])
    for i in range(n):
        col = 0
        for j in input().rstrip().split(" "):
            cur_map[i].append(Cell(i,col,j))
            col = col +1   


def set_cell_degree(cell):
    degree = 0
    if cell.number == "*":
        for i in range(n):
            if abs(i - cell.x) <2 :
                pass
            else:
                if cell.number == '*':
                     degree +=1
        for j in range(n):
            if abs(j - cell.y) < 2 :
                pass
            else:
                if cell.number == '*':
                     degree +=1
    if cell.color == "#":
        for i in range(-1,2):
            for j in range(-1,2):
                if 0 <(abs(i) + abs(j)) < 2 and -1 < (cell.x)+i < n  and -1< (cell.y)+j < n:
                    if cur_map[i+(cell.x)][j+(cell.y)].color == '#':
                        degree +=1
    return degree




def set_cell_num_constraint(cell):
    x = cell.x
    y = cell.y
    if cell.number != '*':
        for i in range(n):
            if i == x :
                continue
            try:
                cur_map[i][y].num_domain.remove(cell.number)
                if len(cur_map[i][y].num_domain) == 0 and cur_map[i][y].isComplete != True:
                    return false
            except:
                pass 
        for j in range(n):
            if j == y: 
                continue
            try:
                cur_map[x][j].num_domain.remove(cell.number)
                if len(cur_map[x][j].num_domain) == 0 and cur_map[x][j].isComplete != True:
                    return False
            except:
                pass 
    return True


def set_cell_color_constraint(cell):
    x = cell.x
    y = cell.y
    cell_color = cell.color
    cell_number = cell.number

    if cell_color != '#':
        for i in range(-1,2):
            for j in range(-1,2):
                if 0 <(abs(i) + abs(j)) < 2 and -1 < x+i < n  and -1< y+j < n:
                    try : 
                        target_cell = cur_map[i+x][j+y]
                        color_domain_list = target_cell.color_domain
                        if target_cell.number != '*':

                            if cell_number < target_cell.number:
                                for c in range(len(color_domain_list)):
                                    if color_domain_list[c] <= cell_color :
                                        color_domain_list[c] = -1 
                                target_cell.color_domain = [x for x in color_domain_list if x >= 0]

                            else :
                                for c in range(len(color_domain_list)):
                                    if color_domain_list[c] >= cell_color :
                                        color_domain_list[c] = -1
                                target_cell.color_domain = [x for x in color_domain_list if x >= 0]
                            
                        else:
                            if cell_color == 0 :
                                target_cell.num_domain = [ x for x in target_cell.num_domain if x> cell_number]
                            elif cell_color == len(color_list)-1:
                                target_cell.num_domain = [ x for x in target_cell.num_domain if x< cell_number]

                        if (len(cur_map[x+i][y+j].color_domain) == 0 ) and (cur_map[x+i][y+j].color == '#'):
                            return False
                        target_cell.color_domain.remove(cell_color)
                    except:
                        pass
    return True


def set_map_constraint():
    for i in range(n):
        for j in range(n):  
            consistancy = set_cell_num_constraint(cur_map[i][j])
            consistancy = set_cell_color_constraint(cur_map[i][j])
            
    return consistancy
                
            # print(cur_map[i][j].num_mrv)

def print_color_mrv():
    for i in range(n):
        for j in range(n):
            # print("*")
            # set_mrv(cur_map[i][j])
            print( cur_map[i][j].color_domain,end=",,,")
        print()


def print_num_mrv():
    for i in range(n):
        for j in range(n):
            # print("*")
            # set_mrv(cur_map[i][j])
            print( cur_map[i][j].num_domain,end=",,,")
        print()


def choose_cell():

    min_mrv_cell = Cell(-1,-1,"*#")
    min_mrv_cell.num_domain=[x for x in range(n+1)]
    min_mrv_cell.color_domain = [x for x in color_list]
    for i in range(n):
        for j in range(n):
            total_min_cell_mrv = len(min_mrv_cell.num_domain) + len(min_mrv_cell.color_domain)
            total_target_cell_mrv = len(cur_map[i][j].num_domain) + len(cur_map[i][j].color_domain)
            if cur_map[i][j].isComplete == False and total_target_cell_mrv <= total_min_cell_mrv:
                if total_min_cell_mrv == total_target_cell_mrv:
                    if set_cell_degree(min_mrv_cell) <= set_cell_degree(cur_map[i][j]):
                        min_mrv_cell =  cur_map[i][j]
                else :
                        min_mrv_cell =  cur_map[i][j]

    return min_mrv_cell 
# set_map_constraint()

def check_consistancy(cell):
    x = cell.x
    y = cell.y
    for i in range(-1,2):
        for j in range(-1,2):
            if 0 <(abs(i) + abs(j)) < 2 and -1 < x+i < n  and -1< y+j < n :
                targt_cell = cur_map[x+i][y+j]
                if targt_cell.color != '#' and targt_cell.number !='*' :
                    if (targt_cell.number < cell.number and targt_cell.color > cell.color) or (targt_cell.number > cell.number and targt_cell.color < cell.color):
                        return False
    return True


def assign_value(cell):
    if len(cell.num_domain) <1:
        return False
    cell.number = cell.num_domain[0]
    cell.num_domain.pop(0)
    cell.isComplete = True



def forward_checking(cell):
    x = set_cell_num_constraint(cell)
    x = set_cell_color_constraint(cell)
    if x == False:
        return "failure "
    
    

m, n = map(int,input("enter m, n in order: \n").split(" "))    

get_input() 

map_isConsistance = set_map_constraint()

if map_isConsistance == False :
    print("your starting map is inconsistance and there is no solution")
    exit()


print_num_mrv()
print("".center(40,"*"))
print_color_mrv()    

print("map for first time: \n")
for i in range(n):
    print(cur_map[i])
print("*********")


has_answer = False
stack.append(cur_map)

while  len(stack)>0:
    # print_num_mrv()
    # print("".center(20,"*"))
    # print_color_mrv()
    chosen_cell = choose_cell()
    if (chosen_cell.x == -1 or chosen_cell.y == -1):
        has_answer = True
        break
    
    if chosen_cell.number == '*':
        if len(chosen_cell.num_domain) == 0:
            t = "failure "
        else:
            x = chosen_cell.num_domain.pop(0)
            bp_map = copy.deepcopy(cur_map)
            stack.append(bp_map)
            chosen_cell.number = x
            if chosen_cell.color != '#':
                chosen_cell.isComplete = True
            t = forward_checking(chosen_cell)
    else:
        if len(chosen_cell.color_domain) ==  0:
            t = "failure "
        else:
            x = chosen_cell.color_domain.pop(0)
            bp_map = copy.deepcopy(cur_map)
            stack.append(bp_map)
            chosen_cell.color = x
            if chosen_cell.number != '*':
                chosen_cell.isComplete = True
            consistance = check_consistancy(chosen_cell)
            if consistance == False:
                # print("back track comand".center(40,"*"))
                t = 'failure '
            else:
                t = forward_checking(chosen_cell)

    if t != "failure ":
        pass

    else:
        # print("******************************back Track")
        cur_map = stack.pop()
       




if has_answer  :
    print("color priority: ", end=" ")
    for color in range(len(color_list)):
        print(color_list[color],end="")
        if color == len(color_list)-1:
            break
        print(" < ",end=" ")
    print("\nresult : \n")
    for i in range(n):
        print(cur_map[i])
    print("*********")
else :
    print("NO solution ")