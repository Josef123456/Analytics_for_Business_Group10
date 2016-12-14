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
subject to creat_community1: x[51,1]+ x[56,1]+x[28,1]+x[14,1]+ x[12,1] <=2;
subject to creat_community2: x[32,1]+ x[54,1]+x[43,1]+x[41,1]+ x[42,1]+x[55,1]+x[16,1]+x[18,1]+x[13,1] <=2;
subject to creat_community3: x[49,1]+ x[27,1]+x[23,1]+x[57,1]+ x[4,1]+x[5,1]+x[11,1]+x[2,1]+x[44,1]+x[26,1]+x[36,1]+x[9,1]+x[40,1]+x[53,1]<=2;
subject to creat_community4: x[15,1]+ x[1,1]+x[29,1]+x[3,1]+ x[37,1]+x[21,1]+x[20,1]+x[60,1]+x[47,1]+x[38,1]+x[52,1]+x[33,1]+x[46,1]+x[59,1] +x[24,1]+x[19,1]+x[17,1]+x[34,1]+x[22,1] +x[7,1]+x[50,1]+x[6,1]+x[45,1]+x[35,1] +x[10,1]+x[30,1]+x[8,1]+x[31,1]+x[58,1] + x[48,1] + x[39,1]<=2;
subject to inf_community1: x[51,2]+ x[56,2]+x[28,2]+x[14,2]+ x[12,2] <=2;
subject to inf_community2: x[32,2]+ x[54,2]+x[43,2]+x[41,2]+ x[42,2]+x[55,2]+x[16,2]+x[18,2]+x[13,2] <=2;
subject to inf_community3: x[49,2]+ x[27,2]+x[23,2]+x[57,2]+ x[4,2]+x[5,2]+x[11,2]+x[2,2]+x[44,2]+x[26,2]+x[36,2]+x[9,2]+x[40,2]+x[53,2]<=2;
subject to inf_community4: x[15,2]+ x[1,2]+x[29,2]+x[3,2]+ x[37,2]+x[21,2]+x[20,2]+x[60,2]+x[47,2]+x[38,2]+x[52,2]+x[33,2]+x[46,2]+x[59,2] +x[24,2]+x[19,2]+x[17,2]+x[34,2]+x[22,2] +x[7,2]+x[50,2]+x[6,2]+x[45,2]+x[35,2] +x[10,2]+x[30,2]+x[8,2]+x[31,2]+x[58,2] + x[48,2] + x[39,2]<=2;