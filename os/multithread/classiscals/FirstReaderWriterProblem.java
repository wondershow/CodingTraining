/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 24, 2017
 */
package os.multithread.classiscals;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.Semaphore;

public class FirstReaderWriterProblem {

	int readCount;
	private Semaphore writelock;
	private Semaphore readCountLock;
	private Random rand = new Random();
	final int MAX_SLEEP_TIME = 2000;
	private Map<String, Integer> schedules;
	
	public static void main(String[] args) {
		
	}
	
	public FirstReaderWriterProblem() {
		readCount = 0;
		writelock = new Semaphore(1, true);
		readCountLock = new Semaphore(1, true);
		schedules = new HashMap();
	}
	
	public void read(String key) throws InterruptedException{
		readCountLock.acquire();
		try {
			readCount++;
			if (readCount == 1) {
				writelock.acquire();
			}
		} finally {
			readCountLock.release();
		}
		
		Thread.sleep(rand.nextInt(MAX_SLEEP_TIME));
		
		System.out.println("value of " + key + " is " + schedules.get(key));
		
		readCountLock.acquire();
		try {
			readCount--;
			if (readCount == 0) {
				if (writelock.hasQueuedThreads()) {
					System.out.println("There are "
						+ writelock.getQueueLength()
					    + " waiting Threads on the write semaphore during reading ");
				}
				writelock.release();
			}
		} finally {
			readCountLock.release();
		}
	}
	
	
	public void write(String key, int val) throws InterruptedException{
		writelock.acquire();
		try {
			schedules.put(key,val);
			Thread.sleep(rand.nextInt(MAX_SLEEP_TIME));
		} finally  {
			writelock.release();
		}
	}
	
	private void init() {
		this.schedules.put("Flight-1", 1);
		this.schedules.put("Flight-2", 4);
		this.schedules.put("Flight-3", 6);
		printSchedules();
	}
	
	private void printSchedules() {
		System.out.print(Thread.currentThread().getId()
				+ " queried schedule ");
		for (String flight : this.schedules.keySet()) {
			System.out.println(flight + " : " + schedules.get(flight));
		}
	}
}
