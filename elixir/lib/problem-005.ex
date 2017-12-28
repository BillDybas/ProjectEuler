defmodule Problem5 do
  @doc """
  2520 is the smallest number that can be divided by
  each of the numbers from 1 to 10 without any remainder.
  What is the smallest positive number that is evenly
  divisible by all of the numbers from 1 to 20?

    iex> Problem5.solve
    232792560
  """
  def solve do
    Enum.reduce(1..20, &lcm(&1, &2))
  end

  defp lcm(a, b) do
    div(abs(a), gcd(a, b)) * abs(b)
  end

  defp gcd(a, a), do: a
  defp gcd(a, b) when a > b, do: gcd(a - b, b)
  defp gcd(a, b), do: gcd(a, b - a)
end

IO.puts "Problem #5: #{Problem5.solve}"
