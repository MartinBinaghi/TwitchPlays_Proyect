promedio:: Float -> Float -> Float
promedio x y = (x+y)/2

f:: Float -> Float
f x = 5 * x

duplica :: Float -> Float
duplica a = a + a

por2:: Float -> Float
por2 y = 2 * y

multiplicar :: Float -> Float -> Float
multiplicar zz tt = zz * tt

signo :: Int -> Int
signo x | x > 0 = 1
        | x < 0 = -1
        | x == 0 = 0

entre0y9 :: Int -> Bool
entre0y9 x | x >=0 && x <= 9 = True
           | otherwise = False

rangoPrecio::Int->String
rangoPrecio precio | precio <= 0 = "esto no puede ser"
                   | 0 < precio && precio <2000 = "muy barato"
                   | 2000 <= precio && precio <= 5000 = "hay que ver bien"
                   | precio > 5000 = "demasiado caro"
