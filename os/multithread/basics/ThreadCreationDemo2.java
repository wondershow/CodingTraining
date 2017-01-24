/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 24, 2017
 */
package os.multithread.basics;
/**
 * Java MultiThread basics
 * How to create a Thread, there are two ways, 1. extend 
 * a Thread class or 2. implement runnable method
 * This code demos how to create a thread passing a runnable
 * -interface-implementd object to a Thread constructor. Then 
 * by calling start of that thread object, we can fan out
 *  multiple threads
 * **/
public class ThreadCreationDemo2 implements Runnable{

	public static void main(String[] args) {
		for (int i = 0; i < 10; i++) {
			Thread td 
				= new Thread(new ThreadCreationDemo2());
			td.start();
		}
	}

	@Override
	public void run() {
		try {
			System.out.println("#" + Thread.currentThread().getId() 
					+ " Thread is running");
		} catch (Exception e) {
			System.out.println("wrong");
		}
	}

}
