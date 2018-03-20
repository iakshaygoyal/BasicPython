static String[] reducedFractionSums(String[] expressions){
		String[] ans=new String[expressions.length];
		for(int j=0;j<expressions.length;j++){
			String s=expressions[j];
			int[] arr=new int[4];
			int idx=0;
			for(int i=0;i<s.length();i++){
				char c=s.charAt(i);
				if(c=='/' || c=='+'){
					idx++;
					continue;
				}
				arr[idx]=arr[idx]*10 + (c-'0');
			}
			int val1=arr[0]*arr[3] + arr[1]*arr[2];
			int val2=arr[1]*arr[3];
			int g=gcd(val1,val2);
			ans[j]=val1/g + "/" + val2/g;
		}
		
		return ans;
	}
	
	static int gcd(int a,int b){
		if(b==0) return a;
		
		return gcd(b,a%b);
	}
