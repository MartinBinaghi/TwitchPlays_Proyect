import Prelude hiding ((!!), (++))

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

esMultiploDe :: Int -> Int -> Bool
esMultiploDe numero divisor | mod numero divisor== 0 = True
                            | otherwise = False

max3::Int-> Int ->Int ->Int 
max3 x y z = max (max x y) z

min3::Int-> Int ->Int ->Int 
min3 x y z = min (min x y) z

dispersion:: Int-> Int ->Int ->Int 
dispersion x y z = (max3 x y z) - (min3 x y z)

esBisiesto:: Int->Bool
esBisiesto x | mod x 400 == 0 = True
        | (mod x 4 == 0) && not (mod x 100 == 0 )=True
        | otherwise = False

csToFahr:: Float -> Float
csToFahr x = x * 1.8 + 32

fahrToCs::Float -> Float
fahrToCs x = (x - 32)/1.8 

haceFrio::Float->Bool
haceFrio x | fahrToCs x < 8 = True
        |otherwise = False
        
segundo3:: (Int,Int,Int)->Int
segundo3 (x, y, z) = y

ordena:: (Int,Int)->(Int,Int)
ordena (x, y) = (min x y , max x y)

rangoPrecioParametrizado:: Int->(Int,Int)->String
rangoPrecioParametrizado a (x,z) | a < 0 = "esto no puede ser"
                                 | a < x = "muy barato"
                                 | a > z = "demasiado caro"
                                 | a >= x && a <= z = "hay que verlo bien"

mayorA3::Int->Bool
mayorA3 x | x > 3 = True
          | otherwise = False

mayor3:: (Int,Int,Int)->(Bool,Bool,Bool)
mayor3 (x,y,z) = (mayorA3 x, mayorA3 y, mayorA3 z)

todosIguales:: (Int,Int,Int)->Bool
todosIguales (x,y,z) = x == y && x == z

eliminarCabeza:: [a] -> [a]
eliminarCabeza [] = []
eliminarCabeza (x:xs) = xs

longitud2:: [Int] -> Int
longitud2 [] = 0
longitud2 (x:xs) = x + longitud2 xs

largo::[a]->Int
largo [] = 0
largo (x:xs) = 1 + largo xs

mayoresQue:: Int->[Int]->[Int]
mayoresQue n [] = []
mayoresQue n (x:xs) | n >= x = mayoresQue n xs
                    | otherwise = x : mayoresQue n xs

multiplica:: Int->[Int]->[Int]
multiplica n [] = []
multiplica n (x:xs) = n*x : multiplica n xs

menores10 :: [Int] -> Bool
menores10 [] = True
menores10 (x:xs) | x < 10 = menores10 xs
                 | otherwise = False

soloPares:: [Int]->[Int]
soloPares [] = []
soloPares (x:xs) | mod x 2 == 0 = x : soloPares xs           
                 | otherwise = soloPares xs

mayoresQueN:: Int->[Int]->[Int]
mayoresQueN n [] = []
mayoresQueN n (x:xs) | x > n = x : mayoresQueN n xs
                        | otherwise = mayoresQueN n xs

sumar1:: [Int]->[Int]
sumar1 [] = []
sumar1 (x:xs) = x + 1 : sumar1 xs

multiplicaN:: Int->[Int]->[Int]
multiplicaN n [] = []
multiplicaN n (x:xs) = n * x : multiplicaN n xs

concatenar:: [a]->[a]->[a]
concatenar [] [] = []
concatenar [] (x:xs) = x : concatenar [] xs
concatenar (x:xs) [] = x : concatenar xs []
concatenar (x:xs) (y:ys) = x : concatenar xs (y:ys)

tomar2:: Int -> [a]->[a]
tomar2 n [] = []
tomar2 n (x:xs) | n == 0 = []
                | otherwise = x : tomar2 (n-1) xs

soltar:: Int -> [a]->[a]
soltar n [] = []
soltar n (x:xs) | n == 0 = x : xs
                | otherwise = soltar (n-1) xs

largo2:: [a]->Int
largo2 [] = 0
largo2 (x:xs) = 1 + largo xs

sumalista:: [a]->[a]->[a]
sumalista [] [] = []
sumalista (x:xs) [] = x : sumalista xs []
sumalista [] (x:xs) = x : sumalista [] xs
sumalista (x:xs) (y:ys) = x : sumalista xs (y:ys)

(++):: [a] -> [a] -> [a]
[] ++ ys = ys  
(x:xs) ++ ys = x : xs ++ ys

(!!):: [a] -> Int -> a
[] !! n = error "lista vacia"
(x:xs) !! n      | n == 0 = x 
                 | otherwise = xs !! (n-1)


                 sdasd

