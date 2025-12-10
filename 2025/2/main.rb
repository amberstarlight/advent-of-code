# Day 2: Gift Shop

def invalid_id?(id)
  if id.length.to_i.odd?
    false
  else
    id[0, (id.length / 2)] == id[(id.length / 2), id.length]
  end
end

def answer(input)
  answer = 0
  id_ranges = File.read(File.join(File.dirname(__FILE__), input)).split(",")
  id_ranges.each { |range|
    min, max = range.scan(/([0-9]+)/)

    (min[0]..max[0]).each do |id|
      if invalid_id?(id)
        answer += id.to_i
      end
    end
  }
  answer
end

puts answer("input.txt")
