# frozen_string_literal: true

# Day 2: Gift Shop

def invalid_id?(id)
  if id.length.to_i.odd?
    false
  else
    id[0, (id.length / 2)] == id[(id.length / 2), id.length]
  end
end

def invalid_id_2?(id)
  id.match?(/^(\d+)\1+$/)
end

def answer(input, validator = method(:invalid_id?))
  answer = 0
  id_ranges = File.read(File.join(File.dirname(__FILE__), input)).split(',')
  id_ranges.each do |range|
    min, max = range.scan(/([0-9]+)/)

    (min[0]..max[0]).each do |id|
      answer += id.to_i if validator.call(id)
    end
  end
  answer
end

puts answer('input.txt')
puts answer('input.txt', method(:invalid_id_2?))
