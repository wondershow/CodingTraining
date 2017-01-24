/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 24, 2017
 */
package os.multithread.basics;
/**
 * 
 * Java MultiThread basics
 * How to create a Thread, there are two ways, 1. extend 
 * a Thread class or 2. implement runnable method
 * This code demos how to create a thread by extending 
 * Thread class
 * **/
public class ThreadCreationDemo extends Thread {

	public static void main(String[] args) {
		for (int i = 0; i < 10; i++) {
			ThreadCreationDemo td = new ThreadCreationDemo();
			td.start();
		}
	}
	
	public void run() {
		try {
			System.out.println("Thread ID : " 
		+ Thread.currentThread().getId() + " is running");
		} catch (Exception e) {
			System.out.println("concurrency excepton");
		}
	}
}
