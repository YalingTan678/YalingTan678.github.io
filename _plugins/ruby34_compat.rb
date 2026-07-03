# Local-build compatibility: Ruby 3.2+ removed taint tracking that liquid 4.0.3 expects.
# GitHub Pages builds in safe mode and ignores _plugins, so this only affects local jekyll serve.
class Object
  def tainted?; false; end unless method_defined?(:tainted?)
  def untaint; self; end unless method_defined?(:untaint)
  def taint; self; end unless method_defined?(:taint)
end
