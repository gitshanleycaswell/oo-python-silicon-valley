from .funding_round import FundingRound

class VentureCapitalist:
    all = []
    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

    @classmethod
    def tres_commas_club(cls):
        da_club = []
        for vc in VentureCapitalist.all:
            if vc.total_worth >= 1000000000:
                da_club.append(vc)
        return da_club
    
    def offer_contract(self, new_startup, new_type, new_investment):
        FundingRound(new_startup, self, new_type, new_investment) 

    @property
    def funding_rounds(self):
        vc_funding_rounds = []
        for round in FundingRound.all:
            if round.venture_capitalist == self:
                vc_funding_rounds.append(round)
        return vc_funding_rounds
    
    @property
    def portfolio(self):
        vc_startups = []
        for round in self.funding_rounds:
            vc_startups.append(round.startup)
        unique = set(vc_startups)
        return list(unique)
    
    def biggest_investment(self):
        investments ={}
        for round in self.funding_rounds:
            key = round.startup
            value = round.investment
            investments[key] = investments.get(key, value)

        top_investment = max(investments, key=investments.get)
        return top_investment
    
    def invested(self, domain_string):
        investments = []
        for round in self.funding_rounds:
            if round.startup.domain == domain_string:
                investments.append(round.investment)
            
        return sum(investments)
