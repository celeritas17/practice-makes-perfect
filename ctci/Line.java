public class Line{
	public static double epsilon = 0.000001;
	public double slope;
	public double yintersect;

	public Line(double slope, double yintersect){
		this.slope = slope;
		this.yintersect = yintersect;
	}

	public boolean intersect(Line line){
		return Math.abs(this.slope - line.slope) > this.epsilon || Math.abs(this.yintersect - line.yintersect) < this.epsilon;
	}

	public static void main(String[] args){
		Line line1 = new Line(1, 0); // y = x
		Line line2 = new Line(-1, 1); // y = -x + 1
		Line line3 = new Line(1.0000000000001, 0); // y = x within our precision
		Line line4 = new Line(1, 1); // y = x + 1

		System.out.println("y = x intersects y = -x + 1: " + line1.intersect(line2)); // true (different slope)
		System.out.println("y = x intersects y = 1.0000000000001x + 1: " + line1.intersect(line3)); // true (same line)
		System.out.println("y = x intersects y = x + 1: " + line1.intersect(line4)); // false (same slope, not same line)
	}
}
