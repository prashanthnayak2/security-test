  import subprocess

  def run(cmd):
      subprocess.call(cmd, shell=True)

  def calc(expr):
      return eval(expr)
