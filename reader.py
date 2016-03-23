# Author: Mingcheng Chen (linyufly@gmail.com)

import numpy as np
import tensorflow as tf

def _parse_recipe(filename):
  result = []
  with tf.gfile.GFile(filename, "r") as f:
    for line in f.read().lower().split("\r\n"):
      result.append(line.split(","))
  return np.array(result[1 : ])
