import java.util.*;
public class Solution {
    
	static class Pair{
		long val,smoke;
		Pair(long val,long smoke){
			this.val=val;
			this.smoke=smoke;
		}
	}
	
	public static void main(String[] args){
		Scanner scn=new Scanner(System.in);
		int t=scn.nextInt();
		while(t--!=0){
			int n=scn.nextInt();
			int[] colors=new int[n];
			for(int i=0;i<n;i++){
				colors[i]=scn.nextInt();
			}
			System.out.println(solve(n, colors));
		}
		scn.close();
	}
	
	public static long solve(int n,int colors[]){
		Pair[][] dp=new Pair[n][n];
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				dp[i][j]=new Pair(-1,-1);
			}
		}
    	return mixture(colors, 0, n-1, dp).smoke;
    }
	
	static Pair mixture(int[] colors,int si,int ei,Pair[][] dp){
		if(si==ei) return new Pair(colors[si], 0);
		
		if(dp[si][ei].val!=-1 && dp[si][ei].smoke!=-1) return dp[si][ei];
		
		long min_val=Integer.MAX_VALUE;
		long min_smoke=Integer.MAX_VALUE;
		for(int i=si;i<ei;i++){
			Pair left=mixture(colors, si, i, dp);
			Pair right=mixture(colors, i+1, ei, dp);
			long curr_smoke=left.smoke + right.smoke + (left.val * right.val);
			if(curr_smoke < min_smoke){
				min_smoke=curr_smoke;
				min_val=(left.val + right.val)%100;
			}
		}
		dp[si][ei].val=min_val;
		dp[si][ei].smoke=min_smoke;
		return new Pair(min_val, min_smoke);
	}
}
