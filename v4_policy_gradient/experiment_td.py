from env import *
from draw import *
from td_agent import *

def collect_stat(record, trace, env):
  for tr in trace:
    s, name_a, _, _ = tr
    _, a = name_a
    if (env.abstract(s), a) not in record:
      record[(env.abstract(s), a)] = 0
    record[(env.abstract(s), a)] += 1

knight = Knight()
td_agent = TDLearn(knight)
exp = Experience(1000)

# populate some experience
for i in xrange(100):
  tr = knight.get_trace(td_agent)
  exp.add(tr)

record = {}

# do some training
for i in xrange(10000):
  tr = knight.get_trace(td_agent)
  # print tr
  exp.add(tr)

  # training
  trace_batch = exp.n_sample(20)
  td_agent.learn(trace_batch, knight)

  print i, tr[-1]

  if i > 500:
    collect_stat(record, tr, knight)

  if i % 100 == 0:
    print "record"
    for blah in sorted(list(record.keys())):
      print blah, record[blah]
