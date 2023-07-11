from lib import *

# code here
# e.g.
# Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
#   vc1 = VentureCapitalist( 'Peter Gregory', 100000000 )
#   fr1 = FundingRound( s1, vc1, 'Pre-Seed', 200000.99 )


s1 = Startup("Facebook", "Mark", "www.facebook.com")
s2 = Startup("Google", "Bill", "www.google.com")
s3 = Startup("Meta", "Mark", "www.meta.com")


vc1 = VentureCapitalist( 'Peter Gregory', 100000000 )
vc2 = VentureCapitalist("Rich Guy McGee", 1000000000)
vc3 = VentureCapitalist("Super Rich man", 20000000000)

fr1 = FundingRound( s3, vc1, 'Pre-Seed', 200000.99 )
fr2 = FundingRound( s3, vc1, 'A Series', 716770.99 )
fr3 = FundingRound( s1, vc3, "Something", 12345)
fr4 =FundingRound( s1, vc1, 'Pre-Seed', 200000.99 )

# do not remove
import ipdb; ipdb.set_trace()
