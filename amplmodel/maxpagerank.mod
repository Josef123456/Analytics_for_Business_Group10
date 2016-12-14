set id ordered ;
param create_pr {id};
param imp_pr {id};
param inf_pr {id};
param friendship_indegree {id};

data allpagerank.dat;
param N := 3;

var x {i in id , 1.. N} binary;

maximize pr: sum {i in id} (x[i,1]*create_pr[i]+ x[i,2]*inf_pr[i] +x[i,3]*imp_pr[i]);

subject to create_friendship: sum {i in id}  (x[i,1]*friendship_indegree[i]) <= 30;
subject to inf_friendship: sum {i in id}  (x[i,2]*friendship_indegree[i]) <= 30;
subject to imp_friendship: sum {i in id}  (x[i,3]*friendship_indegree[i]) <= 30;
subject to create_4members:  sum {i in id} (x[i,1]) = 5;
subject to inf_4members:  sum {i in id} (x[i,2]) = 5;
subject to imp_4members:  sum {i in id} (x[i,3]) = 5;
subject to picked_once {i in id}: x[i,1] + x[i,2] + x[i,3] <= 1;
subject to create_leader: x[7,1] = 1;
subject to inf_leader: x[21,2] = 1;
subject to imp_leader: x[19,3] = 1;