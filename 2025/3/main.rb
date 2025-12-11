# frozen_string_literal: true

# Day 3: Lobby

def input(filename = 'input.txt')
  File.read(File.join(File.dirname(__FILE__), filename))
end

def max_joltage(bank)
  arr = bank.split(//)
  a = arr[0, (arr.length - 1)].max
  max_index = arr.index(a)
  b = arr[max_index + 1, arr.length].max
  a.to_i * 10 + b.to_i
end

max = 0

input.split("\n").each do |n|
  max += max_joltage(n)
end

puts max
