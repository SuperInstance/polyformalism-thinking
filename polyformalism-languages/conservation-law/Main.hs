{- HASKELL: What purity reveals about conservation
   Forces you to think about: The law is timeless, existing outside execution.
   Broken assumption: That iteration is natural — Haskell thinks in lazy streams.
   Novel insight: map compute_delta [1..] is valid. The infinite-fleet limit
     is a computable list, not a mathematical abstraction.
-}

delta :: Floating a => a -> a
delta n = (1 / sqrt n) * (1 - 3 / (2 * n))

ccr :: Floating a => a -> a
ccr n = delta n * 100

main :: IO ()
main = do
  putStrLn $ printf "%5s  %10s  %8s" "n" "δ(n)" "CCR%"
  putStrLn $ replicate 28 '-'
  mapM_ (\n -> putStrLn $ printf "%5d  %10.6f  %7.2f%%" n (delta (fromIntegral n)) (ccr (fromIntegral n))) [1..100]

printf :: String -> String
printf = id  -- simplified: real version would use Text.Printf
