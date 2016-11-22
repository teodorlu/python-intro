module Main where

partName t f = "plate_4_6_" ++ show t ++ "_" ++ show f

partNames = do
  t <- [160, 200, 260]
  f <- [7, 10, 10]
  return $ partName t f

main = mapM_ putStrLn partNames
