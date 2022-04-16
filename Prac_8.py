class LIFO:
       def __init__(self, value):
              self.data = value   
        self.next = None 
        self.len = 0        
  
    def isEmpty(self):
        return self.len == 0

   
    def top(self):
              if self.isEmpty():  
            raise Exception('Stack is Empty! :(')
        return self.next.data

      def push(self, newData):
        newNode = LIFO(newData)    
        newNode.next = self.next    
        self.next = newNode
        self.len += 1
    
    
    def pop(self):
        
        if self.isEmpty():
            raise Exception('Stack is Empty! :(')
        
        pop = self.next

        
        self.next = self.next.next
       
        self.len -= 1
        return pop.data

        def __str__(self):
        show = ''
        peek = self.next
        while peek:     
            show += str(peek.data) + ' | '
            peek = peek.next
        return show[::-1]
    
if __name__ == "__main__":
    print('\t#STACK')
    stack = LIFO('head')
    def consoleOut():
        if f'{stack}' == '':
            print('\tStack is Empty!,\n\tTry to push element.\n')
        else:
            print(f'\tStack:{stack}')
    x = 5
    while x != 0:
        x = int(input('1) Print Stack\n2) Push Element\n3) Pop Element\n4) Print Peek\n0) Exit\t:'))
        
        if x == 1:
            consoleOut()

        if x == 2:
            ele = input('\tEnter element: ')
            stack.push(ele)
            print('\tPushed:',ele)
            
        if x == 3:
            ele = int(input('\tEnter Pop index: '))
            while ele != 0:
                print('\tPopped:',stack.pop())
                ele -= 1

        if x == 4:
            print('\tPeek:',stack.top())
