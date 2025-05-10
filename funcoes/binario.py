def dec_to_bin(decimal: int) -> int:
    binario = 0
    pot10 = 1
    while decimal != 0:
        resto = decimal % 2
        decimal = decimal // 2        
        binario = binario + resto * pot10
        pot10 = pot10 * 10
    
    return binario


bin = dec_to_bin(8729)
print(bin)