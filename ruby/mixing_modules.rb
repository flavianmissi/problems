module Foo
  def self.extended base
    puts "Extended from " << base.to_s
  end

  def foo_bar
    puts "foo_bar called"
  end
end

module Bar
  extend Foo
  foo_bar
  def oi
    puts "oi"
  end
end

class FooClass
  extend Foo
  foo_bar
  def teste
    puts "teste"
  end
end

fb = FooClass.new
fb.teste

include Bar
Bar.oi
