/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 1, 2017
 */
package os;

import java.util.ArrayList;
import java.util.List;

/***
 * Classical Thread synchronization demo code.
 * Produce produces things for consumer to eat.
 * The products are put into a buffer area called "pool"
 * In this case, the add/remove operations of pool are
 * critical code since two Threads are competing shared resources
 * In this case, we need to use a lock to offer exclusive visit
 * to critical resource.
 * ****/
public class ConsumerProducer {
	private static List<String> pool = new ArrayList();
	
	public static void main(String[] args) {
		new Producer().start();
		new Consumer().start();
	}
	
	private static class Producer extends Thread {
		static int Sequence = 0;
		Producer() {
			super("Producer");
		}
		
		public void run() {
			for (;;) {
				try {
					Thread.sleep(10);
				} catch(Exception e) {
					e.printStackTrace();
				}
				synchronized(pool) {
					pool.add("Product " + Sequence++);
				}
			}
		}
	}
	
	private static class Consumer extends Thread {
		public Consumer() {
			super("Consumer");
		}
		
		public void run() {
			while (true) {
				try {
	                Thread.sleep(1);
	            } catch (Exception e) {
	                e.printStackTrace();
	            }
				
				synchronized(pool) {
					System.out.println(pool.remove(0));
				}
			}
		}
	}
}
