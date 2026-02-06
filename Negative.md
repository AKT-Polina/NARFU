```c#
public Bitmap ApplyInvert(Image source)
{
    Bitmap result = new Bitmap(source.Width, source.Height);

    // Матрица инверсии
    ColorMatrix matrix = new ColorMatrix(new float[][]
    {
        new float[] {-1,  0,  0,  0, 0}, // Инверсия красного
        new float[] { 0, -1,  0,  0, 0}, // Инверсия зеленого
        new float[] { 0,  0, -1,  0, 0}, // Инверсия синего
        new float[] { 0,  0,  0,  1, 0}, // Альфа-канал (не меняем)
        new float[] { 1,  1,  1,  0, 1}  // Смещение (добавляем 1 к каждому каналу)
    });

    using (Graphics g = Graphics.FromImage(result))
    {
        using (ImageAttributes attributes = new ImageAttributes())
        {
            attributes.SetColorMatrix(matrix);
            g.DrawImage(source, new Rectangle(0, 0, source.Width, source.Height),
                0, 0, source.Width, source.Height, GraphicsUnit.Pixel, attributes);
        }
    }
    return result;
}

```
