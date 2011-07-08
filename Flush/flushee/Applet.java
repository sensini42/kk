package flushee;

import javax.swing.JApplet;

public class Applet extends JApplet{

	private static final long serialVersionUID = 1L;

	public void init()
	  {
		Flushee flushee = new Flushee();
		add(flushee);
		setSize(400,400);
	  }
	
}
