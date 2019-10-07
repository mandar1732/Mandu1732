c = int(input("Enter Initial level of debt"))
n=int(c+(0.1*c))
intr = int(input("Enter Interest Percentage"))
rpp = int(input("Enter Repayment Percentage"))
dps = 0
intes = 0
rp = 0.01 * rpp * n
for i in range(0,n):
    if(n<0):
        break
    if(n<50):
        break
    inte = 0.01 * intr * n
    dp = rp - inte
    dps = dp + dps
    intes = inte + intes
    n = n - dp
print("Total payment to be made is: ",(intes + dps))