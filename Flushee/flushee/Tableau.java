package flushee;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Point;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.HashMap;
import java.util.Map;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class Tableau extends JPanel
  implements InterfaceBtn
{
  private static final long serialVersionUID = 1L;
  private int action = 0;
  private int pasX = 0;
  private int decX = 80;
  private int larg = 0;
  private int pasY = 0;
  private int haut = 0;
  public static final int BLANC = 0;
  public static final int ROUGE = 1;
  public static final int BLEU = 2;
  public static final int VERT = 3;
  public static final int JAUNE = 4;
  public static final int POMME = 5;
  public static final int SPIRALE = 6;
  private int[][] info = new int[7][6];
  private int[][] undo = new int[7][6];
  private int[][] infoSimul = new int[7][6];
  private int point = 0;
  private boolean affPoint = false;
  private int[][] groupe = new int[7][6];
  private int[][] lstPoint = new int[7][2];
  private Graphics graph;
  private InterfaceTableau intTabDroite;
  private InterfaceTableau intTabGauche;
  private InterfaceImage intImg;

  public Tableau()
  {
    addMouseListener(new MouseAdapter() {
      public void mousePressed(MouseEvent e) {
        Point pt = e.getPoint();
        Tableau.this.actionClic(pt.x / Tableau.this.pasX - 2, pt.y / Tableau.this.pasY);
      }
    });
  }

  protected void paintComponent(Graphics g)
  {
    super.paintComponent(g);
    g.setColor(Color.white);
    g.fillRect(0, 0, getWidth(), getHeight());
    Image im = this.intImg.loadImage(11);
    g.drawImage(im, 0, 0, im.getWidth(null), im.getHeight(null), null, null);

    g.setColor(Color.BLUE);
    this.pasX = 36;
    this.larg = (this.pasX * 6);
    this.pasY = 40;
    this.haut = (this.pasY * 7);

    for (int x = 0; x < 6; x++) {
      g.drawRect(x * this.pasX + this.decX, 0, this.pasX, this.haut);
    }
    for (int y = 0; y < 7; y++) {
      g.drawRect(this.decX, y * this.pasY, this.larg, this.pasY);
    }
    this.graph = g;

    for (int i = 0; i < 6; i++) {
      for (int j = 0; j < 7; j++) {
        afficheCellule(i, j);
      }
    }
    if (this.affPoint) affichePoint();
  }

  public void actionCalcul()
  {
    for (int ligne = 0; ligne < 7; ligne++) {
      actionFlushee(ligne, true);
      this.lstPoint[ligne][1] = this.point;
      if (this.intTabDroite != null) this.intTabDroite.libelleBtn(ligne, String.valueOf(this.point));
      actionFlushee(ligne, false);
      if (this.intTabGauche != null) this.intTabGauche.libelleBtn(ligne, String.valueOf(this.point));
      this.lstPoint[ligne][0] = this.point;
    }
    this.affPoint = true;
    repaint();
  }

  public void actionRaz() {
    this.undo = this.info;
    this.info = new int[7][6];
    this.affPoint = false;
    repaint();
  }

  public void setBtn(int i)
  {
    this.action = i;
  }

  public void setActionBtn(int ligne, boolean droite) {
    actionFlushee(ligne, droite);

    this.undo = this.info;
    this.info = new int[7][6];

    for (int y = 0; y < 7; y++) {
      for (int x = 0; x < 6; x++) {
        this.info[y][x] = this.infoSimul[y][x];
      }
    }
    this.affPoint = false;
    repaint();
  }

  public void actionUndo() {
    this.info = this.undo;
    this.affPoint = true;
    repaint();
  }
  public void actionClic(int i, int j) {
    if ((i >= 0) && (i < 6) && (j >= 0) && (j < 8)) {
      if (this.info[j][i] >= 1) efface(i, j);
      this.info[j][i] = this.action;
      this.graph = getGraphics();
      afficheCellule(i, j);
    }
    else if (j < 8) { setActionBtn(j, i > 5); }
  }

  public void afficheCellule(int i, int j)
  {
    if (this.info[j][i] > 0) {
      Image im = this.intImg.loadImage(this.info[j][i]);

      this.graph.drawImage(im, i * this.pasX + this.decX, j * this.pasY, null);
    }
  }

  public void affichePoint()
  {
    Font normal = new Font("Arial", 0, 15);
    Font gras = new Font("Arial", 1, 15);
    int maxPoint = 0; int maxPointX = 0; int maxPointY = 0;

    for (int j = 0; j < 7; j++) {
      for (int i = 0; i < 2; i++) {
        if (this.lstPoint[j][i] >= maxPoint) {
          maxPoint = this.lstPoint[j][i];
          if (i == 0) maxPointX = -1; else
            maxPointX = 6;
          maxPointY = j;
        }
        int y;
        int x;
        if (i == 0) {
          x = 0;
          y = (int)((j + 0.5D) * this.pasY);
        } else {
          x = 7 * this.pasX + this.decX + 10;
          y = (int)((j + 0.5D) * this.pasY);
        }
        if (this.lstPoint[j][i] >= 1000) {
          this.graph.setColor(Color.RED);
          this.graph.setFont(gras);
        } else {
          this.graph.setColor(Color.BLACK);
          this.graph.setFont(normal);
        }
        this.graph.drawString(String.valueOf(this.lstPoint[j][i]), x, y);
      }

    }

    Image im = this.intImg.loadImage(this.action);
    this.graph.drawImage(im, maxPointX * this.pasX + this.decX, maxPointY * this.pasY, null);
  }

  private void efface(int i, int j)
  {
    this.graph.setColor(Color.BLACK);
    this.graph.drawRect(this.pasX * i + this.decX, this.pasY * j, this.pasX, this.pasY);
    this.graph.setColor(Color.WHITE);
    this.graph.fillRect(this.pasX * i + this.decX + 1, this.pasY * j + 1, this.pasX - 2, this.pasY - 2);
  }

  public void decallageFlushee(int ligne, boolean droite) {
    int flusheeTombe = 0;

    if (droite) {
      flusheeTombe = this.infoSimul[ligne][0];
      for (int x = 0; x < 5; x++) {
        this.infoSimul[ligne][x] = this.infoSimul[ligne][(x + 1)];
      }
      this.infoSimul[ligne][5] = this.action;
    }
    else {
      flusheeTombe = this.info[ligne][5];
      for (int x = 4; x >= 0; x--) {
        this.infoSimul[ligne][(x + 1)] = this.infoSimul[ligne][x];
      }
      this.infoSimul[ligne][0] = this.action;
    }
    if (flusheeTombe == 5) this.point += 1000; 
  }

  public boolean destructionGroupe(int coef) {
    boolean supGroupe = false;
    this.groupe = new int[7][6];
    int cptGroupe = 0;
    for (int y = 0; y < 7; y++) {
      for (int x = 0; x < 6; x++) {
        if ((this.infoSimul[y][x] < 1) || (this.infoSimul[y][x] > 4))
        {
          continue;
        }

        int eltX = 0; int eltY = 0;

        for (int i = 0; i < 2; i++) {
          switch (i) { case 0:
            eltX = x + 1; eltY = y; break;
          case 1:
            eltX = x; eltY = y + 1;
          }
          if ((eltX >= 6) || (eltY >= 7) || (this.infoSimul[y][x] != this.infoSimul[eltY][eltX]))
            continue;
          if (this.groupe[y][x] == 0) { cptGroupe++; this.groupe[y][x] = cptGroupe;
          }
          if (this.groupe[eltY][eltX] == 0) this.groupe[eltY][eltX] = this.groupe[y][x];
          else
          {
            traitementGroupe(this.groupe[y][x], this.groupe[eltY][eltX]);
          }

        }

      }

    }

    Map<String,Integer> map = new HashMap<String,Integer>();
    for (int y = 0; y < 7; y++)
      for (int x = 0; x < 6; x++)
        if (this.groupe[y][x] != 0) {
          String cle = String.valueOf(this.groupe[y][x]);
          Integer nb = Integer.valueOf(0);
          if (map.containsKey(cle)) {
            nb = (Integer)map.get(cle);
          }
          nb = Integer.valueOf(nb.intValue() + 1);
          map.remove(cle);
          map.put(cle, nb);
        }
    int x;
    for (int y = 0; y < 7; y++) {
      for (x = 0; x < 6; x++) {
        if (this.groupe[y][x] > 0) {
          String cle = String.valueOf(this.groupe[y][x]);
          if ((map.containsKey(cle)) && (((Integer)map.get(cle)).intValue() >= 4)) {
            supGroupe = true;
            this.infoSimul[y][x] = -1;
          }
        }
      }
    }

    for (Integer i : map.values()) {
      if (i.intValue() < 4) continue; this.point += (i.intValue() - 1) * 50 * coef;
    }

    return supGroupe;
  }

  public void impesanteur()
  {
    int haltidude = 0;
    for (int x = 0; x < 6; x++) {
      haltidude = 7;
      for (int y = 6; y >= 0; y--)
        if (this.infoSimul[y][x] != -1) {
          haltidude--;
          if (y != haltidude) {
            this.infoSimul[haltidude][x] = this.infoSimul[y][x];
            this.infoSimul[y][x] = -1;
          }
        }
    }
  }

  public void actionFlushee(int ligne, boolean droite)
  {
    for (int y = 0; y < 7; y++) {
      for (int x = 0; x < 6; x++) {
        this.infoSimul[y][x] = this.info[y][x];
      }
    }

    this.point = 0;

    decallageFlushee(ligne, droite);

    int coef = 1;
    while (destructionGroupe(coef)) {
      impesanteur();

      coef++;
    }
  }

  private void traitementGroupe(int groupe1, int groupe2)
  {
    for (int x = 0; x < 6; x++)
      for (int y = 0; y < 7; y++) {
        if (this.groupe[y][x] != groupe2) continue; this.groupe[y][x] = groupe1;
      }
  }

  public void setAction(int action)
  {
    this.action = action;
  }
  public void setInfo(int[][] info) {
    this.info = info;
  }
  public void setInfoSimul(int[][] info) {
    this.infoSimul = info;
  }
  public void setPoint(int point) {
    this.point = point;
  }
  public int[][] getGroupe() {
    return this.groupe;
  }
  public int[][] getInfo() {
    return this.info;
  }

  public int[][] getInfoSimul() {
    return this.infoSimul;
  }
  public int getPoint() {
    return this.point;
  }

  public InterfaceTableau getIntTabDroite()
  {
    return this.intTabDroite;
  }

  public void setIntTabDroite(InterfaceTableau intTabDroite)
  {
    this.intTabDroite = intTabDroite;
  }

  public InterfaceTableau getIntTabGauche()
  {
    return this.intTabGauche;
  }

  public void setIntTabGauche(InterfaceTableau intTabGauche)
  {
    this.intTabGauche = intTabGauche;
  }
  public void setIntImg(InterfaceImage intImg) {
    this.intImg = intImg;
  }

  public int actionPhoto() {
    try {
      AnalyseImage anaIma = new AnalyseImage();
      anaIma.setIntImg(this.intImg);
      anaIma.captureEcran();
      anaIma.compareImage();
      this.info = anaIma.getInfo();
      this.action = anaIma.getAction();
      if (this.action != 0)
        actionCalcul();
      else {
        JOptionPane.showMessageDialog(this, "ProblÃ¨me dans la recherche automatique : ne trouve pas la fenÃªtre kadokado");
      }
      return this.action;
    } catch (Exception e) {
      JOptionPane.showMessageDialog(this, "ProblÃ¨me dans la recherche automatique :" + e.getMessage());
    }return 0;
  }
}
