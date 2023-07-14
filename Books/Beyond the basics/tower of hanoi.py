class Tower():
    def __init__(self):
        self.state = [[1,2,3,4,5,6],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.history =[[self.find_highest_block(c)[0] for c in range(3)]]

    def show_state(self):
        for line in range(6):
            for col in range(3):
                print(self.state[col][line],end = '   ')
            print()
        print('-'*10)

    def find_highest_block(self,col):
        for i in range(6):
            val = self.state[col][i]
            if val:
                return val,i
        else:
            return 0,6

    def move_block(self,source,destination):
        source_val,source_line = self.find_highest_block(source)
        dest_val,dest_line = self.find_highest_block(destination)
        self.state[source][source_line] = 0
        self.state[destination][dest_line-1] = source_val

    def check_move(self,source,destination):
        source_val,source_line = self.find_highest_block(source)
        dest_val,dest_line = self.find_highest_block(destination)
        if dest_line < 0:
            # print('not enough space')
            return False
        if source_val > dest_val and dest_val != 0:
            # print('can\'t place large on small')
            return False
        return True
        
    def try_move(self,source,destination):
        if self.check_move(source,destination):
            self.move_block(source,destination)
            return True
        return False
    
    def preview_move(self,source,destination):
        self.move_block(source,destination)
        preview_highest_blocks = [self.find_highest_block(c)[0] for c in range(3)]
        self.move_block(destination,source)
        return preview_highest_blocks

    def find_all_valid_moves(self):
        highest = [self.find_highest_block(c)+(c,) for c in range(3)]
        valid_sources = [c[2] for c in highest if c[0] != 0]
        valid_destinations = [c[2] for c in highest if c[1] != 0]
        valid_moves = []
        for s in valid_sources:
            for d in valid_destinations:
                if s == d : continue
                if not self.check_move(s,d) : continue
                preview = self.preview_move(s,d)
                if preview in self.history : continue
                valid_moves.append([s,d])
        return valid_moves

    def do_first_valid_move(self):
        moves =  self.find_all_valid_moves()
        if moves:
            self.move_block(*moves[0])
            self.history.append([self.find_highest_block(c)[0] for c in range(3)])
        else:
            print('no valid moves',end =', ')

tower = Tower()
tower.show_state()

for x in range(20):
    tower.do_first_valid_move()
    # print(tower.find_highest_block(1))
    # tower.try_move(0,1)
print()
tower.show_state()
