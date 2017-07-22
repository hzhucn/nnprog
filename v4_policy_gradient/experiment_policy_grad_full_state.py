from env import *
from draw import *
from stateless_model import *


bitadd = BitAdd()
# make a driver that doesn't use abstract state
driver = StatelessAgent("driver", 32, len(bitadd.ACTIONS), False)

exp_size = 20

exp = Experience(exp_size)

# populate some experience
# for i in xrange(2000):
while exp.check_success() < exp_size / 2:
  tr = bitadd.get_trace(driver)
  exp.add_success(tr)
  print "succss trace cnt ",  exp.check_success()

for i in range (exp_size / 2):
  tr = bitadd.get_trace(driver)
  exp.add(tr)

# do some training
for i in xrange(1000000):
  tr = bitadd.get_trace(driver)
  # print tr[-1]
  exp.add_balanced(tr)

  if i % 20 == 0:
    # training
    trace_batch = exp.n_sample(20)
    driver.learn(trace_batch, bitadd)

  if i % 100 == 0:
    print "succss trace cnt ",  exp.check_success()
    driver.inspect = True
    tr = bitadd.get_trace(driver)
    driver.inspect = False
    for trr in tr:
      print trr

