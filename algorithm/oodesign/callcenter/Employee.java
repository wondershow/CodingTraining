/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Dec 31, 2016
 */
package algorithm.oodesign.callcenter;

public abstract class Employee {

	private CallCenter center;
	private EmpRank rank;
	private Call call;
	
	public static void main(String[] args) {
		
	}
	
	public Employee(CallCenter c) {
		this.center = c;
	}
	
	public void handleCall(Call c) {
		this.call = c;
	}
	
	public void higherRank() {
		center.assignEmp(this);
	}
}
