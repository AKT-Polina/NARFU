```c#
using System.Drawing;
using System.Drawing.Imaging;

public Bitmap ApplyGrayscale(Image source)
{
    // Создаем пустой Bitmap того же размера
    Bitmap result = new Bitmap(source.Width, source.Height);

    // Матрица для перевода в оттенки серого
    ColorMatrix matrix = new ColorMatrix(new float[][]
    {
        new float[] {.3f, .3f, .3f, 0, 0},   // Red
        new float[] {.59f, .59f, .59f, 0, 0}, // Green
        new float[] {.11f, .11f, .11f, 0, 0}, // Blue
        new float[] {0, 0, 0, 1, 0},          // Alpha
        new float[] {0, 0, 0, 0, 1}           // Offset
    });

    using (Graphics g = Graphics.FromImage(result))
    {
        ImageAttributes attributes = new ImageAttributes();
        attributes.SetColorMatrix(matrix);

        // Рисуем исходное фото на новое с применением атрибутов
        g.DrawImage(source, new Rectangle(0, 0, source.Width, source.Height),
                    0, 0, source.Width, source.Height, GraphicsUnit.Pixel, attributes);
    }
    return result;
}

```
