


class FundingRound:
    all = []
    def __init__(self, startup, venture_capitalist, type, investment):
        self.startup = startup
        self.venture_capitalist = venture_capitalist
        self.type = type
        self.investment = investment
        FundingRound.all.append(self)

    @property
    def startup(self):
        return self._startup
    
    @startup.setter
    def startup(self, new_startup):
        if hasattr(self, "_startup"):
            raise Exception("Once a funding round is created, you cannot change startup")
        else:
            self._startup = new_startup

    @property
    def startup(self):
        return self._startup
    
    @startup.setter
    def startup(self, new_startup):
        from .startup import Startup
        if isinstance(new_startup, Startup):
            self._startup = new_startup
        else:
            raise Exception("instance must be of type Startup!")
        
    @property
    def venture_capitalist(self):
        return self._venture_capitalist
    
    @venture_capitalist.setter
    def venture_capitalist(self, new_venture_capitalist):
        from .venture_capitalist import VentureCapitalist
        if isinstance(new_venture_capitalist, VentureCapitalist):
            self._venture_capitalist = new_venture_capitalist
        else:
            raise Exception("instance must be of type venture_capitalist_venture_capitalist!")


