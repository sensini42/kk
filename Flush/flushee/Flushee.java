package flushee;


import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Image;
import java.net.URL;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Flushee extends JPanel
  implements InterfaceImage
{
  private static final long serialVersionUID = 1L;
  private LstBtn lstBtn;
  private Tableau tableau;
  private static String[] lstImageNom = { "gomme.png", "red.png", "violet.png", "vert.png", "jaune.png", "pomme.png", "spirale.png", 
    "", "undo.png", "photo.png", "img1.png", "fond.png" };

  private ImageIcon[] lstImageIcon = new ImageIcon[12];

  public Flushee()
  {
    for (int i = 0; i < lstImageNom.length; i++) {
      try
      {
        URL url = getClass().getResource("/flushee/" + lstImageNom[i]);
        if ((url != null) && 
          ("".compareTo(lstImageNom[i]) != 0)) this.lstImageIcon[i] = new ImageIcon(url); 
      }
      catch (Exception e)
      {
        e.printStackTrace();
      }
    }
    this.lstBtn = new LstBtn(this);
    setLayout(new BorderLayout());
    add(this.lstBtn, "North");
    this.tableau = new Tableau();
    this.tableau.setSize(400, 320);
    this.tableau.setMinimumSize(new Dimension(400, 320));
    this.tableau.setMaximumSize(new Dimension(400, 320));
    this.lstBtn.setInterfaceBtn(this.tableau);
    add(this.tableau, "Center");
    this.tableau.setIntImg(this);
  }

  public Image loadImage(int action)
  {
    if (this.lstImageIcon[action] == null) return null;
    return this.lstImageIcon[action].getImage();
  }

  public boolean isImage(int action) {
    return this.lstImageIcon[action] != null;
  }
  
  public static void main(String[] args){
	  JFrame main = new JFrame("Flushee");
	  main.getContentPane().add(new Flushee());
	  main.pack();
	  main.setVisible(true);
	  main.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	  main.setSize(400, 400);
	  main.setResizable(false);
  }
  
}
