/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Dec 31, 2016
 */
package algorithm.oodesign.callcenter;

public enum EmpRank {
	Respondent (1), Manager (2), Director (3);
	private int value;
	private static final int RANK_CEILING = 3;
	EmpRank(int v) {
		value = v;
	}
	
	public static EmpRank nextRank(EmpRank r) {
		if (r.value == RANK_CEILING) {
			return null;
		} else {
			if (r.value == 1) return EmpRank.Manager;
			else return EmpRank.Director;
		}
	}
}
