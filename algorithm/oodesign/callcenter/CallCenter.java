/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Dec 31, 2016
 */
package algorithm.oodesign.callcenter;

import java.util.ArrayList;
import java.util.List;

public class CallCenter {

	private static CallCenter singleton = null;
	
	private static final int MANAGER_NUMBER = 5;
	private static final int DIRECTOR_NUMBER = 2;
	private static final int RESPONDENT_NUMBER = 25;
	
	private List<Manager> managers;
	private List<Director> directors;
	private List<Respondent> respondents;
	
	public static void main(String[] args) {

	}
	
	public void assignEmp(Employee emp) {
		
	}
	
	public void receiveCall(Caller client) {
		
	}
	
	
	
	private int remainingRepondents() {
		return managers.size();
	}
	
	private int remainingManagers() {
		return directors.size();
	}
	
	private int remainingDirectors() {
		return respondents.size();
	}
	
	private CallCenter() {
		managers = new ArrayList();
		directors = new ArrayList();
	    respondents = new ArrayList();
	}
	
	public static CallCenter getCallCenter() {
		if (singleton == null) {
			singleton = new CallCenter();
		}
		return singleton;
	}
}
