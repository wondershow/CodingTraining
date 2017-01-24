/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 24, 2017
 */
package os.multithread.classiscals;

import java.util.LinkedList;
import java.util.Random;

/***
 * http://www.geeksforgeeks.org/producer-consumer-solution-using-threads-java/
 * 
 * Classical Consumer and producer problem. 
 * 
 * One consumer and one producer and a buffer.
 * Notes:
 * Consumer Producer has to compete a lock, which is the object lock of 
 * CP, so that they can go ahead. When the buffer condition test fails, 
 * they need to call "wait()" to release lock. And after job is done, 
 * they need to call "notify()" to wake up other therad.
 * 
 * ***/
class Person {
	
	LinkedList<Integer> buffer = new LinkedList();
	int capacity = 5;
	Random rand = new Random();
	int maxProduce = 100000;
	boolean alternative = true;
	
	public Person() {
		
	}
	
	public void produce() throws InterruptedException{
		while (true) {
			synchronized(this) {
				while (buffer.size() == capacity) {
					wait();
				}
				int newProduce = rand.nextInt(maxProduce);
				buffer.add(newProduce);
				System.out.println("Just produced : " + newProduce);
				notify();
				Thread.sleep(rand.nextInt(3000));
			}
		}
	}
	
	public void consume() throws InterruptedException{
		while (true) {
			synchronized(this) {
				while (buffer.size() == 0) {
					wait();
				}
				System.out.println("Just consumed : " + buffer.removeFirst());
				notify();
				Thread.sleep(rand.nextInt(1000));
			}
		}
	}
}



public class ConsumerProducer {
	public static void main(String[] args) throws InterruptedException{
		LinkedList<Integer> buffer = new LinkedList();
		int maxSize = 10;
		Object o = new Object();
		
		//Note that you need to be put into another thread/
		//that means this object is not supposd to be changed so its final
		final Person pc = new Person();
		Thread c = new Thread(new Runnable () {
			public void run() {
				try {
					pc.consume();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		});
		
		Thread p = new Thread(new Runnable () {
			public void run() {
				try {
					pc.produce();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		});
		
		c.start();
		p.start();
	}
}
