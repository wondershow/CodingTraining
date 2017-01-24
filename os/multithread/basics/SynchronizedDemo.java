/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 24, 2017
 */
package os.multithread.basics;

import java.util.Random;

/**
 * Tutorial from :
 * http://quiz.geeksforgeeks.org/synchronized-in-java/
 * 
 * A demo of using "synchronized" keyword to assure the exclusive
 * use of ONE OBJECT(not one class!). 
 * 
 * Scenario description, a postman delivers mail to its destination
 * We force that a postman can not deliver other mail when he is 
 * on his way delivering a mail.
 * 
 * Here we create a SendThread class to implement this mechanism
 * In the run function of SendThread code, we use a "synchronized(s)"
 * keyword to obtain a "lock" of Postman object. Althgouth we created
 * two or more SendThread to send multiple mails, that means
 * the "run()" code can be entered by two or mroe threads at the same
 * tiem, we used "synchronized(s)", let the OS/JVM check before entergin
 * the code block that if that thread has obtained the lock of that 
 * postman object. if yes, then this thread will flow ahead, otherwise
 * it will be blocked. 
 * 
 * NOTE:
 * comment out the "synchronized(s)" statement and compare the outputs
 * 
 * ***/

class Postman {
	public void send(String msg) {
		System.out.println("Sending msg (" + msg + ")");
		
		Random rand = new Random();
		for (int i = 0; i < rand.nextInt(20);) {
			try {
				Thread.sleep(500);
				System.out.println("msg (" + msg + ")" + "on the way"
						+ "any other ppl can use this channcel to send");
			} catch(Exception e) {
				System.out.println("Thread exception");
			}
		}
		
		System.out.println("msg  (" + msg + ") recevied");
	}
}

class SendThread extends Thread {
	private String msg;
	private Thread t;
	Postman s;
	
	SendThread(String m, Postman obj) {
		msg = m;
		s = obj;
	}
	
	public void run() {
		synchronized(s) {
			s.send(msg);
		}
	}
}



public class SynchronizedDemo {

	public static void main(String[] args) {
		Postman postman = new Postman();
		SendThread s1 = new SendThread("Mail one", postman);
		SendThread s2 = new SendThread("Mail two", postman);
		s1.start();
		s2.start();
	}
	
	
}
