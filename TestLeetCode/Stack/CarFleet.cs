
internal class Car {
    public Car(int position, int speed)
    {
        Position = position;
        Speed = speed;
    }
    public int Position { get; set;}
    public int Speed { get; set;}

}

public class CarFleetSolution2 {
     public int CarFleet(int target, int[] position, int[] speed) {
        var cars = new List<Car>();
        for (int i = 0; i < position.Length; i++) {
            cars.Add(new Car(position[i], speed[i]));
        }

        cars.Sort((a, b) => b.Position.CompareTo(a.Position));

        var times = new List<double>();

        foreach (var car in cars) {
            int pos = car.Position;
            int spd = car.Speed;
            double time = (double)(target - pos) / spd;

            if (times.Count > 0 && time <= times[times.Count - 1]) {
                continue;
            }

            times.Add(time);
        }

        return times.Count;
    }
}
public class CarFleetSolution {
     public int CarFleet(int target, int[] position, int[] speed) {
        var cars = new List<Tuple<int, int>>();
        for (int i = 0; i < position.Length; i++) {
            cars.Add(new Tuple<int, int>(position[i], speed[i]));
        }

        cars.Sort((a, b) => b.Item1.CompareTo(a.Item1));

        var times = new List<double>();

        foreach (var car in cars) {
            int pos = car.Item1;
            int spd = car.Item2;
            double time = (double)(target - pos) / spd;

            if (times.Count > 0 && time <= times[times.Count - 1]) {
                continue;
            }

            times.Add(time);
        }

        return times.Count;
    }
}
