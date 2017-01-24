/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 24, 2017
 */
package os.multithread.basics;

import java.util.Scanner;
/***
 * 
 * ITC inter-thread-communication demo in Java.
 * 1. wait() means, release the current object clock and put current 
 * thread into a "wait-to-run" queue. Note that, this wait-to-run
 * queue means when all other threads terminated, this thread can
 * be resumed
 * 
 * 2. notify() means, when the current critical block exits, 
 * notify all other threads that are in the "wait-to-run" queue and 
 * waiting for this object lock, that they can compete for this lock
 * 
 * 
 * **/


public class ITCDemo {
	
	public static void main(String[] args) 
				throws InterruptedException {
		final PC pc = new PC();
		
		// Create a thread object that calls pc.produce()
		Thread t1 = new Thread(new Runnable() {
			public void run() {
				try {
					pc.produce();
				} catch(InterruptedException e) {
					e.printStackTrace();
				}
			}
		});
		
		//Create another thread object that calls
		//pc.consume()
		Thread t2 = new Thread(new Runnable() {
			public void run(){
				try {
					pc.consume();
				} catch(InterruptedException e) {
					e.printStackTrace();
				}
			}
		});
		
		//Start both threads
		t2.start();
		t1.start();
		
		//t1 finishes before t2
		t1.join();
		t2.join();
	}
	
	public static class PC {
		public void produce() throws InterruptedException {
			// synchronized block ensures only one thread
			// running at a time.
			synchronized(this) {
				System.out.println("producer thread running");
				
				wait(50000);
				
				System.out.println("producer Resumed");
			}
		}
		
		// Sleeps for some time and waits for a key press. After key
		// is pressed, it notifies produce().
		public void consume() throws InterruptedException {
			// this makes the produce thread to run first.
			//Thread.sleep(1000);
			Scanner s = new Scanner(System.in);
			
			// synchronized block ensures only one thread
			// running at a time.
			synchronized(this) {
				System.out.println("Waiting for return key.");
				s.nextLine();
				System.out.println("Return key pressed");
				
				//notifies the produce thread that it
				//can wake up.
				notify();
				
				//sleep
				Thread.sleep(2000);
			}
		}
	}
}
