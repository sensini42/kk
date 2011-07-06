package flushee;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class LstBtn extends JPanel
{
  private static final long serialVersionUID = 1L;
  private JButton[] lstBtn = new JButton[10];
  private static String[] lstLabel = { "w", "r", "b", "g", "y", "a", "s", "calculer", "undo", "photo" };

  private static int[] lstAction = { 0, 1, 2, 3, 4, 5, 6 };
  private InterfaceBtn interfaceBtn;
  private int btnActif = -1;

  public LstBtn(InterfaceImage img) {
    setLayout(new FlowLayout(1, 0, 0));
    for (int i = 0; i < this.lstBtn.length; i++) {
      this.lstBtn[i] = new JButton();

      if (img.isImage(i)) {
        int j = i == 9 ? 60 : 20;
        Image im = img.loadImage(i).getScaledInstance(j, 20, 1);
        this.lstBtn[i].setIcon(new ImageIcon(im));
        this.lstBtn[i].setPreferredSize(new Dimension(j + 10, 30)); } else {
        this.lstBtn[i].setText(lstLabel[i]);
      }
      switch (i) {
      case 0:
        this.lstBtn[i].addActionListener(new ActionListener()
        {
          public void actionPerformed(ActionEvent e) {
            int res = JOptionPane.showConfirmDialog(null, 
              "Nouveau tableau ?");
            if (res == 0)
              LstBtn.this.interfaceBtn.actionRaz();
          }
        });
        break;
      case 7:
        this.lstBtn[i].addActionListener(new ActionListener() {
          public void actionPerformed(ActionEvent e) {
            LstBtn.this.interfaceBtn.actionCalcul();
          }
        });
        this.lstBtn[i].setPreferredSize(new Dimension(100, 30));

        break;
      case 8:
        this.lstBtn[i].addActionListener(new ActionListener() {
          public void actionPerformed(ActionEvent e) {
            LstBtn.this.interfaceBtn.actionUndo();
          }
        });
        break;
      case 9:
        this.lstBtn[i].addActionListener(new ActionListener() {
          public void actionPerformed(ActionEvent e) {
            int action = LstBtn.this.interfaceBtn.actionPhoto();
            if (LstBtn.this.btnActif != -1) LstBtn.this.lstBtn[LstBtn.this.btnActif].setBackground(null);
            if (action != 0) {
              LstBtn.this.btnActif = action;
              LstBtn.this.lstBtn[LstBtn.this.btnActif].setBackground(Color.BLUE);
            }

            LstBtn.this.interfaceSimple(action != 0);
          }
        });
        break;
      case 1:
      case 2:
      case 3:
      case 4:
      case 5:
      case 6:
      default:
        final int nb = i;
        this.lstBtn[i].addActionListener(new ActionListener()
        {
          public void actionPerformed(ActionEvent e) {
            if (LstBtn.this.btnActif != -1) LstBtn.this.lstBtn[LstBtn.this.btnActif].setBackground(null);
            LstBtn.this.btnActif = nb;
            LstBtn.this.lstBtn[LstBtn.this.btnActif].setBackground(Color.BLUE);
            LstBtn.this.interfaceBtn.setBtn(LstBtn.lstAction[nb]);
          }
        });
      }
      add(this.lstBtn[i]);
    }

    interfaceSimple(true);
  }

  public void interfaceSimple(boolean val)
  {
    for (int i = 0; i < 9; i++) this.lstBtn[i].setVisible(!val);
    this.lstBtn[9].setPreferredSize(new Dimension(val ? 60 : 30, 30));
  }

  public InterfaceBtn getInterfaceBtn() {
    return this.interfaceBtn;
  }
  public void setInterfaceBtn(InterfaceBtn interfaceBtn) {
    this.interfaceBtn = interfaceBtn;
  }
}

