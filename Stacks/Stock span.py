class StockSpanner(object):

    def __init__(self):
        self.st=[]
    #[[],[28],[14],[28],[35],[46],[53],[66],[80],[87],[88]]
    #[[], [100], [80], [60], [70], [60], [75], [85]]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span=1
        while(self.st and self.st[-1][0]<=price):
            span+=self.st.pop()[1]
        
        self.st.append((price,span))  
        return span  
