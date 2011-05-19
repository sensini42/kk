package flushee;

import java.awt.AWTException;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;

import javax.swing.ImageIcon;

public class AnalyseImage
{
  private BufferedImage image;
  private BufferedImage imageComp;
  private int[][] info = new int[7][6];
  private int action = 0;
  private InterfaceImage intImg;
  public static final int ROUGE = -5239022;
  public static final int BLEU = -9491771;
  public static final int VERT = -11076091;
  public static final int JAUNE = -3644159;
  public static final int POMME = -13312;
  public static final int SPIRALE = -11698023;

  public void captureEcran()
  {
    try
    {
      Robot robot = new Robot();
      this.image = robot.createScreenCapture(
        new Rectangle(Toolkit.getDefaultToolkit().getScreenSize()));
    }
    catch (AWTException e)
    {
      e.printStackTrace();
    }
  }

  public boolean compareImage() {
    this.imageComp = toBufferedImage(this.intImg.loadImage(10));

    int haut = this.image.getHeight(null) - this.imageComp.getHeight(null);
    int lar = this.image.getWidth(null) - this.imageComp.getWidth(null);
    int posX = 0;
    int posY = 0;
    boolean rech = false;
    for (int j = 0; j < haut; j++) {
      for (int i = 0; i < lar; i++) {
        if (!testImage(i, j))
          continue;
        rech = true;
        posX = i + 61;
        posY = j + 43;

        j = haut;
        System.out.println("[" + posX + "," + posY + "]");
        break;
      }
    }

    if (!rech) return rech;

    for (int j = 0; j < 7; j++) {
      for (int i = 0; i < 6; i++) {
        int[] tab = rechercheValeur(posX + i * 36, posY + j * 36);
        this.info[j][i] = tab[0];
      }

    }

    int[] resul = new int[2];
    int[] valeur = { 0, -1 };

    for (int y = 0; y < 280; y++)
    {
      resul = rechercheValeur(posX - 36, posY + y);
      if ((resul[0] != 0) && (resul[0] < 5) && (resul[1] == 0)) {
        valeur[1] = resul[1];
        valeur[0] = resul[0];
        break;
      }
      if ((valeur[1] == -1) || (resul[1] < valeur[1])) {
        valeur[1] = resul[1];
        valeur[0] = resul[0];
      }

      resul = rechercheValeur(posX + 216, posY + y);
      if ((resul[0] != 0) && (resul[0] < 5) && (resul[1] == 0)) {
        valeur[1] = resul[1];
        valeur[0] = resul[0];
        break;
      }
      if ((valeur[1] == -1) || (resul[1] < valeur[1])) {
        valeur[1] = resul[1];
        valeur[0] = resul[0];
      }
    }

    this.action = valeur[0];
    return true;
  }

  public int[] rechercheValeur(int x, int y) {
    int rgb = this.image.getRGB(x, y);
    int[] resul = new int[2];

    int valeur = 0;
    switch (rgb) { case -11076091:
      valeur = 3; break;
    case -3644159:
      valeur = 4; break;
    case -9491771:
      valeur = 2; break;
    case -5239022:
      valeur = 1; break;
    case -13312:
      valeur = 5; break;
    case -11698023:
      valeur = 6;
    }
    if (valeur > 0) {
      resul[0] = valeur;
      resul[1] = 0;
      return resul;
    }
    int ecart = -1; int ecart2 = 0; int couleur = 0; int val = 0;
    for (int i = 0; i < 6; i++) {
      switch (i) { case 0:
        couleur = -11076091; val = 3; break;
      case 1:
        couleur = -3644159; val = 4; break;
      case 2:
        couleur = -9491771; val = 2; break;
      case 3:
        couleur = -5239022; val = 1; break;
      case 4:
        couleur = -13312; val = 5; break;
      case 5:
        couleur = -11698023; val = 6;
      }
      ecart2 = testCouleur(rgb, couleur);
      if ((ecart == -1) || (ecart2 <= ecart)) {
        ecart = ecart2;
        resul[0] = val;
      }
    }
    resul[1] = ecart;

    return resul;
  }
  public boolean testImage(int x, int y) {
    for (int j = 0; j < this.imageComp.getHeight(null); j++) {
      for (int i = 0; i < this.imageComp.getWidth(null); i++) {
        int rgv = this.image.getRGB(x + i, y + j);
        int rgv2 = this.imageComp.getRGB(i, j);
        if (rgv != rgv2) return false;
      }
    }

    return true;
  }

  public int testCouleur(int couleur1, int couleur2) {
    int r1 = (couleur1 & 0xFF0000) >> 16;
    int r2 = (couleur2 & 0xFF0000) >> 16;
    int g1 = (couleur1 & 0xFF00) >> 8;
    int g2 = (couleur2 & 0xFF00) >> 8;
    int b1 = couleur1 & 0xFF;
    int b2 = couleur2 & 0xFF;
    int distance = (r1 - r2) * (r1 - r2) + (g1 - g2) * (g1 - g2) + (b1 - b2) * (b1 - b2);
    return distance;
  }

  public BufferedImage toBufferedImage(Image image) {
    if ((image instanceof BufferedImage)) {
      return (BufferedImage)image;
    }

    image = new ImageIcon(image).getImage();

    BufferedImage bufferedImage = new BufferedImage(
      image.getWidth(null), 
      image.getHeight(null), 
      1);

    Graphics g = bufferedImage.createGraphics();
    g.drawImage(image, 0, 0, null);
    g.dispose();

    return bufferedImage;
  }

  public void setInfo(int[][] info)
  {
    this.info = info;
  }
  public void setImage(BufferedImage image) {
    this.image = image;
  }
  public BufferedImage getImage() {
    return this.image;
  }
  public int[][] getInfo() {
    return this.info;
  }
  public void setIntImg(InterfaceImage intImg) {
    this.intImg = intImg;
  }
  public int getAction() {
    return this.action;
  }
}

