from .funding_round import FundingRound

class Startup:
   all = []
   def __init__(self, name, founder, domain):
      self.name = name
      self.founder = founder
      self.domain = domain
      Startup.all.append(self)

   @property
   def founder(self):
      return self._founder

   @founder.setter
   def founder(self, new_founder):
      if hasattr(self, "_founder"):
         raise Exception("cannot change founder name")
      else:
         self._founder = new_founder

   @property
   def domain(self):
      return self._domain

   @domain.setter
   def domain(self, new_domain):
      if hasattr(self, "_domain"):
         raise Exception("domain already exists")
      else:
         self._domain = new_domain

   def pivot(self, new_name, new_domain):
      self.name = new_name
      self._domain = new_domain

   @classmethod
   def find_by_founder(cls, search_founder):
      for startup in Startup.all:
         if startup.founder == search_founder:
            return startup
      else:
         print("That founder does not exist")

   @classmethod
   def domains(cls):
      domains = []
      for startup in Startup.all:
         domains.append(startup.domain)
      return domains
   
   def sign_contract(self, new_venture_capitalist, new_type, new_investment):
      FundingRound(self, new_venture_capitalist, new_type, new_investment)

   @property
   def num_funding_rounds(self):
      startups_rounds = []
      for round in FundingRound.all:
         if round.startup == self:
            startups_rounds.append(round)
      return startups_rounds
   
   def total_funds(self):
      startups_funding = []
      for round in self.num_funding_rounds:
         startups_funding.append(round.investment)
      return sum(startups_funding)
   
   @property
   def investors(self):
      startups_investors = []
      for round in self.num_funding_rounds:
         startups_investors.append(round.venture_capitalist)
      unique = set(startups_investors)
      return list(unique)
   
   def big_investors(self):
      big_investors = []
      for investor in self.investors:
         if investor.total_worth > 1000000000:
            big_investors.append(investor)
      unique = set(big_investors)
      return list(unique)
