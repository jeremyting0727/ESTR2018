n=readline(prompt = "Number of states: ")
n=as.numeric(n)

x<-matrix(,nrow=n,ncol=n)
y<-matrix(,nrow=n,ncol=1)
#initial of each state 
for(i in 1:n){
  intit=readline(prompt =paste("The probability of being in state ",i," initially is: "))
  intit<-as.numeric(intit)
  y[i,1]<-intit
}
#each transition probability
for(i in 1:n){
  for(j in 1:n){
    if(i==j){
      prob=readline(prompt =paste("The probability of being in state ",i," is:"))
      prob=as.numeric(prob)
    }else{
      prob=readline(prompt =paste("The probability of transitioning from state ", i," to state ",j," is : "))
      prob=as.numeric(prob)
    }
    x[j,i]<-prob
  }
}
#matrix multiplication
intit<-x
m<-as.numeric(readline(prompt = "Number of transitions: "))
for(num in 1:m-1){
  x<-x%*%intit
}
ans<-x%*%y
for(i in 1:n) print(paste("The probability of being in state ",i," is ",ans[i]))

#Monte Carlo simulation
SIZE=1000000
estimate<-rep(0,5)

for(i in 1:SIZE){
  initial<-sample(1:n,size=1,prob=y[,1])
  for(j in 1:m){
    initial=sample(1:n,size=1,prob=intit[,initial])
  }
  estimate[initial]=estimate[initial]+1
}
options(digit=12)
for(i in 1:n) print(paste("The estimate probability of being in state ",i," is ",estimate[i]/SIZE))
