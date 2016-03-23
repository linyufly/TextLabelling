# Author: Mingcheng Chen (linyufly@gmail.com)

import os
import reader as rd
import tensorflow as tf

flags = tf.flags
FLAGS = flags.FLAGS

flags.DEFINE_string("task", "action_function", "Possible options are: action_function, action_channel, trigger_function, trigger_channel.")
flags.DEFINE_string("data_path", None, "data_path")

flags.DEFINE_float("train_ratio", 0.6, "The ratio of training data.")
flags.DEFINE_float("valid_ratio", 0.2, "The ratio of validation data.")

def main(_):
  if not FLAGS.data_path:
    raise ValueError("Must set --data_path to IFTTT data directory.")

  print "The task is to predict {0}.".format(FLAGS.task)

  filename = os.path.join(FLAGS.data_path, "dataset.txt")
  dataset = rd._parse_recipe(filename)

  train_size = int(len(dataset) * FLAGS.train_ratio)
  valid_size = int(len(dataset) * FLAGS.valid_ratio)

  print "train_size: {0}".format(train_size)
  print "valid_size: {0}".format(valid_size)
  print "test_size: {0}".format(len(dataset) - train_size - valid_size)

  vocabs = set([])
  sentences = []
  labels = []

  for recipe in dataset:
    sentence = recipe[0].split()
    sentences.append(sentence)
    for vocab in sentence:
      vocabs.add(vocab)
    task_id = {
        "action_function" : 1,
        "action_channel" : 2,
        "trigger_function" : 3,
        "trigger_channel" : 4,
    }[FLAGS.task]
    labels.append(recipe[task_id])



if __name__ == "__main__":
  tf.app.run()
